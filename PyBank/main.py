import os
import csv
bankStmt = os.path.join('C:\\Users\\Demo\\Desktop\\data_Analytics\\GitRepo\\python_challenge\\PyBank\\Resources\\budget_data.csv')

month=0                                                              # Declaring Variables
Total=0 
GrandTotal=0
pyl=[]
date=0
dates=[]
pair=[]
with open(bankStmt) as csvfile:                                      # Opening csv file
    bankStmt = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvfile)                                       # Avoiding header
    for row in bankStmt:                                             # Reading the Profit/Lossesvalues  
        Total = int(float(row[1]))
        pyl.append(Total)                                            # Cerating list with Profit/Losses values
        GrandTotal = GrandTotal + Total                              # Getting the Total Profit/Losses value 
        month=month+1                                                # Getting Total Months
        date = (row[0])
        dates.append(date)                                           # Creating list for months

pyl.reverse()                                                        # Adjusting Profit/Losses list to substract 
dates.reverse()                                                      # Adjusting Dates list to keep sync with Profit/Losses list
      
suma=0
for i in range(len(pyl)-1):                                          # Adding values in Profit/Losses reversed list
    suma =  pyl[i]-pyl[i+1]
    pair.append(suma)
avch= sum(pair)                                                      # Getting Average Change
index = pair.index(max(pair))                                        # Getting Greatest increase
index2= pair.index(min(pair))                                        # Getting Greatest decrease


print(f'{"------------------------------------------------------------------"}')     # Printing results to terminal
print(f'{"---                   Financial Analysis                       ---"}')
print(f'{"------------------------------------------------------------------"}')
print(f'{"    " } { "Total Months:"   }   {month}    ')
print(f'{"    " } { "Total :"   } {"$"}{GrandTotal}    ')
print(f'{"    " } { "Average Change:"   }  {"$"}{avch/85:.2f}    ')
print(f'{"    " } { "Greatest Increase in Profits:"   } {(dates[index])}   {"($"}{max(pair)} {")"} ')
print(f'{"    " } { "Greatest decrease in Profits:"   } {(dates[index2])}  {"($"}{min(pair)} {")"} ')
print(f'{"-----------------------------------------------------------------"}')

output_path = os.path.join('C:\\Users\\Demo\\Desktop\\data_Analytics\\GitRepo\\python_challenge\\PyBank\\Analysis\\Financial_Analysis.txt')  # Creating text files with results


with open(output_path, 'w') as file_object:
    file_object.write(f'------------------------------------------------------------------   \n') 
    file_object.write(f'---                   Financial Analysis                       ---   \n')
    file_object.write(f'------------------------------------------------------------------   \n')
    file_object.write(f'   Total Months:     {month}                                         \n')
    file_object.write(f'   Total : ${GrandTotal}                                             \n')
    file_object.write(f'   Average Change:    ${avch/85:.2f}                                 \n')
    file_object.write(f'   Greatest Increase in Profits:   {(dates[index])}   (${max(pair)}) \n')
    file_object.write(f'   Greatest decrease in Profits:   {(dates[index2])}  (${min(pair)}) \n')
    file_object.write(f'------------------------------------------------------------------   \n')


