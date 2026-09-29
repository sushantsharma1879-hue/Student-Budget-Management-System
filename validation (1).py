
from datetime import datetime

CATEGORIES = [
    "Food",
    "Travel",
    "Education",
    "Shopping",
    "Entertainment",
    "Health",
    "Bills",
    "Other"
]

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False

def validate_category(category):
    return category.strip().title() in CATEGORIES
