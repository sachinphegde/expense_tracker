"""
Statistics module for the Expense Tracker application.
This module provides functions to generate statistics or graphs based on the expenses.
"""

import matplotlib.pyplot as plt
import sqlite3

from config import DB_LOCAL_PATH
import budget


def generate_monthly_summary(month, year):
    """
    Generate monthly summary report
    """
    cat_budget = budget.load_budget()
    # total_expense = get_expense_sum(month, year)
    cat_expense = get_expense_sum_by_category(month, year)
    plot_expense_pie_chart_by_category(cat_expense)
    plot_budget_vs_expense_bar(cat_budget, cat_expense)


def get_expense_sum(month, year):
    """
    Calculates the total sum of expenses in the database.
    """
    conn = sqlite3.connect(DB_LOCAL_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            SUM(amount)
        FROM
            expenses
        WHERE
            month = ? AND year = ?
        """, (month, year))
    total_sum = cursor.fetchone()[0]
    conn.close()
    if total_sum is not None:
        return total_sum
    else:
        return 0


def get_expense_sum_by_category(month, year):
    """
    Calculates the total sum of expenses for each category in the database.
    """
    conn = sqlite3.connect(DB_LOCAL_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        category,
        SUM(amount)
    FROM
        expenses
    WHERE
        month = ? AND year = ?
    GROUP BY
        category
    """, (month, year))
    results = cursor.fetchall()
    conn.close()
    if results:
        return results
    else:
        print("No expenses found.")


def plot_expense_pie_chart_by_category(results):
    """
    Plots a pie chart of expenses by category.
    """
    categories = [row[0] for row in results]
    totals = [row[1] for row in results]
    plt.figure(figsize=(8, 8))
    plt.pie(totals, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.axis('equal')
    plt.show()


def plot_budget_vs_expense_bar(cat_budget, cat_expense):
    """
    Plots a bar graph comparing category budgets and actual expenses.
    Args:
        cat_budget (dict): Category budgets, e.g., {'Food': 500, 'Travel': 300}
        cat_expense (list): List of tuples, e.g., [('Food', 450), ('Travel', 350)]
    """
    import matplotlib.pyplot as plt

    expense_dict = dict(cat_expense)
    categories = sorted(set(cat_budget.keys()) | set(expense_dict.keys()))
    budgets = [cat_budget.get(cat, 0) for cat in categories]
    expenses = [expense_dict.get(cat, 0) for cat in categories]

    total_budget = sum(budgets)
    total_expense = sum(expenses)
    print(f"\nTotal Budget: {total_budget:.2f}")
    print(f"Total Expense: {total_expense:.2f}\n")

    x = range(len(categories))
    plt.figure(figsize=(10, 6))
    bar1 = plt.bar(x, budgets, width=0.4, label='Budget', align='center', alpha=0.7)
    bar2 = plt.bar([i + 0.4 for i in x], expenses, width=0.4, label='Expense', align='center', alpha=0.7)
    plt.xticks([i + 0.2 for i in x], categories, rotation=45)
    plt.ylabel('Amount')
    plt.title('Category-wise Budget vs Expense')
    plt.legend()
    plt.tight_layout()

    # Annotate bars with values
    for rect in bar1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    for rect in bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=9, color='blue')

    plt.show()
