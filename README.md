# DKU Academic Calendar (.ics)

An importable / subscribable calendar of Duke Kunshan University academic
dates, transcribed from the [Office of the
Registrar](https://registrar.dukekunshan.edu.cn/academic-calendar/).

**Currently covers AY2025-26 and AY2026-27 — 126 events**, including Sports
Complex holiday closures from Athletics notices.

## Subscribe

Copy this URL:

```
https://raw.githubusercontent.com/zhouyisu/dku-academic-calendar/main/dku_academic_calendar.ics
```

**macOS Calendar** → File → New Calendar Subscription → paste →
set **Location: iCloud** (so it syncs to your iPhone and iPad automatically —
"On My Mac" strands it on the laptop), **Auto-refresh: Every day**, and tick
**Remove: Alerts**.

**iPhone / iPad** (only needed if you didn't use iCloud above) → Settings →
Apps → Calendar → Calendar Accounts → Add Account → Other → Add Subscribed
Calendar → paste.

**Google Calendar** → Other calendars → **+** → **From URL** → paste. Note that
Google re-polls subscribed URLs on its own schedule and can lag a day or more.

**Sharing with someone else:** send them the same URL with `https://` swapped
for `webcal://`. That makes it a clickable link that opens their calendar app
straight into the subscribe dialog.

Subscribing is a live mirror: when a new academic year is added to the file, it
appears on its own. You never re-import, and you only ever have one DKU
calendar in your sidebar.

*(If you'd rather have a one-time copy that never updates, download the `.ics`
and double-click it instead.)*

## What's in it

- Multi-day items (holidays, reading periods, exam periods) are **single
  all-day events spanning the range**, not one event per day.
- Move-in times and residence-hall closings are **timed events** in
  Asia/Shanghai, so they stay right if you travel.
- Every event carries the registrar's **verbatim wording** in the notes, plus
  the academic year and a link to the source.
- Events are marked free (`TRANSP:TRANSPARENT`), so the calendar doesn't make
  you look busy to colleagues checking your availability.
- Each event is tagged with its academic year (`DKU AY2026-27`) as a category.
- Sports Complex closures and holiday service hours from Athletics emails are
  tagged `DKU Athletics` and name the notice as their source. To add a future
  notice, add rows to (or copy) `years/ay2026_27_athletics.py` — set
  `SOURCE_URL = None` plus a `SOURCE` line when there's no web page to link.

## Repo layout

```
build.py                     the generator + self-checks
years/ay2025_26.py           one editable table per academic year
years/ay2026_27.py
years/ay2026_27_athletics.py Sports Complex / facility notices (not from the registrar)
dku_academic_calendar.ics    the built output — this is what people subscribe to
```

## Adding next year

1. `cp years/ay2026_27.py years/ay2027_28.py`
2. Set `AY` and `SOURCE_URL` at the top
3. Replace the `EVENTS` table. Each row is one line:

   ```python
   ("2027-08-23", None, "Fall 2027 classes begin", "Monday. Classes begin."),
   #  start        end   short title (calendar)     verbatim registrar text
   ```

   - `end = None` → single day. Otherwise the **last day** of the range,
     inclusive — `build.py` handles the off-by-one that iCalendar requires.
   - Add a time to the start (`"2027-08-14 09:00"`) for a timed event.
4. `python3 build.py` — it rebuilds and runs self-checks
5. Commit and push. The subscription URL never changes.

Nothing else needs touching; `build.py` picks up any `years/ay*.py`
automatically and sorts by filename.

Fastest way to do step 3: paste the registrar's page text to an LLM and ask it
to produce the `EVENTS` table in this format. Then spot-check five or six dates
against the source — the registrar's own day-of-week labels occasionally
disagree with their dates, so one human pass is still worth it.

## Editing the .ics by hand (don't, but if you must)

It's plain text, but the format has several ways to break silently: lines must
end in **CRLF**, no line may exceed **75 bytes** (longer ones are folded onto a
continuation line starting with a space), `DTEND` for all-day events is
**exclusive** (a one-day event on the 24th ends on the 25th), and commas and
semicolons in text must be backslash-escaped. Edit the year tables and rerun
`build.py` instead.

## Caveats

- The registrar states **"CALENDAR SUBJECT TO CHANGE."** AY2026-27 is a
  snapshot taken 2026-07-22.
- Two AY2026-27 ranges are marked **(Tentative)** in their titles, matching the
  source.
- Chinese national holiday dates (Mid-Autumn, National Day, Spring Festival,
  Qing Ming, Labor Day) are set annually by the State Council and DKU sometimes
  adjusts them after publishing. These are the dates as printed.
- The spring 2026 section of the AY2025-26 source PDF never gives the date the
  second 7-week undergraduate session ends. Rather than guess, that row is
  absent. Every other printed row is present.
- Unofficial and community-maintained. Confirm anything that matters against
  the registrar.

## Source documents

| Year | Source |
|---|---|
| AY2025-26 | [PDF](https://newstatic.dukekunshan.edu.cn/mainsite/2025/11/21102804/DKU-Acdemic-Calendar-2025-2026_250919_v2.pdf) (registrar's "Past Academic Calendars") |
| AY2026-27 | [Registrar's Academic Calendar page](https://registrar.dukekunshan.edu.cn/academic-calendar/) |
