
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Read Dataset
# ---------------------------------

df = pd.read_csv("expenses.csv")

print("Expense Dataset:\n")
print(df)

# ---------------------------------
# Dataset Information
# ---------------------------------

print("\nDataset Information:")
print(df.info())

# ---------------------------------
# Statistical Summary
# ---------------------------------

print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------
# Missing Values
# ---------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------
# Total Expense
# ---------------------------------

total_expense = df["Amount"].sum()

print("\nTotal Expense:", total_expense)

# ---------------------------------
# Average Expense
# ---------------------------------

average_expense = df["Amount"].mean()

print("\nAverage Expense:", average_expense)

# ---------------------------------
# Highest Spender
# ---------------------------------

highest_spender = df.loc[df["Amount"].idxmax()]

print("\nHighest Spender:")
print("Name:", highest_spender["Payer"])
print("Amount:", highest_spender["Amount"])

# ---------------------------------
# Lowest Spender
# ---------------------------------

lowest_spender = df.loc[df["Amount"].idxmin()

]

print("\nLowest Spender:")
print("Name:", lowest_spender["Payer"])
print("Amount:", lowest_spender["Amount"])

# ---------------------------------
# Number of Transactions
# ---------------------------------

print("\nNumber of Transactions:", len(df))

# ---------------------------------
# Person-wise Expense
# ---------------------------------

person_wise_expense = df.groupby("Payer")["Amount"].sum()

print("\nAmount Spent by Each Person:")
print(person_wise_expense)

# ---------------------------------
# Contribution Percentage
# ---------------------------------

contribution_percentage = (
    person_wise_expense / total_expense
) * 100

print("\nContribution Percentage:")
print(contribution_percentage)

# ---------------------------------
# Ranking of Spenders
# ---------------------------------

ranking = person_wise_expense.sort_values(
    ascending=False
)

print("\nRanking of Spenders:")
print(ranking)

# ---------------------------------
# Most Frequent Payer
# ---------------------------------

payer_count = df["Payer"].value_counts()

print("\nMost Frequent Payer:")
print(payer_count)

# ---------------------------------
# Standard Deviation
# ---------------------------------

print(
    "\nStandard Deviation:",
    df["Amount"].std()
)

# ---------------------------------
# Median Expense
# ---------------------------------

print(
    "\nMedian Expense:",
    df["Amount"].median()
)

# ---------------------------------
# Maximum Expense
# ---------------------------------

print(
    "\nMaximum Expense:",
    df["Amount"].max()
)

# ---------------------------------
# Minimum Expense
# ---------------------------------

print(
    "\nMinimum Expense:",
    df["Amount"].min()
)

# ---------------------------------
# Export Analytics Report
# ---------------------------------

report = {
    "Total Expense": [total_expense],
    "Average Expense": [average_expense],
    "Highest Spender": [highest_spender["Payer"]],
    "Lowest Spender": [lowest_spender["Payer"]],
    "Transactions": [len(df)]
}

report_df = pd.DataFrame(report)

report_df.to_csv(
    "analytics_report.csv",
    index=False
)

# ---------------------------------
# Bar Chart
# ---------------------------------

plt.figure(figsize=(7, 5))

person_wise_expense.plot(
    kind='bar'
)

plt.title("Expense by Each Person")
plt.xlabel("Person")
plt.ylabel("Amount")

plt.show()

# ---------------------------------
# Pie Chart
# ---------------------------------

plt.figure(figsize=(6, 6))

person_wise_expense.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.ylabel("")
plt.title("Expense Distribution")

plt.show()

# ---------------------------------
# Line Graph
# ---------------------------------

plt.figure(figsize=(7, 5))

person_wise_expense.plot(
    kind='line',
    marker='o'
)

plt.title("Expense Trend")
plt.xlabel("Person")
plt.ylabel("Amount")

plt.show()

# ---------------------------------
# Histogram
# ---------------------------------

plt.figure(figsize=(7, 5))

df["Amount"].plot(
    kind='hist',
    bins=5
)

plt.title("Distribution of Expenses")
plt.xlabel("Amount")

plt.show()

# ---------------------------------
# Box Plot
# ---------------------------------

plt.figure(figsize=(5, 5))

plt.boxplot(
    df["Amount"]
)

plt.title("Box Plot of Expenses")

plt.show()

