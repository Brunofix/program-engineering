import csv
import json

csv_datoteka = "ex2-text.csv"

employees = []

with open(csv_datoteka, newline="") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    column_names=csv_reader.fieldnames

    for row in csv_reader:
        employee_info={}
        for column in column_names:
            employee_info[column]= row[column]

        employees.append(employee_info)


print(employees)

with open('ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)