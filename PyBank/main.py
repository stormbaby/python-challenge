
import csv
import os

rel_path = './Resources/budget_data.csv'

# initialize variables
prior_profit_losses = 0
sum_changes = 0
profit_losses = 0
count = 0
great_inc = 0
great_dec = 0

#open and set reader for input file
with open(rel_path) as bank_data:
    csvreader = csv.reader(bank_data)

    # Read the header
    header = next(csvreader)
    rows_data = 0
    # For each row in the CSV file.
    for row in csvreader:

        # Add to the total row count
        rows_data += 1
        #if the first row of data
        if rows_data == 1:
            prior_profit_losses = int(row[1])
        #if not the first row of data
        else:
            change = int(row[1]) - prior_profit_losses
            sum_changes += change
            prior_profit_losses = int(row[1])
            #find the greatest increase and the greatest decrease
            if change > great_inc:
                great_inc = change
                date_inc = row[0]
            elif change < great_dec:
                great_dec = change
                date_dec = row[0]
#increase the total of profit and losses
        profit_losses += int(row[1])


#calculate the total of changes
avg_change = sum_changes/(rows_data-1)

# Save the results to our text file.
with open('analysis/PyBank_output_data', "w") as txt_file:

    
    analysis_results = (
        f"\nFinancial Analysis\n\n"
        f"-------------------------\n\n"
        f"Total Months: {rows_data}\n\n"
        f"Total: ${profit_losses}\n\n"
        f"Average Change: {avg_change:.2f}\n\n"
        f"Greatest Increase in Profits: {date_inc} (${great_inc})\n\n"
        f"Greatest Decrease in Profits: {date_dec} (${great_dec})\n\n")

    print(analysis_results, end="")

    txt_file.write(analysis_results)

 
        # results to the terminal.
        
  



 
  