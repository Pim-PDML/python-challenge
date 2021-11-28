import os
import csv

poll_data = os.path.join('.', 'Resources', 'election_data.csv')

with open(poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    unique_list = []
    for row in csv_reader:   
        if row[2] not in unique_list:            
            unique_list.append(row[2])
            
#print(unique_list)

with open(poll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

#Total number of votes cast           
    cnt_vote = 0
    Khan_cnt = 0
    Correy_cnt = 0
    Li_cnt = 0
    O_Tooley_cnt = 0
    
    for row in csv_reader:  
        cnt_vote += 1 
        if row[2] in "Khan":            
            Khan_cnt += 1
        elif row[2] in "Correy":            
            Correy_cnt += 1
        elif row[2] in "Li":            
            Li_cnt += 1
        elif row[2] in "O'Tooley":            
            O_Tooley_cnt += 1


    Khan_pct = (Khan_cnt * 100) / cnt_vote
    Correy_pct = (Correy_cnt * 100) / cnt_vote
    Li_pct = (Li_cnt * 100) / cnt_vote
    O_Tooley_pct = (O_Tooley_cnt * 100) / cnt_vote
    
    if (Khan_cnt > Correy_cnt) & (Khan_cnt > Li_cnt) & (Khan_cnt > O_Tooley_cnt):
        winner = "Khan"
    elif (Correy_cnt > Khan_cnt) & (Correy_cnt > Li_cnt) & (Correy_cnt > O_Tooley_cnt):
        winner = "Correy"
    elif (Li_cnt > Khan_cnt) & (Li_cnt > Correy_cnt) & (Li_cnt > O_Tooley_cnt):
        winner = "Li"
    elif (O_Tooley_cnt > Khan_cnt) & (O_Tooley_cnt > Li_cnt) & (O_Tooley_cnt > Correy_cnt):
        winner = "O'Tooley"
    
#print(Khan_cnt, Correy_cnt, Li_cnt, O_Tooley_cnt, cnt_vote) 
#print(round(Khan_pct,3), round(Correy_pct,3), round(Li_pct,3), round(O_Tooley_pct,3))

#print(f'Average Change: {Khan_pct:.3f}')

print("Election Results")
print("----------------------------------------")
print(f'Total Votes: {str(cnt_vote)}')
print("----------------------------------------")
print(f'Khan: {Khan_pct:.3f}% ({str(Khan_cnt)})')
print(f'Correy: {Correy_pct:.3f}% ({str(Correy_cnt)})')
print(f'Li: {Li_pct:.3f}% ({str(Li_cnt)})')
print(f"O'Tooley: {O_Tooley_pct:.3f}% ({str(O_Tooley_cnt)})")
print("----------------------------------------")
print(f'Winner: {winner}')
print("----------------------------------------")



with open('./analysis/results.csv', 'w') as csvwriter:
    csvwriter.writelines("Election Results\n")
    csvwriter.writelines("----------------------------------------\n")
    csvwriter.writelines(f'Total Votes: {str(cnt_vote)}\n')
    csvwriter.writelines("----------------------------------------\n")
    csvwriter.writelines(f'Khan: {Khan_pct:.3f}% ({str(Khan_cnt)})\n')
    csvwriter.writelines(f'Correy: {Correy_pct:.3f}% ({str(Correy_cnt)})\n')
    csvwriter.writelines(f'Li: {Li_pct:.3f}% ({str(Li_cnt)})\n')
    csvwriter.writelines(f"O'Tooley: {O_Tooley_pct:.3f}% ({str(O_Tooley_cnt)})\n")
    csvwriter.writelines("----------------------------------------\n")
    csvwriter.writelines(f'Winner: {winner}\n')
    csvwriter.writelines("----------------------------------------\n")



