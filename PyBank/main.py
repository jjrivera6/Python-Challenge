#PyBank
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#path to csv

pybankpath = os.path.join("Resources","budget_data.csv")

profit = []
monthly_change = []
date = []

count = 0
total_profit = 0
overall_change_profit = 0
initial_profit = 0

with open(pybankpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	for row in csvreader:

		#count method to calculate the number of months in dataset

		count = count + 1

		date.append(row[0])

		profit.append(row[1])
		total_profit = total_profit + int(row[1])

		final_profit = int(row[1])
		monthly_change_profit = final_profit - initial_profit

		monthly_change.append(monthly_change_profit)

		overall_change_profit = overall_change_profit + monthly_change_profit
		initial_profit = final_profit

		average_change_profits = (overall_change_profit/count)

		greatest_increase_profits = max(monthly_change)
		greatest_decrease_profits = min(monthly_change)

		increase_date = date[monthly_change.index(greatest_increase_profits)]
		decrease_date = date[monthly_change.index(greatest_decrease_profits)]

#print statements to run in terminal"

print("-------------------------------------")
print("Final Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" +str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("-------------------------------------")



