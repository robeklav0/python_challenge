import os
import csv

ElecP = os.path.join('C:\\Users\\Demo\\Desktop\\data_Analytics\\GitRepo\\python_challenge\\PyPoll\\Resources\\election_data.csv')
nreg=0
candid = 0
candidName=[]
with open(ElecP) as csvfile:
	ElecP = csv.reader(csvfile, delimiter=',')                                 # reading the csv file

	csv_header = next(csvfile)                                                 # Avoiding Header of csv file
	print('{"Working on it"}')
	for row in ElecP:                                                          # Creating a list for candidates name
		candid = (row[2])
		candidName.append(candid)
		nreg=nreg+1                                                            # Counting Votes
	

data=set(candidName)

print(f'{"---   Election  Results    ---"}')                                   # printing results to terminal
print(f'{"------------------------------"}')
print(f'{"    " } { "Total Votes:"   }   {nreg}    ')
print(f'{"------------------------------"}')

Tname="  "
Tvaluef=0
Tname:str
Tvalue1:int
Tvalue1 = 0
Tvalue=0
name: str
for name in data:
		print(f' {name}{":  "} { candidName.count(name)*100/nreg:.2f}%{"  "} {"("} {candidName.count(name)}  {")"} ') # Loop to find the voting quantities per candidate
		Tvalue1= candidName.count(name)
		if Tvalue1>Tvalue:
			Tvalue=Tvalue1
			Tname=name
print(f'{"------------------------------"}')
print(f'{"---  Winner: " } {Tname}    ')
print(f'{"------------------------------"}')


output_path = os.path.join('C:\\Users\\Demo\\Desktop\\data_Analytics\\GitRepo\\python_challenge\\PyPoll\\Analysis\\Election_Results.txt') # Creating text file 


with open(output_path, 'w') as file_object:
	file_object.write(f'---   Election  Results   - ---      \n')
	file_object.write(f'-------------------------------      \n')
	file_object.write(f'      Total Votes:     {nreg}        \n')
	file_object.write(f'-------------------------------      \n')
	for name in data:
		file_object.write(f' {name}{":  "} { candidName.count(name)*100/nreg:.2f}%{"  "} {"("} {candidName.count(name)}  {")"} \n')


	file_object.write(f'-------------------------------      \n')
	file_object.write(f'---  Winner:  {Tname}                \n')
	file_object.write(f'-------------------------------      \n')






