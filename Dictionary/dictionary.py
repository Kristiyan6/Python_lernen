student_scores = {
     "Harry": 81,
     "Ron": 78,
     "Hermine": 99,
     "Draco": 74,
     "Neville": 62,
     "Kristiyan": 100
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        student_grades[name] = "Outstanding"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"



#student_grades = {
#     "Harry": "Exceeds Expectations",
#     "Ron": "Acceptable",
#     "Hermine": "Outstanding",
#     "Draco": "Acceptable",
#     "Neville": "Fail"
#}

#print(student_grades)

for key in student_scores:
    print(f"{key}: {student_grades[key]}")
