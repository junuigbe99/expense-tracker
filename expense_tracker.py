expenses = []
def add_expense(date, time, location, store, amount):
    if len(expenses) == 0:
        id = 1
    else:
        id = expenses[-1]["id"] + 1
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

add_expense("01-15-2026", "12:00", "Columbus, Ohio", "Marshalls", 85.00)
add_expense("07-01-2026", "03:14", "Columbus, Ohio", "Saks Fifth Avenue", 1295.00)
list_expenses()