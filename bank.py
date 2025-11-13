# Step 1: Create accounts
accounts = []

n = int(input("How many bank accounts do you want to create? "))

for i in range(n):
    print(f"\n--- Account #{i+1} ---")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    accounts.append({"name": name, "balance": balance})

# Step 2: Main menu loop
while True:
    print("\n===== BANK MENU =====")
    print("1. Show all account balances")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Show accounts with above-average balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1️ Show all accounts
    if choice == "1":
        print("\n Account list:")
        for acc in accounts:
            print(f" {acc['name']} →  {acc['balance']}")

    # 2️ Deposit
    elif choice == "2":
        name = input("Enter account name for deposit: ")
        amount = float(input("Enter deposit amount: "))
        found = False
        for acc in accounts:
            if acc["name"] == name:
                acc["balance"] += amount
                print(f"{amount} added to {name}'s account.")
                found = True
                break
        if not found:
            print(" Account not found!")

    # 3️ Withdraw
    elif choice == "3":
        name = input("Enter account name for withdrawal: ")
        amount = float(input("Enter withdrawal amount: "))
        found = False
        for acc in accounts:
            if acc["name"] == name:
                if acc["balance"] >= amount:
                    acc["balance"] -= amount
                    print(f" {amount} withdrawn from {name}'s account.")
                else:
                    print(" Insufficient balance!")
                found = True
                break
        if not found:
            print("Account not found!")

    # 4️ Above average accounts
    elif choice == "4":
        if not accounts:
            print(" No accounts available!")
        else:
            avg = sum(acc["balance"] for acc in accounts) / len(accounts)
            print(f"\n Average balance: {avg}")
            print(" Accounts with above-average balance:")
            for acc in accounts:
                if acc["balance"] > avg:
                    print(f" {acc['name']} →  {acc['balance']}")

    # 5️ Exit
    elif choice == "5":
        print(" Goodbye! Thank you for using our banking system.")
        break

    # Invalid option
    else:
        print("Invalid choice. Please try again.")
