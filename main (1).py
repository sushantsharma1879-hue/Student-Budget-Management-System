
from database import initialize_database

from expense import (
    add_expense,
    get_expenses,
    search_expenses,
    update_expense,
    delete_expense
)

from budget import (
    set_budget,
    get_budget_status
)

from reports import show_report

from utils import (
    show_categories,
    display_expenses,
    display_budgets
)


def add_expense_menu():

    print("\n========== ADD EXPENSE ==========")

    date = input(
        "Enter date (YYYY-MM-DD): "
    )

    show_categories()

    category = input(
        "Enter category: "
    )

    description = input(
        "Enter description: "
    )

    amount = input(
        "Enter amount: "
    )

    success, message = add_expense(
        date,
        category,
        description,
        amount
    )

    print("\n" + message)


def view_expenses_menu():

    print("\n========== ALL EXPENSES ==========")

    expenses = get_expenses()

    display_expenses(expenses)


def search_expenses_menu():

    print("\n========== SEARCH EXPENSE ==========")

    keyword = input(
        "Enter category or description: "
    )

    expenses = search_expenses(keyword)

    display_expenses(expenses)


def update_expense_menu():

    print("\n========== UPDATE EXPENSE ==========")

    expenses = get_expenses()

    display_expenses(expenses)

    try:
        expense_id = int(
            input("Enter expense ID: ")
        )
    except ValueError:
        print("Invalid ID.")
        return

    date = input(
        "Enter new date (YYYY-MM-DD): "
    )

    show_categories()

    category = input(
        "Enter new category: "
    )

    description = input(
        "Enter new description: "
    )

    amount = input(
        "Enter new amount: "
    )

    success, message = update_expense(
        expense_id,
        date,
        category,
        description,
        amount
    )

    print("\n" + message)


def delete_expense_menu():

    print("\n========== DELETE EXPENSE ==========")

    expenses = get_expenses()

    display_expenses(expenses)

    try:
        expense_id = int(
            input("Enter expense ID: ")
        )
    except ValueError:
        print("Invalid ID.")
        return

    success, message = delete_expense(
        expense_id
    )

    print("\n" + message)


def budget_menu():

    print("\n========== SET BUDGET ==========")

    show_categories()

    category = input(
        "Enter category: "
    )

    amount = input(
        "Enter budget amount: "
    )

    success, message = set_budget(
        category,
        amount
    )

    print("\n" + message)


def budget_status_menu():

    print("\n========== BUDGET STATUS ==========")

    budgets = get_budget_status()

    display_budgets(budgets)


def main():

    initialize_database()

    while True:

        print("""
==========================================
   STUDENT BUDGET MANAGEMENT SYSTEM
==========================================

1. Add Expense
2. View All Expenses
3. Search Expenses
4. Update Expense
5. Delete Expense
6. Set / Update Budget
7. View Budget Status
8. Generate Expense Report
9. Exit

==========================================
""")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            add_expense_menu()

        elif choice == "2":

            view_expenses_menu()

        elif choice == "3":

            search_expenses_menu()

        elif choice == "4":

            update_expense_menu()

        elif choice == "5":

            delete_expense_menu()

        elif choice == "6":

            budget_menu()

        elif choice == "7":

            budget_status_menu()

        elif choice == "8":

            show_report()

        elif choice == "9":

            print(
                "\nThank you for using "
                "Student Budget Management System!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-9."
            )


if __name__ == "__main__":
    main()
