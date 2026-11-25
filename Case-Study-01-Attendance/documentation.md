
# Case Study 01: Attendance Recovery Computation

## 1. Problem Statement
Develop a Python program to calculate a student's current attendance percentage and determine the minimum number of consecutive classes required to achieve the minimum attendance eligibility percentage.

## 2. Objectives
- Calculate current attendance percentage.
- Check whether the student is eligible.
- Calculate the minimum additional classes required.
- Validate user inputs.

## 3. Assumptions
- Total classes conducted must be greater than zero.
- Attended classes cannot exceed total classes.
- Required attendance must be between 1 and 100.
- The student attends every additional class.

## 4. Algorithm
1. Start.
2. Read total classes conducted.
3. Read classes attended.
4. Read required attendance percentage.
5. Validate the inputs.
6. Calculate current attendance percentage.
7. Check whether the student meets the required percentage.
8. If eligible, display the eligibility status.
9. Otherwise, use a loop to calculate the minimum additional classes required.
10. Display the result.
11. Stop.

## 5. Pseudocode

START
INPUT total_classes
INPUT attended_classes
INPUT required_percentage

IF inputs are invalid THEN
    DISPLAY "Invalid input"
ELSE
    current_percentage = (attended_classes / total_classes) * 100
    DISPLAY current_percentage

    IF current_percentage >= required_percentage THEN
        DISPLAY "Eligible"
    ELSE
        additional_classes = 0

        WHILE attendance percentage < required percentage
            additional_classes = additional_classes + 1
        END WHILE

        DISPLAY additional_classes
    END IF
END IF

STOP

## 6. Python Source Code
Refer to main.py in this folder.

## 7. Test Cases

| Test | Total | Attended | Required | Expected Result |
|---|---:|---:|---:|---|
| 1 | 100 | 65 | 75 | 40 additional classes |
| 2 | 100 | 80 | 75 | Eligible |
| 3 | 50 | 25 | 75 | 100 additional classes |
| 4 | 0 | 0 | 75 | Invalid input |

## 8. Output
For Test Case 1:

Current Attendance: 65.0%
Status: Not Eligible
Minimum consecutive classes to attend: 40
Total classes after recovery: 140

## 9. Concepts Used
- Variables
- Data types
- Arithmetic operators
- Conditional statements
- While loop
- Input and output functions

## 10. Conclusion
The Attendance Recovery Computation program successfully calculates attendance percentage and determines the minimum number of consecutive classes required to achieve the specified attendance eligibility.
