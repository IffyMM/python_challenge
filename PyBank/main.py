# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
budget_csv= os.path.join("Resources", "budget_data.csv")  # Input file path
analysis_txt = os.path.join("Analysis", "bank.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total=0
month_change=[]
greatest_increase_profits=["", 0]
greatest_decrease_profits=["", 99999999999999999]
net_change_list=[]
# Open and read the csv
with open(budget_csv) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row=next(reader)

    # Track the total and net change
    total_months=total_months+1
    total_net=total_net+int(first_row[1])
    previous_net=int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months+=1
        total_net=total_net+int(row[1])

        # Track the net change
        net_change=int(row[1])-previous_net
        net_change_list.append(net_change)
        previous_net=int(row[1])
        month_change.append(row[0])

        # Calculate the greatest increase in profits (month and amount)
        #greatest_increase_profits=max(total_net)
        if net_change>greatest_increase_profits[1]:
            greatest_increase_profits[0]=row[0]
            greatest_increase_profits[1]=net_change
        # Calculate the greatest decrease in losses (month and amount)
        #greatest_decrease_profits=min(total_net)
        if net_change<greatest_decrease_profits[1]:
            greatest_decrease_profits[0]=row[0]
            greatest_decrease_profits[1]=net_change

# Calculate the average net change across the months
average_change=sum(net_change_list) / len(net_change_list)

# Generate the output summary
output= (
f"\nFinancial Analysis\n"
f"..................\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: {average_change: .2f}\n"
f"Greatest Increase in Profits: {(greatest_increase_profits[0])} (${(greatest_increase_profits[1])})\n"
f"Greatest Decrease in Profits: {(greatest_decrease_profits[0])} (${(greatest_decrease_profits[1])})\n"
)
#print output

print(output)

with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)