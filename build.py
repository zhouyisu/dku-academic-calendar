#!/usr/bin/env python3
"""Build one combined .ics from every academic year in years/.

    python3 build.py

Reads every years/ay*.py module and writes a single dku_academic_calendar.ics
containing all of them. Subscribers see whatever is in that one file, so
adding a year is: drop in years/ay2027_28.py, rerun, commit.

Adding a year
-------------
1. cp years/ay2026_27.py years/ay2027_28.py
2. Set AY and SOURCE_URL at the top
3. Replace EVENTS. Each row is:

       ("2027-08-23", None, "Fall 2027 classes begin", "Monday. Classes begin.")
       #  start        end   short title (calendar)     verbatim registrar text

   start/end : "YYYY-MM-DD"       -> all-day
               "YYYY-MM-DD HH:MM" -> timed, Asia/Shanghai
   end       : None for a single day, else the LAST day of the range
               (inclusive - the off-by-one iCalendar wants is handled here)
4. Update SESSIONS: one entry per 7-week undergraduate session, listing the
   Monday of each of its seven teaching weeks plus the Monday of its finals
   week. build.py turns these into "Week 1" ... "Week 7" / "Week 8 Final"
   all-day banners (Mon-Sun). A week that a holiday splits or shifts can be
   given as (start, end, note) instead of a bare Monday. The checks below
   refuse a session that does not have exactly seven weeks ending before its
   finals Monday, so a miscounted holiday fails loudly.
5. python3 build.py && git commit -am "Add AY2027-28" && git push

Editing an existing year: change the row, rerun, commit. Because event IDs are
derived from the academic year + date + title, an edited *title or date* is
seen as a new event and the old one disappears from subscribers; an edited
description updates in place. Either way subscribers converge on the file -
that is the point of subscribing rather than importing.
"""

import hashlib
import importlib.util
import pathlib
from datetime import date, timedelta

HERE = pathlib.Path(__file__).parent
OUTFILE = HERE / "dku_academic_calendar.ics"
CAL_NAME = "DKU Academic Calendar"
CAL_DESC = ("Duke Kunshan University academic calendar. Transcribed from the "
            "Office of the Registrar. Calendar subject to change.")
UID_DOMAIN = "dku-academic-calendar.local"
HOME_URL = "https://registrar.dukekunshan.edu.cn/academic-calendar/"

# Deliberately a fixed constant, not the current time: it keeps rebuilds
# byte-identical, so `git status` after `python3 build.py` shows a diff only
# when the calendar data actually changed. Clients resolve updates by UID
# (and SEQUENCE), so a static DTSTAMP costs nothing here.
BUILD_STAMP = "20260722T000000Z"


def esc(text):
    """Escape per RFC 5545 section 3.3.11."""
    return (text.replace("\\", "\\\\")
                .replace(";", "\\;")
                .replace(",", "\\,")
                .replace("\n", "\\n"))


def fold(line):
    """Fold to 75 octets per RFC 5545 section 3.1, without splitting a
    multi-byte character across the continuation."""
    raw = line.encode("utf-8")
    if len(raw) <= 75:
        return line
    out, chunk, limit = [], b"", 75
    for ch in line:                        # whole characters, never split
        b = ch.encode("utf-8")
        if len(chunk) + len(b) > limit:
            out.append(chunk)
            chunk, limit = b, 74           # continuation lines lose 1 to the leading space
        else:
            chunk += b
    out.append(chunk)
    return "\r\n ".join(c.decode("utf-8") for c in out)


def uid(*parts):
    h = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:20]
    return f"{h}@{UID_DOMAIN}"


WEEKS_PER_SESSION = 7
WEEKS_CATEGORY = "DKU Weeks"
DERIVED_NOTE = ("(Week numbers are derived from the registrar's session dates; "
                "the registrar does not print them.)")


def week_range(entry):
    """A SESSIONS week is "YYYY-MM-DD" (a Monday; the week is Mon-Sun) or
    (start, end[, note]) for a week a holiday splits or shifts."""
    if isinstance(entry, str):
        first = date.fromisoformat(entry)
        return first, first + timedelta(days=6), None
    start, end, *rest = entry
    return date.fromisoformat(start), date.fromisoformat(end), (rest or [None])[0]


def expand_sessions(year):
    """Turn a year's SESSIONS table into (start, end, summary, description)
    rows, one per teaching week plus one for the finals week."""
    rows = []
    for session in getattr(year, "SESSIONS", []):
        name, weeks, finals = session["name"], session["weeks"], session["finals"]
        if len(weeks) != WEEKS_PER_SESSION:
            raise SystemExit(f"{name}: expected {WEEKS_PER_SESSION} weeks, "
                             f"got {len(weeks)}")
        finals_first = date.fromisoformat(finals)
        if finals_first.weekday() != 0:
            raise SystemExit(f"{name}: finals week must start on a Monday "
                             f"({finals})")
        prev_end = None
        for n, entry in enumerate(weeks, 1):
            first, last, note = week_range(entry)
            if first.weekday() != 0:
                raise SystemExit(f"{name} week {n}: {first} is not a Monday")
            if prev_end and first <= prev_end:
                raise SystemExit(f"{name} week {n}: overlaps week {n - 1}")
            if last >= finals_first:
                raise SystemExit(f"{name} week {n}: runs into finals week")
            prev_end = last
            text = (f"Week {n} of {WEEKS_PER_SESSION}, {name}. "
                    f"{first:%a %-d %b} - {last:%a %-d %b %Y}.")
            if note:
                text += " " + note
            text += " " + DERIVED_NOTE
            rows.append((first.isoformat(), last.isoformat(),
                         f"Week {n} ({name})", text))
        finals_last = finals_first + timedelta(days=6)
        rows.append((finals, finals_last.isoformat(),
                     f"Week {WEEKS_PER_SESSION + 1} Final ({name})",
                     f"Final examinations week, {name}. "
                     f"{finals_first:%a %-d %b} - {finals_last:%a %-d %b %Y}. "
                     "See the registrar's reading-period and final-examination "
                     "events for the exact days. " + DERIVED_NOTE))
    return rows


