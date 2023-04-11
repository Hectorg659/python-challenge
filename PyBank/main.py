#import modules
import os
import csv
#Set CSV path 
csvpath = os.path.join('Resources', 'budget_data.csv')
#Set CSV Output path
Financial_analysis_final = os.path.join('Analysis', 'financial_analysis_final.txt')
#Open the CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

    next(csvreader)
    #Assigned Variables
    month_count = 0
    net_total = 0
    previous_value = 0
    total_changes = 0
    greatest_decrease = ["", 9999999]
    greatest_increase = ["", 0]
    total_change_list = []
    change_month = []

    #Loop through all months to count amount of months/net total
    for row in csvreader:
        
        #Monthly count of Data
        month_count+= 1
        #Calculate net total of data set
        net_total+= int(row[1])
        
        #Calculate the changes in profit/losses
        total_changes = float(row[1]) - previous_value
        previous_value = float(row[1])
        total_change_list = total_change_list + [total_changes]
        change_month = [change_month] + [row[0]]

        #Calculate greatest increase in profits over the period
        if total_changes>greatest_increase[1]:
            greatest_increase[1] = total_changes
            greatest_increase[0] = row[0]
        #Calculate greatest decrease in profits over the period
        if total_changes<greatest_decrease[1]:
            greatest_decrease[1] = total_changes
            greatest_decrease[0] = row[0]

#Writing changes to new CSV file with final analysis
with open(Financial_analysis_final, 'w') as file:

    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write("Total Months: %d\n" % month_count)
    file.write("Total: $%d\n" % net_total)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
    #Print results on terminal
    print("Financial Analysis\n")
    print("-----------------------------\n")
    print("Total Months: %d\n" % month_count)
    print("Total: $%d\n" % net_total)
    print("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
