# Case Study 09: Travel Expense Tracker

print("===== Travel Expense Tracker =====")

expenses = []
categories = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        if amount > 0:
            categories.append(category)
            expenses.append(amount)
            print("Expense added successfully!")
        else:
            print("Enter a valid expense amount.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n===== Expense List =====")
            for i in range(len(expenses)):
                print(categories[i], "-", expenses[i])

    elif choice == "3":
        total = sum(expenses)
        print("Total Expenses: Rs.", total)

    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

print("==============================")