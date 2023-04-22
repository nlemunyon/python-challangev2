# here we go
#Py bannk

import os
import csv



path = "Resources/budget_data.csv"
output_file_path = 'output.csv'


csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)

#total # of months
#total amount of prof/losses
net_prof = 0
total_months = 0
for row in csv_reader:
   total_months += 1
   net_prof +=int(row[1])

csv_file.seek(0)
next(csv_reader)

#change in net_proff, return average change

changes = [1]
previous_value = None

for row in csv_reader:
        value = int(row[1])
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
        previous_value = value

csv_file.seek(0)
next(csv_reader)

# Calculate the average change
if len(changes) > 0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0


csv_file.seek(0)
next(csv_reader)


max_increase = 0
previous_value = None

 # Loop over each row in the file and calculate the increase from the previous value
for row in csv_reader:
        value = float(row[1])
        if previous_value is not None:
            increase = value - previous_value
            if increase > max_increase:
                max_increase = increase
        previous_value = value


csv_file.seek(0)
next(csv_reader)

# greatest decrease

max_decrease = 0
previous_value = None

for row in csv_reader:
        for row in csv_reader:
            value = float(row[1])
            if previous_value is not None:
                decrease = value - previous_value
                if max_decrease is None or decrease < max_decrease:
                    max_decrease = decrease
                    max_decrease_title = [row[0]]
            previous_value = value





#print(results
print( "Financial Analysis"
        "--------------------")
print (f"total months is" ,total_months)
print (f"Total $ is",net_prof)
print(f"Average change is ", average_change)
print(f"Max increase is" ,max_increase)
print(f"Max decrease is" ,max_decrease)

with open(output_file_path, 'w', newline='') as output_file:

    # Create a CSV writer object
    csv_writer = csv.writer(output_file)

    # Write the header row
    csv_writer.writerow(['All results',])

    #
    csv_writer.writerow([total_months, 
                         net_prof, 
                         average_change, 
                         max_increase, max_decrease])