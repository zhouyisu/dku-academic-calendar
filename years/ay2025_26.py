"""DKU Academic Calendar AY2025-2026.

Source: DKU-Acdemic-Calendar-2025-2026_250919_v2.pdf (linked from the
registrar's "Past Academic Calendars" list). PDF header says "Updated
March 3, 2025".

Note on fidelity: the spring 2026 section of the source PDF never states the
date the second 7-week undergraduate session ends (fall 2025 does, and both
terms do in AY2026-27). That row is absent here rather than guessed.
"""

AY = "2025-26"
SOURCE_URL = ("https://newstatic.dukekunshan.edu.cn/mainsite/2025/11/21102804/"
              "DKU-Acdemic-Calendar-2025-2026_250919_v2.pdf")

EVENTS = [
    # ---------------- Fall 2025 -------------------------------------------
    ("2025-08-08 09:00", None, "Move-in: new international UG + int'l 1st-year grad",
     "Friday at 9:00 AM. All new international undergraduate students "
     "(Class of 2029) and international first-year graduate students move-in."),
    ("2025-08-10 09:00", None, "Move-in: new Chinese UG + Chinese 1st-year grad",
     "Sunday at 9:00 AM. All new Chinese undergraduate students (Class of "
     "2029) and Chinese first-year graduate students move-in."),
    ("2025-08-15 09:00", None, "Move-in: returning UG + grad students",
     "Friday at 9:00 AM. Returning undergraduate and graduate students move-in."),
    ("2025-08-18", None, "Fall 2025 classes begin (UG + grad)",
     "Monday. Undergraduate and graduate classes begin."),
    ("2025-08-21", None, "Drop/add ends - 1st 7-week UG session",
     "Thursday. Drop/add ends for first 7-week undergraduate session."),
    ("2025-08-28", None, "Drop/add ends - 14-week UG session",
     "Thursday. Drop/add ends for 14-week undergraduate session."),
    ("2025-08-29", None, "Drop/add ends - graduate classes",
     "Friday. Drop/add ends for graduate classes."),
    ("2025-09-18", None, "Deadlines - 1st 7-week W / grading basis / I grades",
     "Thursday. Last day to withdraw with a W grade of first 7-week classes; "
     "Last day to change grading basis of first 7-week classes; Last day to "
     "resolve I grade of second seven-week classes in spring 2025."),
    ("2025-10-01", "2025-10-08", "National Day + Mid-Autumn Festival - No classes",
     "Wednesday - Wednesday. National Day Holiday and Mid-autumn Festival - "
     "No classes."),
    ("2025-10-09", None, "All classes resume; Wednesday class schedule in effect",
     "Thursday. All classes resume. The Wednesday class meeting schedule is "
     "in effect on this day."),
    ("2025-10-10", None, "Thursday class schedule in effect; 1st 7-week UG session ends",
     "Friday. The Thursday meeting schedule is in effect on this day. First "
     "7-week undergraduate session end."),
    ("2025-10-11", "2025-10-12", "UG reading period",
     "Saturday-Sunday. Undergraduate reading period."),
    ("2025-10-13", "2025-10-16", "1st 7-week UG final examinations",
     "Monday-Thursday. First 7-week undergraduate session final examinations. "
     "Graduate classes continue."),
    ("2025-10-20", None, "2nd 7-week UG session begins",
     "Monday. Second 7-week undergraduate session begins."),
    ("2025-10-23", None, "Drop/add ends - 2nd 7-week UG session",
     "Thursday. Drop/add ends for second 7-week undergraduate session."),
    ("2025-11-06", None, "Deadlines - 14-week W / grading basis",
     "Thursday. Last day to withdraw with a W grade of 14-week classes. Last "
     "day to change grading basis of 14-week classes."),
    ("2025-11-20", None, "Graduate classes end; 2nd 7-week W / grading / I deadlines",
     "Thursday. Graduate classes end (ECE classes continue); Last day to "
     "withdraw with a W grade of second 7-week classes; Last day to change "
     "grading basis of second 7-week classes; Last day to resolve I grade of "
     "first 7-week classes."),
    ("2025-11-21", "2025-11-25", "Graduate reading days",
     "Friday-Tuesday. Graduate reading days; ECE classes continue."),
    ("2025-11-26", "2025-11-28", "Graduate exams",
     "Wednesday-Friday. Graduate exams."),
    ("2025-11-27", None, "ECE classes end",
     "Thursday. ECE classes end."),
    ("2025-11-28", "2025-12-02", "ECE program reading days",
     "Friday-Tuesday. ECE program reading days."),
    ("2025-12-03", "2025-12-05", "ECE program exam period",
     "Wednesday-Friday. ECE program exam period."),
    ("2025-12-04", None, "2nd 7-week UG session ends",
     "Thursday. Second 7-week undergraduate session ends."),
    ("2025-12-05", "2025-12-07", "UG reading period",
     "Friday-Sunday. Undergraduate reading period."),
    ("2025-12-08", "2025-12-11", "UG final examinations",
     "Monday-Thursday. Undergraduate final examinations."),
    ("2025-12-12 13:00", None, "Residence halls close for Winter Break",
     "Friday at 13:00. All residence halls close for Winter Break."),

    # ---------------- Spring 2026 -----------------------------------------
    ("2026-01-03 09:00", None, "Residence halls reopen",
     "Saturday at 9:00 AM. All residence halls reopen."),
    ("2026-01-05", None, "Spring 2026 classes begin (UG + grad)",
     "Monday. Undergraduate and graduate classes begin."),
    ("2026-01-08", None, "Drop/add ends - 1st 7-week UG session",
     "Thursday. Drop/add ends for first 7-week undergraduate session."),
    ("2026-01-15", None, "Drop/add ends - 14-week UG session",
     "Thursday. Drop/add ends for 14-week undergraduate session."),
    ("2026-01-16", None, "Drop/add ends - graduate classes",
     "Friday. Drop/add ends for graduate classes."),
    ("2026-02-05", None, "Deadlines - 1st 7-week W / grading basis / I grades",
     "Thursday. Last day to withdraw with a W grade of first 7-week classes; "
     "Last day to change grading basis of first 7-week classes; Last day to "
     "resolve I grade of fall 2025 second 7-week classes."),
    ("2026-02-13", None, "Monday class schedule in effect",
     "Friday. The Monday class schedule is in effect on this day."),
    ("2026-02-16", "2026-02-23", "Spring Festival (Chinese New Year) - No classes",
     "Monday-Monday. Spring Festival Holiday - Chinese New Year - No classes."),
    ("2026-02-24", None, "All classes resume",
     "Tuesday. All classes resume."),
    ("2026-02-26", None, "1st 7-week UG session ends",
     "Thursday. First 7-week undergraduate session ends."),
    ("2026-02-27", "2026-03-01", "UG reading days",
     "Friday-Sunday. Undergraduate Reading Days."),
    ("2026-03-02", "2026-03-05", "1st 7-week UG final examinations",
     "Monday-Thursday. First 7-week undergraduate session final examinations. "
     "Graduate classes continue."),
    ("2026-03-09", "2026-03-13", "Mini-term week (UG) / Spring recess (grad)",
     "Monday-Friday. Mini-term week for undergraduate students; Spring recess "
     "for graduate programs."),
    ("2026-03-16", None, "2nd 7-week UG session begins",
     "Monday. Second 7-week undergraduate session begins."),
    ("2026-03-19", None, "Drop/add ends - 2nd 7-week UG session",
     "Thursday. Drop/add ends for second 7-week undergraduate session."),
    ("2026-04-02", None, "Deadlines - 14-week W / grading basis",
     "Thursday. Last day to withdraw with a W grade of 14-week classes. Last "
     "day to change grading basis of 14-week classes."),
    ("2026-04-03", "2026-04-05", "Qing Ming (Tomb Sweeping Day) - No classes",
     "Friday-Sunday. Qing Ming - Tomb Sweeping Day - No classes."),
    ("2026-04-16", None, "Graduate classes end; 2nd 7-week W / grading / I deadlines",
     "Thursday. Graduate classes end (ECE classes continue); Last day to "
     "withdraw with a W grade of second 7-week classes; Last day to change "
     "grading basis for second 7-week classes; Last day for I grade change of "
     "spring 2026 first 7-week classes."),
    ("2026-04-17", "2026-04-21", "Graduate reading days",
     "Friday-Tuesday. Graduate Reading Days."),
    ("2026-04-22", "2026-04-24", "Graduate exams",
     "Wednesday-Friday. Graduate exams; ECE classes continue."),
    ("2026-04-23", None, "ECE classes end",
     "Thursday. ECE Classes end."),
    ("2026-04-24", "2026-04-26", "ECE program reading days",
     "Friday-Sunday. ECE program reading days."),
    ("2026-04-27", "2026-04-29", "ECE program exam period",
     "Monday-Wednesday. ECE program exam period."),
    ("2026-05-01", "2026-05-03", "International Labor Day Holiday - No classes",
     "Friday-Sunday. International Labor Day Holiday - No classes."),
    ("2026-05-01", "2026-05-03", "UG reading days",
     "Friday-Sunday. Undergraduate Reading Days."),
    ("2026-05-04", "2026-05-07", "UG final exam period",
     "Monday-Thursday. Undergraduate final exam period."),
    ("2026-05-15", None, "Commencement (Graduate + Undergraduate)",
     "Friday. Graduate and Undergraduate Commencement."),
    ("2026-05-16 13:00", None, "All residence halls close",
     "Saturday at 13:00. All residence halls close."),
]

