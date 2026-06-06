import csv

income = 0
expenses = 0

with open("transactions.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = float(row["Amount"])

        if amount > 0:
            income += amount
        else:
            expenses += abs(amount)

print("Income:", income)
print("Expenses:", expenses)
print("Net:", income - expenses)
