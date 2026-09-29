
from database import get_connection


def total_expenses():

    conn = get_connection()

    total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses"
    ).fetchone()[0]

    conn.close()

    return total


def category_summary():

    conn = get_connection()

    data = conn.execute(
        """
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()

    conn.close()

    return data


def monthly_summary():

    conn = get_connection()

    data = conn.execute(
        """
        SELECT
            substr(date, 1, 7) AS month,
            SUM(amount) AS total
        FROM expenses
        GROUP BY month
        ORDER BY month
        """
    ).fetchall()

    conn.close()

    return data


def show_report():

    print("\n========== EXPENSE REPORT ==========")

    print(
        f"Total Expenses: ₹{total_expenses():.2f}"
    )

    print("\nCategory-wise Spending:")

    data = category_summary()

    if not data:
        print("No expenses recorded.")

    for row in data:
        print(
            f"{row['category']}: "
            f"₹{row['total']:.2f}"
        )

    print("\nMonthly Spending:")

    data = monthly_summary()

    if not data:
        print("No monthly data available.")

    for row in data:
        print(
            f"{row['month']}: "
            f"₹{row['total']:.2f}"
        )
