import csv

csvpath = "../PyBank/Resources/budget_data.csv"
outputpath = "../PyBank/Analysis/budget_analysis.txt"
total = 0
sum_PL = 0
avg=[]
months=[]
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    csv_firstrow = next(csvreader)
    total += 1
    sum_PL += int(csv_firstrow[1])
    prev_amount=int(csv_firstrow[1])
    for row in csvreader:
        #print(row [1])
        total += 1
        sum_PL += int(row[1])
        change=int(row[1]) - prev_amount 
        avg.append(change)
        prev_amount=int(row[1])
        months.append(row[0])


    
    avg_change=sum(avg)/len(avg)
    max_index=avg.index(max(avg))
    min_index=avg.index(min(avg))

Bank_output=(f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {total}\n'
f'Total: ${sum_PL}\n'
f'Average Change: ${round(avg_change,2)}\n'
f'Greatest Increase in Profits: {months[max_index]} (${max(avg)})\n'
f'Greatest Decrease in Profits: {months[min_index]} (${min(avg)})')
                                      
print(Bank_output)

with open(outputpath,"w") as outputfile:
    outputfile.write(Bank_output)
