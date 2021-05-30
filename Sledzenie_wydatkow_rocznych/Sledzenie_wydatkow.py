expenses = []

def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')
def add_expense(month):
    print()
    expense_amount = int(input("Podaj kwotę [zł]: "))
    expense_type = input("Podaj typ wydatku (jedzenie, rozrywka, dom itp) ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)

def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_all = total_amount_all / len(expenses)


    print()
    print("Statystki")
    print("Wszytkie wydatki w tym miesiącu [zł] ", total_amount_this_month)
    print("Średni wydatek w tym miesiącu  [zł] ", average_expense_this_month)
    print("Wszytkie wydatki [zł] ", total_amount_all)
    print("Średni wydatek  [zł] ", average_expense_all)

while True:
    print()
    month = int(input("Wybierz miesiac [1-12] "))

    if month == 0:
        break
    while True:
        print("0. Powrót do wyboru miesiąca")
        print("1. Wyświetl wszystkie wydatki")
        print("2. Dodaj wydatek")
        print("3. Statystki")
        choice = int(input("Wybierz opcję: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)
        if choice == 3:
            show_stats(month)

