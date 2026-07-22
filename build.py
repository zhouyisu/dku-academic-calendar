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
4. python3 build.py && git commit -am "Add AY2027-28" && git push

Editing an existing year: change the row, rerun, commit. Because event IDs are
derived from the academic year + date + title, an edited *title or date* is
seen as a new event and the old one disappears from subscribers; an edited
description updates in place. Either way subscribers converge on the file -
that is the point of subscribing rather than importing.
"""

import hashlib
import importlib.util
import pathlib
from datetime import date, datetime, timedelta, timezone

HERE = pathlib.Path(__file__).parent
OUTFILE = HERE / "dku_academic_calendar.ics"
CAL_NAME = "DKU Academic Calendar"
CAL_DESC = ("Duke Kunshan University academic calendar. Transcribed from the "
            "Office of the Registrar. Calendar subject to change.")
UID_DOMAIN = "dku-academic-calendar.local"
HOME_URL = "https://registrar.dukekunshan.edu.cn/academic-calendar/"


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
    for byte in raw:
        if len(chunk) + 1 > limit and (byte & 0xC0) != 0x80:
            out.append(chunk)
            chunk, limit = bytes([byte]), 74   # continuation lines lose 1 to the leading space
        else:
            chunk += bytes([byte])
    out.append(chunk)
    return "\r\n ".join(c.decode("utf-8") for c in out)


def uid(*parts):
    h = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:20]
    return f"{h}@{UID_DOMAIN}"


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
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

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
        for start, end, summary, description in year.EVENTS:
            u = uid(year.AY, start, summary)
            if u in seen_uids:
                raise SystemExit(
                    f"Duplicate event ID in AY{year.AY}: {start} {summary!r}. "
                    "Two rows share a year, start and title - vary the title.")
            seen_uids.add(u)

            lines.append("BEGIN:VEVENT")
            lines.append(f"UID:{u}")
            lines.append(f"DTSTAMP:{stamp}")
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
                f"DESCRIPTION:{esc(description)}\\n\\nAY{year.AY} \\u2014 "
                f"source: {year.SOURCE_URL}"))
            lines.append(fold(f"URL:{year.SOURCE_URL}"))
            lines.append("LOCATION:Duke Kunshan University")
            lines.append(fold(f"CATEGORIES:{esc(f'DKU AY{year.AY}')}"))
            lines.append("TRANSP:TRANSPARENT")
            lines.append("STATUS:CONFIRMED")
            lines.append("END:VEVENT")
            total += 1

    lines.append("END:VCALENDAR")

    OUTFILE.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8", newline="")

    label = ", ".join(f"AY{y.AY} ({len(y.EVENTS)})" for y in years)
    print(f"Wrote {OUTFILE.name}: {total} events across {len(years)} years")
    print(f"  {label}")

    # Cheap self-checks, so a bad commit fails loudly rather than quietly
    # breaking everyone's subscription.
    raw = OUTFILE.read_text(encoding="utf-8", newline="")
    over = [l for l in raw.split("\r\n") if len(l.encode()) > 75]
    assert not over, f"{len(over)} line(s) exceed 75 octets"
    assert raw.count("BEGIN:VEVENT") == raw.count("END:VEVENT") == total
    assert raw.endswith("END:VCALENDAR\r\n")
    print("  self-checks passed")


if __name__ == "__main__":
    build()
