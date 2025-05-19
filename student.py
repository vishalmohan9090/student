import csv
import os

FILENAME = "expenses.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Books, Travel): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if len(expenses) <= 1:
            print("No expenses recorded yet.")
            return
        print(f"{'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
        print("-" * 55)
        for row in expenses[1:]:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<20} {row[3]:>8}")

def summarize_expenses():
    summary = {}
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            category = row[1]
            amount = float(row[3])
            summary[category] = summary.get(category, 0) + amount
            total += amount
    print("Expense Summary by Category:")
    for cat, amt in summary.items():
        print(f"{cat:<12}: {amt:.2f}")
    print(f"Total Spent : {total:.2f}")

def main():
    initialize_csv()
    while True:
        print("\nStudent Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
