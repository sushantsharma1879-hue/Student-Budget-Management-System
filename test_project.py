
from database import initialize_database
from expense import add_expense, get_expenses
from budget import set_budget, get_budget_status

print("========== PROJECT TESTING ==========")

initialize_database()

print("\n1. Testing Expense Module...")

success, message = add_expense(
    "2026-09-30",
    "Food",
    "Test Lunch",
    100
)

print(message)

if success:
    print("Expense Test: PASSED")
else:
    print("Expense Test: FAILED")


print("\n2. Testing Budget Module...")

success, message = set_budget(
    "Food",
    3000
)

print(message)

budgets = get_budget_status()

if budgets:
    print("Budget Test: PASSED")
else:
    print("Budget Test: FAILED")


print("\n3. Testing Database...")

expenses = get_expenses()

if expenses:
    print("Database Test: PASSED")
else:
    print("Database Test: FAILED")


print("\n========== TESTING COMPLETED ==========")