def categories_line(*cats):
    return fold("CATEGORIES:" + ",".join(esc(c) for c in cats))


def load_years():
    """Import every years/ay*.py, oldest first."""
    years = []
    for path in sorted((HERE / "years").glob("ay*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        years.append(mod)
    return years


def build():
    years = load_years()
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//DKU Academic Calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        fold(f"X-WR-CALNAME:{esc(CAL_NAME)}"),
        fold(f"X-WR-CALDESC:{esc(CAL_DESC)}"),
        "X-WR-TIMEZONE:Asia/Shanghai",
        "REFRESH-INTERVAL;VALUE=DURATION:P1D",
        "X-PUBLISHED-TTL:P1D",
        f"SOURCE;VALUE=URI:{HOME_URL}",
        # China has had no DST since 1991: one fixed +08:00 standard rule.
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Shanghai",
        "BEGIN:STANDARD",
        "DTSTART:19910915T000000",
        "TZOFFSETFROM:+0900",
        "TZOFFSETTO:+0800",
        "TZNAME:CST",
        "END:STANDARD",
        "END:VTIMEZONE",
    ]

    total = 0
    seen_uids = set()
    for year in years:
        # Optional per-module overrides for non-registrar sources (e.g. an
        # emailed notice): CATEGORY, and SOURCE text in place of SOURCE_URL.
        source_url = year.SOURCE_URL
        source = getattr(year, "SOURCE", source_url)
        category = getattr(year, "CATEGORY", f"DKU AY{year.AY}")
        rows = ([(*row, (category,)) for row in year.EVENTS] +
                [(*row, (category, WEEKS_CATEGORY))
                 for row in expand_sessions(year)])
        for start, end, summary, description, cats in rows:
            u = uid(year.AY, start, summary)
            if u in seen_uids:
                raise SystemExit(
                    f"Duplicate event ID in AY{year.AY}: {start} {summary!r}. "
                    "Two rows share a year, start and title - vary the title.")
            seen_uids.add(u)

            lines.append("BEGIN:VEVENT")
            lines.append(f"UID:{u}")
            lines.append(f"DTSTAMP:{BUILD_STAMP}")
            lines.append("SEQUENCE:0")
            if " " in start:                       # timed
                d, t = start.split()
                ts = d.replace("-", "") + "T" + t.replace(":", "") + "00"
                lines.append(f"DTSTART;TZID=Asia/Shanghai:{ts}")
                lines.append(f"DTEND;TZID=Asia/Shanghai:{ts}")
            else:                                  # all-day
                first = date.fromisoformat(start)
                last = date.fromisoformat(end) if end else first
                if last < first:
                    raise SystemExit(f"End before start: {start}..{end} {summary!r}")
                lines.append(f"DTSTART;VALUE=DATE:{first:%Y%m%d}")
                # DTEND is exclusive for all-day events.
                lines.append(f"DTEND;VALUE=DATE:{last + timedelta(days=1):%Y%m%d}")
            lines.append(fold(f"SUMMARY:{esc(summary)}"))
            lines.append(fold(
                f"DESCRIPTION:{esc(description)}\\n\\nAY{year.AY} \u2014 "
                f"source: {esc(source)}"))
            if source_url:
                lines.append(fold(f"URL:{source_url}"))
            lines.append("LOCATION:Duke Kunshan University")
            lines.append(categories_line(*cats))
            lines.append("TRANSP:TRANSPARENT")
            lines.append("STATUS:CONFIRMED")
            lines.append("END:VEVENT")
            total += 1

    lines.append("END:VCALENDAR")

    # open() rather than write_text(newline=...), so the stock macOS
    # python3 (3.9) can run this too.
    with OUTFILE.open("w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines) + "\r\n")

    def count(y):
        n_weeks = len(expand_sessions(y))
        return (f"{len(y.EVENTS)}" if not n_weeks
                else f"{len(y.EVENTS)} + {n_weeks} week banners")
    label = ", ".join(f"{getattr(y, 'CATEGORY', f'AY{y.AY}')} ({count(y)})"
                      for y in years)
    print(f"Wrote {OUTFILE.name}: {total} events across {len(years)} years")
    print(f"  {label}")

    # Cheap self-checks, so a bad commit fails loudly rather than quietly
    # breaking everyone's subscription.
    with OUTFILE.open(encoding="utf-8", newline="") as f:
        raw = f.read()
    over = [l for l in raw.split("\r\n") if len(l.encode()) > 75]
    assert not over, f"{len(over)} line(s) exceed 75 octets"
    assert raw.count("BEGIN:VEVENT") == raw.count("END:VEVENT") == total
    assert raw.endswith("END:VCALENDAR\r\n")
    print("  self-checks passed")


if __name__ == "__main__":
    build()
