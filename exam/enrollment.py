def gather_credits(needed_credits, *args):
    courses = []
    credit = needed_credits
    max_credits = 0
    result = []

    for course in args:
        if course[0] in courses:
            continue

        max_credits += course[1]
        courses.append(course[0])

        if max_credits >= needed_credits:
            break

    if max_credits >= needed_credits:
        result.append(f"Enrollment finished! Maximum credits: {max_credits}.")
        result.append(f"Courses: {', '.join(sorted(courses, key=lambda x: x[0]))}")
    elif max_credits < needed_credits:
        result.append(f"You need to enroll in more courses! You have to gather {abs(needed_credits - max_credits)} credits more.")

    return "\n".join(result)


print(gather_credits(
    80,
    ("Basics", 40),
    ("Basics", 80),
))


print(gather_credits(
    80,
    ("Basics", 80),
    ("Advanced", 30),
    ("Fundamentals", 27),
))



print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))