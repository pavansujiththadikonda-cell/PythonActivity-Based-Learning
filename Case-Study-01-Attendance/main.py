
# Attendance Recovery Computation

print("===================================")
print("     ATTENDANCE RECOVERY SYSTEM")
print("===================================")

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes or required_percentage <= 0 or required_percentage > 100:
    print("Invalid input! Please enter valid values.")

else:
    current_percentage = (attended_classes / total_classes) * 100

    print("\nCurrent Attendance:", round(current_percentage, 2), "%")

    if current_percentage >= required_percentage:
        print("Status: Eligible")
        print("You have already reached the required attendance.")

    else:
        print("Status: Not Eligible")

        additional_classes = 0

        while ((attended_classes + additional_classes) /
               (total_classes + additional_classes)) * 100 < required_percentage:
            additional_classes += 1

        print("Minimum consecutive classes to attend:",
              additional_classes)

        print("Total classes after recovery:",
              total_classes + additional_classes)

print("\nThank you!")
