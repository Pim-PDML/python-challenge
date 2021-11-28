import os
import csv

budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

#set Count mounths    
#set Summary of profit/Losses
    cnt_mth = 0
    sum_profit = 0
    for row in csv_reader:
            sum_profit += int(row[1])
            cnt_mth += 1  
    
    #print(cnt_mth)
    #print(sum_profit)

#set Average of profit/Losses 
#    pre_profit = int((next(csv_reader))[1])
#     sum_chg_profit = 0
#     cnt = 0
    
#     for row in csv_reader:                
#         chg_profit = int(row[1]) - pre_profit
#         sum_chg_profit += chg_profit        
#         cnt += 1
#         pre_profit = int(row[1])
       
#     chg_profit = float(sum_chg_profit/cnt)
        
    #print(f'${chg_profit:.2f}')     

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
#set Greatest Increase and Decrease 
    pre_profit = int((next(csv_reader))[1])
    sum_chg_profit = 0
    cnt = 0
    max_profit = 0
    min_profit = 0
    
    for row in csv_reader:
        chg_profit = int(row[1]) - pre_profit
        sum_chg_profit += chg_profit        
        cnt += 1
        if chg_profit > max_profit:
            max_profit = chg_profit
            maxM_profit = row[0]
        elif chg_profit < min_profit:
            min_profit = chg_profit
            minM_profit = row[0] 
        pre_profit = int(row[1])

#set Average of profit/Losses        
    chg_profit = float(sum_chg_profit/cnt)
    

print("Financial Analysis")
print("----------------------------------------")
print(f'Total Months: {str(cnt_mth)}')
print(f'Total: ${str(sum_profit)}')
print(f'Average Change: ${chg_profit:.2f}')
print(f'Greatest Increase in Profits: {maxM_profit} (${max_profit})')
print(f'Greatest Decrease in Profits: {minM_profit} (${min_profit})')

# Specify the file to write to
#output_path = os.path.join(".", "analysis", "results.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow("Financial Analysis")
#     csvwriter.writerow("----------------------------------------")
#     csvwriter.writerow(f'Total Months: {str(cnt_mth)}')
#     csvwriter.writerow(f'Total: ${str(sum_profit)}')
#     csvwriter.writerow(f'Average Change: ${chg_profit:.2f}')
#     csvwriter.writerow(f'Greatest Increase in Profits: {maxM_profit} (${max_profit})')
#     csvwriter.writerow(f'Greatest Decrease in Profits: {minM_profit} (${min_profit})')

# Open the file using "write" mode. Specify the variable to hold the contents

with open('./analysis/results.csv', 'w') as csvwriter:
    csvwriter.writelines("Financial Analysis\n")
    csvwriter.writelines("----------------------------------------\n")
    csvwriter.writelines(f'Total Months: {str(cnt_mth)}\n')
    csvwriter.writelines(f'Total: ${str(sum_profit)}\n')
    csvwriter.writelines(f'Average Change: ${chg_profit:.2f}\n')
    csvwriter.writelines(f'Greatest Increase in Profits: {maxM_profit} (${max_profit})\n')
    csvwriter.writelines(f'Greatest Decrease in Profits: {minM_profit} (${min_profit})\n')


