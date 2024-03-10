# import what we need

import csv
import os

# create lists for incoming data
date_list = []
profit_loss_list = []
date_change_dict = {}

# read csv to variable
cwd = os.getcwd()
#budget_data_path = os.path.join("PyBank","Resources","budget_data.csv")
budget_data_path = "./PyBank/Resources/budget_data.csv"

with open(budget_data_path, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    for row in csvreader:
        date_list.append(row[0])
        profit_loss_list.append(row[1])

date_list_header = date_list.pop(0)
profit_loss_list_header = profit_loss_list.pop(0)

profit_loss_list_int = [int(x) for x in profit_loss_list]

total_months = len(date_list)
print(total_months)

print(profit_loss_list)

total_profit = [int(num) for num in profit_loss_list_int]
#total_profit = 0
#for num in profit_loss_list_int:
#    total_profit += int(num)
print(total_profit)

greatest_profit = 0
greatest_delta = 0
greatest_date = ""
greatest_loss = 0
greatest_loss_delta = 0
greatest_loss_date = ""

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

print(greatest_profit)
print(greatest_date)
print(greatest_loss)
print(greatest_loss_date)

