import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

#initialize counter for total number of rows(records) in budget_data.csv file
row_cntr = 0

#define lists to be populated by csvfile without the header

mydate = []
profit_loss = []
monthly_profit_change = []


with open(csvpath, newline = '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ',')
   
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    total = 0
    for row in csvreader:
        row_cntr += 1
        
        # Add csv date to mydate list
        #mydate.append(row)
        mydate.append(row[0])
        
        # tally up a sum of total profit/losses and add to profit_loss list
        total += int(row[1])  
        profit_loss.append(row[1])
    
    
    index = 0
    for profit_val in profit_loss:
        #if this is the first value in the list
        if (index == 0):    
            
            #set value to prev_month
            prev_month = int(profit_val) 
            index += 1
            
        
        #if not the first file and not the last file (in between)        
        elif index < 86:
            curr_month = int(profit_val)
            profit_change = int(curr_month - prev_month)
            monthly_profit_change.append(str(profit_change))
            prev_month = curr_month
            index += 1
            
        #else  this is the last value in profit_loss list
        else: 
            
            #set last value to curr_month and prev_month to value just before last value
            curr_month = (profit_loss[index])
            prev_month = (profit_loss[index-1])
            profit_change = int(curr_month - prev_month)
            monthly_profit_change.append(str(profit_change))
    
    total_profit_change = 0
    avg_change = 0.00
    for val in monthly_profit_change:
        total_profit_change += int(val)
        
    #computes the average change in profits/losses by taking a total of all values in list called 
    #monthly_profit_change and dividing it by the total number of months(records in csv file which is in var
    #row_cntr. Then the answer is rounded to 2 decimal places.
    avg_change = round((total_profit_change/(row_cntr-1)), 2)
    
    #computes the max value in the list called monthly_profit_change
    cur_val = 0 
    for val in monthly_profit_change:
        
        if int(val) > cur_val:
            max_prof = int(val)
            cur_val = int(val)
            
    #determine at what index location max_prof was found in monthly_profit_change
    max_index = (monthly_profit_change.index(str(max_prof)))
      
    
    #computes the min value in the list called monthly_profit_change
    cur_val = 0
    for val in monthly_profit_change:
        
        if int(val) < cur_val:
            min_prof = int(val)
            cur_val = int(val)
    
    min_index = (monthly_profit_change.index(str(min_prof)))
        
        
    text_file = open('hw_3_Bankoutput.txt', 'w')
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("Financial Analysis Output")
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("Total Months: "+ str(row_cntr))  
    text_file.write("'\n'")
    text_file.write("Total: $" + str(total))
    text_file.write("'\n'")
    text_file.write("Average Change: $"+ str(avg_change))
    text_file.write("'\n'")
    text_file.write("Greatest increase in profits: "+ mydate[int(max_index)+1] +' $' + str(max_prof))
    text_file.write("'\n'")
    text_file.write("Greatest decrease in profits: "+ mydate[int(min_index)+1] +' $' + str(min_prof))
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.write("'\n'")
    text_file.write("-----------------------------------------------------------------")
    text_file.close()
    


    #print output to the terminal/screen
    print("------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total Months: " + str(row_cntr))
    print("Total: $", total)
    print("Average Change: $", avg_change)
    print("Greatest increase in profits: " , mydate[int(max_index)+1]+ " $", (max_prof))
    print("Greatest decrease in profits: " +mydate[int(min_index)+1]+ " $", (min_prof))
    print("------------------------------------------------")
    print("------------------------------------------------")

