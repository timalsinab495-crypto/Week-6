import datetime

# Global variable
college_name = "Bhaktapur Multiple Campus"

start_date = "2025-05-01"

exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]


def parse_date(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date


def get_exam_date(start_str, days):
    start = parse_date(start_str)
    exam_date = start + datetime.timedelta(days=days)
    return exam_date.strftime("%Y-%m-%d")


def print_schedule(start_str, exams):
    print("College:", college_name)
    print("---- Exam Schedule ----")
    for subject, days in exams:
        date = get_exam_date(start_str, days)
        print(subject, "->", date)


print_schedule(start_date, exams)