# Teaching weeks of each 7-week undergraduate session, for the "Week N"
# banners. Each entry is the Monday of a Mon-Sun week; a holiday-disrupted
# week is (start, end, note). Seven weeks per session; `finals` is the Monday
# of the exam week ("Week 8 Final"). A calendar week that is entirely holiday
# (Spring Festival) is simply not listed, so the count resumes after it.
SESSIONS = [
    {
        "name": "Fall 2025 Session 1",
        "weeks": [
            "2025-08-18", "2025-08-25", "2025-09-01", "2025-09-08",
            "2025-09-15", "2025-09-22",
            ("2025-09-29", "2025-10-12",
             "Split by the National Day / Mid-Autumn holiday (1-8 Oct): "
             "Mon/Tue classes on 29-30 Sep, then the Wednesday schedule on "
             "Thu 9 Oct and the Thursday schedule on Fri 10 Oct, when the "
             "session ends."),
        ],
        "finals": "2025-10-13",
    },
    {
        "name": "Fall 2025 Session 2",
        "weeks": [
            "2025-10-20", "2025-10-27", "2025-11-03", "2025-11-10",
            "2025-11-17", "2025-11-24", "2025-12-01",
        ],
        "finals": "2025-12-08",
    },
    {
        "name": "Spring 2026 Session 1",
        "weeks": [
            "2026-01-05", "2026-01-12", "2026-01-19", "2026-01-26",
            "2026-02-02",
            ("2026-02-09", "2026-02-15",
             "Fri 13 Feb runs the Monday class schedule, making up for "
             "Mon 23 Feb (Spring Festival)."),
            # 16-22 Feb is entirely Spring Festival holiday: no week number.
            ("2026-02-23", "2026-03-01",
             "Mon 23 Feb is still Spring Festival holiday (its Monday classes "
             "met on Fri 13 Feb); classes resume Tue 24 Feb and the session "
             "ends Thu 26 Feb."),
        ],
        "finals": "2026-03-02",
    },
    {
        "name": "Spring 2026 Session 2",
        "weeks": [
            "2026-03-16", "2026-03-23", "2026-03-30", "2026-04-06",
            "2026-04-13", "2026-04-20", "2026-04-27",
        ],
        "finals": "2026-05-04",
    },
]
