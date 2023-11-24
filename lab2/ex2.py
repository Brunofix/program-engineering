import csv


employees=[]

with open ('ex2-text.csv', 'r') as csv_file:

    if len (row) >=2:

        employee= row[0]

        office = row[-1]

        employees.append(f"{employee},{row[1]}")
        ([]).append(f"{employee},{office}")

with open ('ex2-employees.txt', 'w') as employees_files:

    employees_file.write('\n'.join(employees))

with open('ex2-locations.txt', 'w') as locations_files:

    locations_files.write('\n'.join([]))