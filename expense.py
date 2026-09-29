
from database import get_connection
from validation import validate_date, validate_amount, validate_category

def add_expense(date, category, description, amount):

    category = category.strip().title()

    if not validate_date(date):
        return False, "Invalid date. Use YYYY-MM-DD."

    if not validate_category(category):
        return False, "Invalid category."

    if description.strip() == "":
        return False, "Description cannot be empty."

    if not validate_amount(amount):
        return False, "Amount must be greater than 0."

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO expenses
        (date, category, description, amount)
        VALUES (?, ?, ?, ?)
        """,
        (date, category, description.strip(), float(amount))
    )

    conn.commit()
    conn.close()

    return True, "Expense added successfully."


def get_expenses():

    conn = get_connection()

    expenses = conn.execute(
        """
        SELECT * FROM expenses
        ORDER BY date DESC, id DESC
        """
    ).fetchall()

    conn.close()

    return expenses


def search_expenses(keyword):

    conn = get_connection()

    expenses = conn.execute(
        """
        SELECT * FROM expenses
        WHERE category LIKE ?
        OR description LIKE ?
        ORDER BY date DESC
        """,
        (f"%{keyword}%", f"%{keyword}%")
    ).fetchall()

    conn.close()

    return expenses


def update_expense(
    expense_id,
    date,
    category,
    description,
    amount
):

    category = category.strip().title()

    if not validate_date(date):
        return False, "Invalid date."

    if not validate_category(category):
        return False, "Invalid category."

    if description.strip() == "":
        return False, "Description cannot be empty."

    if not validate_amount(amount):
        return False, "Amount must be greater than 0."

    conn = get_connection()

    cursor = conn.execute(
        """
        UPDATE expenses
        SET date = ?,
            category = ?,
            description = ?,
            amount = ?
        WHERE id = ?
        """,
        (
            date,
            category,
            description.strip(),
            float(amount),
            expense_id
        )
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False, "Expense ID not found."

    conn.close()

    return True, "Expense updated successfully."


def delete_expense(expense_id):

    conn = get_connection()

    cursor = conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False, "Expense ID not found."

    conn.close()

    return True, "Expense deleted successfully."
