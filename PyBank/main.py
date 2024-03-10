# import what we need

import csv

# create lists for incoming data
date_list = []
profit_loss_list = []
date_change_dict = {}

# .csv to variable
budget_data_path = "./PyBank/Resources/budget_data.csv"

# write .csv data to two lists
with open(budget_data_path, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(row[1])

# store headers for some reason
date_list_header = date_list.pop(0)
profit_loss_list_header = profit_loss_list.pop(0)

# change list from strings to integers
profit_loss_list_int = [int(x) for x in profit_loss_list]

# total months is the length of the list
total_months = len(date_list)

# add up total profit
total_profit = 0
for num in profit_loss_list_int:
    total_profit += int(num)

# create variables to store info about the change in profit/loss
greatest_profit = 0
greatest_delta = 0
greatest_date = ""
greatest_loss = 0
greatest_loss_delta = 0
greatest_loss_date = ""

# iterate and find greatest change in both profit and loss
for i in range(len(profit_loss_list_int)-1):
    if profit_loss_list_int[i] < profit_loss_list_int[i+1]:
        greatest_delta = profit_loss_list_int[i+1] - profit_loss_list_int[i]
        if greatest_delta > greatest_profit:
            greatest_profit = greatest_delta
            greatest_date = date_list[i+1]
    elif profit_loss_list_int[i] > profit_loss_list_int[i+1]:
        greatest_loss_delta = profit_loss_list_int[i+1] - profit_loss_list_int[i]
        if greatest_loss_delta < greatest_loss:
            greatest_loss = greatest_loss_delta
            greatest_loss_date = date_list[i+1]

# calculate average change in such a way that it matches the asssignment 
average_change = round((profit_loss_list_int[-1] - profit_loss_list_int[0]) / (len(profit_loss_list_int)-1), 2)

# dashes to make the output look interesting
dashes = ""
for i in range(20):
    dashes += "-"

# write to .txt file
with open("./PyBank/analysis/FinancialAnalysis.txt","w") as output_text_file:
    output_text_file.write("Financial Analysis")
    output_text_file.write("\n\n" + dashes)
    output_text_file.write(f"\n\n Total Months: {str(total_months)}")
    output_text_file.write(f"\n\n Total: {str(total_profit)}")
    output_text_file.write(f"\n\n Average Change: {str(average_change)}")
    output_text_file.write(f"\n\n Greatest Increase in Profits: {greatest_date} ({greatest_profit})")
    output_text_file.write(f"\n\n Greatest Decrease in Profits: {greatest_loss_date} ({greatest_loss})")

# print to terminal
print("\nFinancial Analysis")
print("\n" + dashes)
print(f"\n Total Months: {str(total_months)}")
print(f"\n Total: {str(total_profit)}")
print(f"\n Average Change: {str(average_change)}")
print(f"\n Greatest Increase in Profits: {greatest_date} ({greatest_profit})")
print(f"\n Greatest Decrease in Profits: {greatest_loss_date} ({greatest_loss})\n")