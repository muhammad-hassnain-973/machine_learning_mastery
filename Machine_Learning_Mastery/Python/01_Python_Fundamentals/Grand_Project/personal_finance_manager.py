import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

transactions = []


def load_transactions():
    """Load transactions from the JSON file into the global list."""
    global transactions
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                transactions = json.load(f)
        except (json.JSONDecodeError, IOError):
            transactions = []
    else:
        transactions = []


def save_transactions():
    """Save the global transactions list to the JSON file in the script folder."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(transactions, f, indent=2)
    except IOError:
        print("Error: Could not write to data file.")


def add_transaction():
    tran_id = input("Enter transaction id: ")
    tran_type = input("Enter type (income/expense): ").strip().lower()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Transaction cancelled.")
        return
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date in DDMMYYYY: ")

    transactions.append({
        "id": tran_id,
        "type": tran_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    })

    if tran_type == "expense":
        try:
            budget_limit = float(input("Enter your budget limit: "))
        except ValueError:
            budget_limit = None
        if budget_limit is not None:
            total_expense = sum(float(t["amount"]) for t in transactions if t.get("type") == "expense")
            if total_expense > budget_limit:
                print(f"Warning: You have exceeded your budget limit of ${budget_limit:.2f}")

    save_transactions()


def view_transactions():
    load_transactions()
    if not transactions:
        print("No transactions found. Please add a transaction first.")
        return
    for t in transactions:
        print(t)


def get_balance():
    load_transactions()
    total_income = sum(float(t.get("amount", 0)) for t in transactions if t.get("type") == "income")
    total_expense = sum(float(t.get("amount", 0)) for t in transactions if t.get("type") == "expense")
    balance = total_income - total_expense
    print(f"Your current balance is: ${balance:.2f}")


def monthly_summary():
    load_transactions()
    month = input("Enter month in MM format: ")
    year = input("Enter year in YYYY format: ")
    income = 0.0
    expense = 0.0
    for t in transactions:
        d = t.get("date", "")
        if len(d) >= 8 and d[2:4] == month and d[4:8] == year:
            if t.get("type") == "income":
                income += float(t.get("amount", 0))
            elif t.get("type") == "expense":
                expense += float(t.get("amount", 0))
    print(f"Monthly Summary for {month}/{year}:")
    print(f"Income: ${income:.2f}")
    print(f"Expense: ${expense:.2f}")


def search_transactions():
    load_transactions()
    search_id = input("Enter transaction id to search: ")
    for t in transactions:
        if t.get("id") == search_id:
            print(t)
            return
    print("Transaction not found.")


def delete_transaction():
    load_transactions()
    delete_id = input("Enter transaction id to delete: ")
    for t in list(transactions):
        if t.get("id") == delete_id:
            transactions.remove(t)
            save_transactions()
            print("Transaction deleted successfully.")
            return
    print("Transaction not found.")


def exit_program():
    save_transactions()
    print("Exiting the Personal Finance Manager and data saved. Goodbye!")
    sys.exit(1)


def show_menu():
    print("Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Get Balance")
    print("4. Monthly Summary")
    print("5. Search Transactions")
    print("6. Delete Transaction")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        get_balance()
    elif choice == "4":
        monthly_summary()
    elif choice == "5":
        search_transactions()
    elif choice == "6":
        delete_transaction()
    elif choice == "7":
        exit_program()
    else:
        print("Invalid choice. Please try again.")


def main():
    load_transactions()
    while True:
        print("Personal Finance Manager")
        print("Welcome to the Personal Finance Manager!")
        print("Press 1 to show menu")
        print("Press 2 to Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_menu()
        elif choice == "2":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()