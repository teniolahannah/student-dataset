
import csv

students = [
    ["Student ID", "Department", "Level", "Attendance Percentage", "Average Examination Score"],
    ["CUL001", "Computer Science", 200, 85, 78],
    ["CUL002", "Cyber Security", 200, 90, 82],
    ["CUL003", "Software Engineering", 100, 75, 69],
    ["CUL004", "Computer Science", 300, 95, 88],
    ["CUL005", "Information Technology", 200, 80, 74],
    ["CUL006", "Cyber Security", 100, 70, 65],
    ["CUL007", "Computer Science", 400, 92, 90],
    ["CUL008", "Software Engineering", 300, 88, 81],
    ["CUL009", "Information Technology", 100, 78, 72],
    ["CUL010", "Computer Science", 200, 96, 85]
]

with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student dataset created successfully!")
print("Total students:", len(students) - 1)
