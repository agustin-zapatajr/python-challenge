import os, csv
from pathlib import Path

input_file = Path("PyBank", "Resources", "budget_data.csv" )

#empty lists
total_months = []
total_profit = []
profit_change= []

with open(input_file,newline ="", encoding = "utf-8") as budget:

    csvreader = csv.reader(budget,delimiter = ",")

    header = next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):

        profit_change.append(total_profit[i+1]-total_profit[i])

# Min and Max
max_increase = max(profit_change)
max_decrease = min(profit_change)

max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1

#Print statements

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change : ${round(sum(profit_change)/len(profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

#Output files

output_file = Path("PyBank", "Financial_Analysis.txt")

with open(output_file,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")