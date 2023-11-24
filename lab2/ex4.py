import json


with open("ex2-text.csv", "r", encoding="utf-8") as f:
    txt = f.readlines()

employees = []
for line in txt:
    split_line = line.split(',')
    split_line = [ x.strip() for x in split_line ]
    employee = {}
    employee['employee'] = split_line[0]
    employee['title'] = split_line[1]
    employee['age'] = split_line[2]
    employee['office'] = split_line[3]
    employees.append(employee)

print(employees)


