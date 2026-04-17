import csv
import os
from datetime import datetime

DATA_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Travel', 'Bills', 'Shopping', 'Other']

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])

def add_expense():
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    print("Categories:", ", ".join(CATEGORIES))
    category = input("Enter category: ").capitalize()
    if category not in CATEGORIES:
        category = 'Other'
    
    description = input("Enter brief description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, description])
    
    print("Expense saved successfully!")

def show_total():
    print("\n--- Spending Summary ---")
    total = 0.0
    category_totals = {cat: 0.0 for cat in CATEGORIES}

    if not os.path.exists(DATA_FILE):
        print("No expenses recorded yet.")
        return

    with open(DATA_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = float(row['Amount'])
            total += amt
            cat = row['Category']
            if cat in category_totals:
                category_totals[cat] += amt

    print(f"\nGrand Total: ₹{total:.2f}")
    print("\nBreakdown by Category:")
    for cat, amt in category_totals.items():
        if amt > 0:
            print(f" - {cat}: ₹{amt:.2f}")

def view_all_expenses():
    print("\n--- All Expenses ---")
    if not os.path.exists(DATA_FILE):
        print("No data found.")
        return

    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            print(f"{row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")

def main():
    initialize_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Totals")
        print("3. View All Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_total()
        elif choice == '3':
            view_all_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()