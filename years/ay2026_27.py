"""DKU Academic Calendar AY2026-2027.

Source: registrar's Academic Calendar page, "2026-2027 Academic Calendar" tab,
retrieved 2026-07-22. (That tab's heading reads "Academic Year 2025-2026" - a
typo on the registrar's side; the content is genuinely AY2026-27.)

The Summer 2026 entries are printed on that page and are included here.
"""

AY = "2026-27"
SOURCE_URL = "https://registrar.dukekunshan.edu.cn/academic-calendar/"

EVENTS = [
    # ---------------- Summer 2026 (listed on the AY2026-27 page) -----------
    ("2026-07-06", None, "Summer session starts",
     "Monday. Summer session starts (for class of 2029 mainland and HMT "
     "students only)."),
    ("2026-08-13", None, "Summer session exams",
     "Thursday. Summer session exams."),

    # ---------------- Fall 2026 -------------------------------------------
    ("2026-08-14 09:00", None, "Move-in: new international UG + int'l 1st-year grad",
     "Friday at 9:00 AM. All new international undergraduate students "
     "(Class of 2030) and international first-year graduate students move-in."),
    ("2026-08-16 09:00", None, "Move-in: new Chinese UG + Chinese 1st-year grad",
     "Sunday at 9:00 AM. All new Chinese undergraduate students (Class of "
     "2030) and Chinese first-year graduate students move-in."),
    ("2026-08-21 09:00", None, "Move-in: returning UG + grad students",
     "Friday at 9:00 AM. Returning undergraduate and graduate students move-in."),
    ("2026-08-24", None, "Fall 2026 classes begin (UG + grad)",
     "Monday. Undergraduate and graduate classes begin."),
    ("2026-08-27", None, "Drop/add ends - 1st 7-week UG session",
     "Thursday. Drop/add ends for first 7-week undergraduate session."),
    ("2026-09-03", None, "Drop/add ends - 14-week UG session",
     "Thursday. Drop/add ends for 14-week undergraduate session."),
    ("2026-09-04", None, "Drop/add ends - graduate classes",
     "Friday. Drop/add ends for graduate classes."),
    ("2026-09-18", None, "Thursday class schedule in effect",
     "Friday. Classes continue. The Thursday class meeting schedule is in "
     "effect on this day."),
    ("2026-09-24", None, "Deadlines - 1st 7-week W / grading basis / I grades",
     "Thursday. Last day to withdraw with a W grade of first 7-week classes; "
     "Last day to change grading basis of first 7-week classes; Last day to "
     "resolve I grade of second seven-week classes in spring 2026."),
    ("2026-09-25", "2026-09-27", "Mid-Autumn Festival - No classes",
     "Friday - Sunday. Mid-Autumn Festival - No classes."),
    ("2026-10-01", "2026-10-11", "National Day Holiday - No classes",
     "Thursday - Sunday. National Day Holiday - No classes."),
    ("2026-10-12", None, "All classes resume",
     "Monday. All classes resume."),
    ("2026-10-15", None, "1st 7-week UG session ends",
     "Thursday. First 7-week undergraduate session end."),
    ("2026-10-16", "2026-10-18", "UG reading period",
     "Friday-Sunday. Undergraduate reading period."),
    ("2026-10-19", "2026-10-22", "1st 7-week UG final examinations",
     "Monday-Thursday. First 7-week undergraduate session final examinations. "
     "Graduate classes continue."),
    ("2026-10-26", None, "2nd 7-week UG session begins",
     "Monday. Second 7-week undergraduate session begins."),
    ("2026-10-29", None, "Drop/add ends - 2nd 7-week UG session",
     "Thursday. Drop/add ends for second 7-week undergraduate session."),
    ("2026-11-12", None, "Deadlines - 14-week W / grading basis",
     "Thursday. Last day to withdraw with a W grade of 14-week classes. Last "
     "day to change grading basis of 14-week classes."),
    ("2026-11-26", None, "Graduate classes end; 2nd 7-week W / grading / I deadlines",
     "Thursday. Graduate classes end (ECE classes continue); Last day to "
     "withdraw with a W grade of second 7-week classes; Last day to change "
     "grading basis of second 7-week classes; Last day to resolve I grade of "
     "first 7-week classes."),
    ("2026-11-27", "2026-12-01", "Graduate reading days",
     "Friday-Tuesday. Graduate reading days; ECE classes continue."),
    ("2026-12-02", "2026-12-04", "Graduate exams",
     "Wednesday-Friday. Graduate exams."),
    ("2026-12-03", None, "ECE classes end",
     "Thursday. ECE classes end."),
    ("2026-12-04", "2026-12-08", "ECE program reading days",
     "Friday-Tuesday. ECE program reading days."),
    ("2026-12-09", "2026-12-11", "ECE program exam period",
     "Wednesday-Friday. ECE program exam period."),
    ("2026-12-10", None, "2nd 7-week UG session ends",
     "Thursday. Second 7-week undergraduate session ends."),
    ("2026-12-11", "2026-12-13", "UG reading period",
     "Friday-Sunday. Undergraduate reading period."),
    ("2026-12-14", "2026-12-17", "UG final examinations",
     "Monday-Thursday. Undergraduate final examinations."),
    ("2026-12-18 13:00", None, "Residence halls close for Winter Break",
     "Friday at 13:00. All residence halls close for Winter Break."),
    ("2026-12-18", "2026-12-24", "(Tentative) Extended requirement - Class of 2030",
     "Friday-Thursday (tentative). Extended requirement for Class of 2030 "
     "starts (required for mainland Chinese students and optional for HMT "
     "students)."),

    # ---------------- Spring 2027 -----------------------------------------
    ("2027-01-09 09:00", None, "Residence halls reopen",
     "Saturday at 9:00 AM. All residence halls reopen."),
    ("2027-01-11", None, "Spring 2027 classes begin (UG + grad)",
     "Monday. Undergraduate and graduate classes begin."),
    ("2027-01-14", None, "Drop/add ends - 1st 7-week UG session",
     "Thursday. Drop/add ends for first 7-week undergraduate session."),
    ("2027-01-21", None, "Drop/add ends - 14-week UG session",
     "Thursday. Drop/add ends for 14-week undergraduate session."),
    ("2027-01-22", None, "Drop/add ends - graduate classes",
     "Friday. Drop/add ends for graduate classes."),
    ("2027-02-05", "2027-02-14", "Spring Festival (Chinese New Year) - No classes",
     "Friday-Sunday. Spring Festival Holiday - Chinese New Year - No classes."),
    ("2027-02-15", None, "All classes resume",
     "Monday. All classes resume."),
    ("2027-02-18", None, "Deadlines - 1st 7-week W / grading basis / I grades",
     "Thursday. Last day to withdraw with a W grade of first 7-week classes; "
     "Last day to change grading basis of first 7-week classes; Last day to "
     "resolve I grade of fall 2026 second 7-week classes."),
    ("2027-03-04", None, "1st 7-week UG session ends",
     "Thursday. First 7-week undergraduate session ends."),
    ("2027-03-05", "2027-03-07", "UG reading days",
     "Friday-Sunday. Undergraduate Reading Days."),
    ("2027-03-08", "2027-03-11", "1st 7-week UG final examinations",
     "Monday-Thursday. First 7-week undergraduate session final examinations. "
     "Graduate classes continue."),
    ("2027-03-15", "2027-03-19", "Mini-term week (UG) / Spring recess (grad)",
     "Monday-Friday. Mini-term week for undergraduate students; Spring recess "
     "for graduate programs."),
    ("2027-03-22", None, "2nd 7-week UG session begins",
     "Monday. Second 7-week undergraduate session begins."),
    ("2027-03-25", None, "Drop/add ends - 2nd 7-week UG session",
     "Thursday. Drop/add ends for second 7-week undergraduate session."),
    ("2027-04-05", None, "Qing Ming (Tomb Sweeping Day) - No classes",
     "Monday. Qing Ming - Tomb Sweeping Day - No classes."),
    ("2027-04-06", None, "Monday class schedule in effect",
     "Tuesday. The Monday class schedule is in effect on this day."),
    ("2027-04-07", None, "Tuesday class schedule in effect",
     "Wednesday. The Tuesday class schedule is in effect on this day."),
    ("2027-04-08", None, "Wednesday class schedule in effect",
     "Thursday. The Wednesday class schedule is in effect on this day."),
    ("2027-04-09", None, "Thursday class schedule in effect; 14-week W / grading deadline",
     "Friday. The Thursday class schedule is in effect on this day. Last day "
     "to withdraw with a W grade of 14-week classes. Last day to change "
     "grading basis of 14-week classes."),
    ("2027-04-22", None, "Graduate classes end; 2nd 7-week W / grading / I deadlines",
     "Thursday. Graduate classes end (ECE classes continue); Last day to "
     "withdraw with a W grade of second 7-week classes; Last day to change "
     "grading basis for second 7-week classes; Last day for I grade change of "
     "spring 2027 first 7-week classes."),
    ("2027-04-23", "2027-04-27", "Graduate reading days",
     "Friday-Tuesday. Graduate Reading Days."),
    ("2027-04-28", "2027-04-30", "Graduate exams",
     "Wednesday-Friday. Graduate exams; ECE classes continue."),
    ("2027-04-29", None, "ECE classes end",
     "Thursday. ECE Classes end."),
    ("2027-04-30", "2027-05-04", "ECE program reading days",
     "Friday-Tuesday. ECE program reading days."),
    ("2027-05-01", "2027-05-03", "International Labor Day Holiday - No classes",
     "Saturday-Monday. International Labor Day Holiday - No classes."),
    ("2027-05-04", None, "Monday class schedule in effect",
     "Tuesday. The Monday class schedule is in effect on this day."),
    ("2027-05-05", None, "Tuesday class schedule in effect",
     "Wednesday. The Tuesday class schedule is in effect on this day."),
    ("2027-05-05", "2027-05-07", "ECE program exam period",
     "Wednesday-Friday. ECE program exam period."),
    ("2027-05-06", None, "Wednesday class schedule in effect",
     "Thursday. The Wednesday class schedule is in effect on this day."),
    ("2027-05-07", None, "Thursday class schedule in effect; 2nd 7-week UG session ends",
     "Friday. The Thursday class schedule is in effect on this day. Second "
     "7-week undergraduate session ends."),
    ("2027-05-08", "2027-05-09", "UG reading days",
     "Saturday-Sunday. Undergraduate Reading Days."),
    ("2027-05-10", "2027-05-13", "UG final exam period",
     "Monday-Thursday. Undergraduate final exam period."),
    ("2027-05-17", "2027-05-20", "(Tentative) Extended Training (theory) - Class of 2030",
     "Monday-Thursday (tentative). Extended Training (theory) for Class of "
     "2030 (required for mainland Chinese students and optional for HMT "
     "students)."),
    ("2027-05-21", None, "Commencement (Graduate + Undergraduate)",
     "Friday. Graduate and Undergraduate Commencement."),
    ("2027-05-22 13:00", None, "All residence halls close",
     "Saturday at 13:00. All residence halls close."),
]
