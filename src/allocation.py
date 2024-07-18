import matplotlib.pyplot as plt
import numpy as np
import locale

# Set locale to 'id_ID' for Indonesian formatting
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')


def allocate_funds(monthly_income):
    # Define the percentage allocations
    expense_percent = 0.23  # Adjusted for expenses
    personal_investment_percent = 0.07
    investment_percent = 0.60
    emergency_savings_percent = 0.10

    # Calculate actual amounts
    expenses = monthly_income * expense_percent
    personal_investment = monthly_income * personal_investment_percent
    investments = monthly_income * investment_percent
    emergency_savings = monthly_income * emergency_savings_percent

    # Sub-categorize investments
    crypto = investments * 0.80
    stocks = investments * 0.20

    # Further sub-categorize crypto
    btc = crypto * 0.70
    alt_future = crypto * 0.30

    # Data for plotting
    labels = ['Living Expenses', 'Personal Investment',
              'Emergency Savings', 'Bitcoin', 'Altcoins/Futures', 'Stocks']
    sizes = [expenses, personal_investment,
             emergency_savings, btc, alt_future, stocks]
    colors = ['#ff9999', '#ffcc99', '#66b3ff', '#99ff99', '#ffb3e6', '#c2c2f0']
    explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # "explode" the slices

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Pie chart
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    ax1.set_title('Monthly Income Allocation')
    ax1.text(
        0, -1.5, "Invest in your growth, diversify your investments.", ha='center')

    # Table
    amounts = [locale.currency(amount, grouping=True, symbol=True)
               for amount in sizes]
    percentages = [f"{size/sum(sizes)*100:.1f}%" for size in sizes]
    cell_text = [[label, amount, percent]
                 for label, amount, percent in zip(labels, amounts, percentages)]
    cell_text.append(["Total", locale.currency(
        sum(sizes), grouping=True, symbol=True), "100%"])
    ax2.axis('off')
    table = ax2.table(cellText=cell_text, colLabels=[
                      'Category', 'Amount', 'Percentage'], cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)

    plt.tight_layout()
    plt.show()


# Example usage
monthly_income = float(input("Enter your monthly income in IDR: "))
allocate_funds(monthly_income)
