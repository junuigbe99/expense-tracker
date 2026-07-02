import csv
expenses = []
def add_expense(date, time, location, store, amount):
    if len(expenses) == 0:
        id = 1
    else:
        id = int(expenses[-1]["id"]) + 1
    expense = {
        "id": id,
        "date": date,
        "time": time,
        "location": location,
        "store": store,
        "amount": amount
        }
    expenses.append(expense)

def list_expenses():
    for expense in expenses:
        print(f"ID: {expense['id']} | Date: {expense['date']} | Time: {expense['time']} | Location: {expense['location']} | Store: {expense['store']} | Amount: ${expense['amount']}")

def save_expenses():
    with open("expenses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date", "time", "location", "store", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
            pass
def delete_expense(id):
    global expenses
    expenses = [expense for expense in expenses if int(expense["id"]) != id]

def total_expenses():
    total = 0
    for expense in expenses:
        total += float(expense["amount"])
    print(f"Total: ${total:.2f}")
    
load_expenses()
list_expenses()
total_expenses()
save_expenses()