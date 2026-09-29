
from validation import CATEGORIES


def show_categories():

    print("\nAvailable Categories:")

    for category in CATEGORIES:
        print("-", category)


def display_expenses(expenses):

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)

    print(
        f"{'ID':<5}"
        f"{'Date':<13}"
        f"{'Category':<16}"
        f"{'Description':<25}"
        f"{'Amount':>10}"
    )

    print("=" * 75)

    for expense in expenses:

        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<13}"
            f"{expense['category']:<16}"
            f"{expense['description'][:23]:<25}"
            f"₹{expense['amount']:>9.2f}"
        )

    print("=" * 75)


def display_budgets(budgets):

    if not budgets:
        print("\nNo budgets found.")
        return

    print("\n" + "=" * 65)

    print(
        f"{'Category':<18}"
        f"{'Budget':>12}"
        f"{'Spent':>12}"
        f"{'Remaining':>15}"
    )

    print("=" * 65)

    for budget in budgets:

        print(
            f"{budget['category']:<18}"
            f"₹{budget['limit_amount']:>10.2f}"
            f"₹{budget['spent']:>10.2f}"
            f"₹{budget['remaining']:>13.2f}"
        )

    print("=" * 65)
