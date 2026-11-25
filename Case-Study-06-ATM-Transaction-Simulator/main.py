# Case Study 06: ATM Transaction Simulator

print("===== ATM Transaction Simulator =====")

balance = 10000.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("Updated Balance: Rs.", balance)
        else:
            print("Enter a valid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Updated Balance: Rs.", balance)
        elif amount <= 0:
            print("Enter a valid withdrawal amount.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")

print("==============================")