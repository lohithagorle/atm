# ATM Management System

balance = 10000  # Initial balance
pin = "1234"

print("===== WELCOME TO ATM =====")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance}")
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN! Access Denied.")
