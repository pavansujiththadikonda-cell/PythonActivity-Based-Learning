# Case Study 10: Online Quiz System

print("===== Online Quiz System =====")

questions = [
    "What is the capital of India?",
    "Which language is used for Python programming?",
    "What is 5 + 7?",
    "Which planet is known as the Red Planet?",
    "What does CPU stand for?"
]

options = [
    ["1. Mumbai", "2. New Delhi", "3. Chennai", "4. Hyderabad"],
    ["1. Python", "2. HTML", "3. CSS", "4. SQL"],
    ["1. 10", "2. 11", "3. 12", "4. 13"],
    ["1. Earth", "2. Venus", "3. Jupiter", "4. Mars"],
    ["1. Central Processing Unit", "2. Computer Personal Unit",
     "3. Central Program Utility", "4. Control Processing User"]
]

answers = ["2", "1", "3", "4", "1"]

score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1, ":", questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer (1-4): ")

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("\n===== Quiz Result =====")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Final Score:", score, "/", len(questions))

if score == 5:
    print("Grade: Excellent!")
elif score >= 3:
    print("Grade: Good!")
else:
    print("Grade: Keep Practicing!")

print("==============================")
