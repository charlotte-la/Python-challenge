# import modules
import csv
import os

# defining variables
TotalMonths = 0
Profits = 0
GreatestIncrease = 0
GreatestDecrease = 9999999999999999
ProfitChange = 0
TotalProfitChange = 0
total_net = 0
HighestMonth = ""
LowestMonth = ""
Profit = []

# open file
csvpath = "./Resources/budget_data.csv"  # path to csv file
csvfile = open(csvpath)  # open csv file
reader = csv.reader(csvfile)
header = next(reader)

# loop through rows
first_row = next(reader)  # read first row
prev_net = int(first_row[1])
TotalMonths = TotalMonths + 1  # add 1 to total months
total_net = total_net + int(first_row[1])  # add the first profit to the total profits

# loop through from the second row
for row in reader:
    print("row: ", row)
    TotalMonths = TotalMonths + 1
    total_net = total_net + int(row[1])

    print("net change", prev_net)  # confirm the previous net is correct

    # here we calculate the change in profit
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])

    Profit.append(net_change)  # add the change in profit to the list

    # Calculate the greatest increase
    if net_change > GreatestIncrease:
        HighestMonth = row[0]
        GreatestIncrease = net_change

    # Calculate the greatest decrease
    if net_change < GreatestDecrease:
        LowestMonth = row[0]
        GreatestDecrease = net_change

# calculate the average change in profit
net_profit_avg = sum(Profit) / len(Profit)

# print report and write to file
file_to_save = open("budget_analysis.txt", "w")
print(f"Financial Analysis")
file_to_save.write(f"Financial Analysis\n")
print(f"----------------------------")
file_to_save.write(f"----------------------------\n")
print(f"Total Months: {TotalMonths}")
file_to_save.write(f"Total Months: {TotalMonths}\n")
print(f"Total: ${total_net}")
file_to_save.write(f"Total: ${total_net}\n")
print(f"Average Change: ${net_profit_avg:.2f}")
file_to_save.write(f"Average Change: ${net_profit_avg:.2f}\n")
print(f"Greatest Increase in Profits: {HighestMonth} (${GreatestIncrease})")
file_to_save.write(f"Greatest Increase in Profits: {HighestMonth} (${GreatestIncrease})\n")
print(f"Greatest Decrease in Profits: {LowestMonth} (${GreatestDecrease})")
file_to_save.write(f"Greatest Decrease in Profits: {LowestMonth} (${GreatestDecrease})\n")
file_to_save.close()  # close the text file

csvfile.close()  # close the csv file
