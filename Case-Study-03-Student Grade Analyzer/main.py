# Case Study 03: Student Grade Analyzer

print("===== Student Grade Analyzer =====")

student_name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))
mark4 = float(input("Enter mark for Subject 4: "))
mark5 = float(input("Enter mark for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print("\n===== Student Report =====")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

print("===============================")