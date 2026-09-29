
from database import get_connection
from validation import validate_amount, validate_category


def set_budget(category, limit_amount):

    category = category.strip().title()

    if not validate_category(category):
        return False, "Invalid category."

    if not validate_amount(limit_amount):
        return False, "Budget must be greater than 0."

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO budgets
        (category, limit_amount)
        VALUES (?, ?)
        ON CONFLICT(category)
        DO UPDATE SET limit_amount = excluded.limit_amount
        """,
        (category, float(limit_amount))
    )

    conn.commit()
    conn.close()

    return True, "Budget saved successfully."


def get_budget_status():

    conn = get_connection()

    budgets = conn.execute(
        """
        SELECT
            b.category,
            b.limit_amount,
            COALESCE(SUM(e.amount), 0) AS spent,
            b.limit_amount -
            COALESCE(SUM(e.amount), 0) AS remaining

        FROM budgets b

        LEFT JOIN expenses e
        ON b.category = e.category

        GROUP BY
            b.category,
            b.limit_amount

        ORDER BY b.category
        """
    ).fetchall()

    conn.close()

    return budgets
