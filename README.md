# Google Pay Expense Sharing System

## Overview

This project is a Google Pay-inspired Expense Sharing System developed using Python and Data Science libraries. It helps users split expenses fairly, calculate balances, and determine final settlements among group members.



## Features

* Equal expense splitting
* Balance calculation
* Final settlement suggestions
* Expense analytics
* Statistical analysis
* Data visualization using graphs
* CSV dataset generation
* Handling uneven contributions
* Handling missing payments



## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook



## Project Structure
google-pay-expense-sharing-system
│
├── expense_sharing.py
├── analytics.py
├── expenses.csv
├── analytics_report.csv
├── expense_sharing.ipynb
└── analytics.ipynb

## Dataset

The dataset contains:

| Column       | Description                    |
| ------------ | ------------------------------ |
| Payer        | Person who paid                |
| Amount       | Amount paid                    |
| Participants | People involved in the expense |

Example:

| Payer | Amount | Participants    |
| ----- | ------ | --------------- |
| Alice | 900    | Alice,Bob,David |
| Bob   | 300    | Alice,Bob,David |
| David | 200    | Alice,David     |


## Data Preprocessing

* Created a DataFrame using Pandas.
* Checked for missing values.
* Calculated summary statistics.
* Generated contribution percentages.
* Ranked spenders.



## Expense Splitting Methodology

The project uses **equal contribution** among participants.

### Example

Suppose:

* Alice pays Rs.900
* Bob pays Rs.300
* David pays Rs.200

Final settlement:
David pays Alice Rs.300
Bob pays Alice Rs.100


## Analytics Performed

* Total Expense
* Average Expense
* Highest Spender
* Lowest Spender
* Number of Transactions
* Contribution Percentage
* Ranking of Spenders
* Standard Deviation
* Median Expense
* Maximum Expense
* Minimum Expense



## Visualizations

The following graphs are generated using Matplotlib:

* Bar Chart
* Pie Chart
* Line Graph
* Histogram
* Box Plot



## Edge Cases Handled

### Uneven Contributions

Users may contribute different amounts, and balances are calculated fairly.

### Missing Payments

Users who have not paid are assigned negative balances and appropriate settlements are suggested.

### Partial Participation

Expenses involving only selected participants are supported.

## Sample Output

Balances:

Alice : 400
Bob : -100
David : -300

Final Settlement:

David pays Alice Rs.300
Bob pays Alice Rs.100


## Future Enhancements

* Weighted expense splitting
* User authentication
* GUI application
* Database integration
* Machine Learning-based spending prediction

