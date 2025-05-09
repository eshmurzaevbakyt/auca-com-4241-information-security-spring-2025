import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"

def ensure_data_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load_expenses():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category (e.g., Labs, Medication): ").strip()
    amount = float(input("Enter amount: ").strip())
    method = input("Payment method (cash/card): ").strip().lower()
    note = input("Optional note: ").strip()

    new_expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "method": method,
        "note": note
    }

    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. {item['date']} | {item['category']} | {item['amount']} | {item['method']} | {item['note']}")

def delete_expense():
    expenses = load_expenses()
    view_expenses()
    index = int(input("Enter index to delete: ").strip())
    if 1 <= index <= len(expenses):
        deleted = expenses.pop(index - 1)
        save_expenses(expenses)
        print(f"Deleted: {deleted}")
    else:
        print("Invalid index.")

def main():
    ensure_data_file()
    while True:
        print("\n--- VHI Expense Tracker ---")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def add_expense_programmatically(date, category, amount, method="manual", note=""):
    new_expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "method": method,
        "note": note
    }
    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)


if __name__ == "__main__":
    main()
