# Import dependencies 
import os
import csv

# Set path for file 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables  
dates = []
monthly_total = []
total_months = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
overall_change = 0

# Open file using UTF-8 encoding 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop through rows to establish monthly increase/decrease 
    for row in csvreader:
       dates.append(row[0])
       monthly_total.append(int(row[1]))
       if int(row[1]) > greatest_increase:
           greatest_increase = int(row[1])
    
    # Find total months 
    for i in dates:
        total_months += 1

    # Find total profit/loss
    for i in monthly_total:
        net_total += int(i)

    # Initialize variables to find average month-to-month change 
    start_total = int(monthly_total[0])
    end_total = int(monthly_total[-1])
    overall_change = end_total - start_total

    # Calculate average of changes and format percentage 
    average_change = overall_change/(total_months -1)
    average_change = round(average_change, 2)

    # Initialize variables to find greatest change increase and greatest change decrease 
    monthly_changes_list = []
    month_1 = int(monthly_total[0])
    month_2 = 0
    monthly_change = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

    # Loop through month=to-month changes 
    for i in monthly_total:
        month_2 = int(i)
        monthly_change = month_2 - month_1
        month_1 = month_2
        monthly_changes_list.append(monthly_change)

    # Calculate greatest change increase and decrease 
    greatest_increase = max(monthly_changes_list)
    greatest_decrease = min(monthly_changes_list)

    # Pull months corresponding to greatest increase and greatest decrease in change 
    for i in range(1, len(monthly_changes_list)): 
        if monthly_changes_list[i] == greatest_increase:
            greatest_increase_date = dates[i]
        elif monthly_changes_list[i] == greatest_decrease:
            greatest_decrease_date = dates[i]

# Display results 
print("Financial Analysis\n")
print("-------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} ${max(monthly_changes_list)}\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ${min(monthly_changes_list)}\n")

# Print to txt file 
output_result = os.path.join(".", "analysis", "results.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} ${max(monthly_changes_list)}\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${min(monthly_changes_list)}\n")