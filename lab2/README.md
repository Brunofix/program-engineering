# Lab 2 - File IO and Classes in Python

## Documentation

- For details see: [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)

- Python cheatsheet/concise documentation: [CodeSkulptor Docs](https://py3.codeskulptor.org/docs.html#tabs-Types)

- Interactive python environment: [CodeSkulptor](https://py3.codeskulptor.org/)

## First part: File IO python tutorial

- Open chapter 7 of the Official Python tutorial.
- Read the sections and solve the exercises

### Exercise 1

- Read section 7.1 from the tutorial
- Write a simple program which asks the user for their name and prints the
  greeting to the user (Hi Name!)
  in the three string interpolation ways described in the section:
  - using the formatted string literals method (7.1.1)
  - using the String `format()` method (7.1.2)
  - using the old string formatting method (7.1.4)
- Save your solution as ` ex1.py ` and commit


### Exercise 2

- Read section 7.2 from the tutorial.
- Read string methods documentation: 
  - https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
  - https://docs.python.org/3/library/stdtypes.html#string-methods
  - Give special focus to ` split() ` and ` strip() ` methods
- Write a simple program which loads the data from the `.csv` file hint
  about [csv file format](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/) and writes it to different files
  - Read data from file `ex2-text.csv`
  - Parse it (split lines on ` , ` chars and store in variables)
  - Write data to files:
    - `ex2-employees.txt` in format `employee,job title`
    - `ex2-locations.txt` in format `employee,office`
- Save your solution as ` ex2.py ` and commit, along with created `.txt`
  files, all in the same commit.


### Exercise 3

- Read section 5 of the tutorial, with special focus on 5.5.
  (dictionaries), and 5.6 (looping techniques for dictionaries). 
- Dictionaries are essentially `key: value` pairs, as we can see in the
  first code example in section 5.5.:

```python
# Creating a dictionary with two key:value pairs
>>> tel = {'jack': 4098, 'sape': 4139}
# Adding a new key:value pair
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
# Accessing the value of a pair using the key
>>> tel['jack']
4098
# Deleting a single item using the key
>>> del tel['sape']
# Adding another key:value pair
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
# Converting to list returns a list of keys in the dict
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
# Check if key is in the dict
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
<!--- `--->

- Write a simple program that will:
  - Load the data from `ex2-text.csv`
  - Parse the data and save it to a list of employees (var called
    `employees`)
  - Each item in the list is a dictionary with the employee's info
  - Print the created dictionary var
  - Example when printing the var `employees` with loaded and parsed data:

```python
>>> print(employees)
[{'employee': 'John Campbell', 'title': 'Software Architect', 'age': 83, 'office': '1-41'}, {'employee': 'Richel Omaba', 'title': 'Lawyer', 'age': 119, 'office': '0-33'}, ...]
```
<!--- `--->

- Save your solution as ` ex3.py ` and commit.

### Exercise 4

- Read section 7.2.2 (JSON)
- Modify the program ` ex3.py ` from the previous exercise. The modified
  program has to load and parse data to a dictionary, same as in ` ex3.py `.
  However, the modified program now has to save that data to disk in `json`
  format:

```python
with open('ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)
```
<!--- `--->

- Save your changes to ` ex3.py ` and commit both the
  modified ` ex3.py ` and the created `.json` file.
- Hint: Reread section 7.2 to remind yourself how to open a file with `with`
  keyword

## Second part: Python classes tutorial

- Open chapter 9 of the Official Python tutorial.
- Read the sections and solve the exercises

### Exercise 5

- Read sections 9 - 9.4, with a special focus on 9.3
- Write a simple program that will:
- Use class `Employee`:

```python
class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"
```

- Load employees from `ex4-employees.json` file 

```python
with open("ex4-employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)
```
<!--- `--->


- Create a list `employees_list` 
- For each employee in `employees`, create an object of a type `Employee` and
  append it to the `employees_list`
- Print all the employees using the following code:

```python
for e in employees_list:
    print(e)
```

- The code should print out:

```
John Campbell (83), Software Architect @ 1-41
Richel Omaba (119), Lawyer @ 0-33
... and so on ...
```
<!--- `--->

- Save your solution to ` ex5.py` and commit it.


### Exercise 6

Use the following starting code:

```python
import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)

    def load_from_json(self, path_to_json):
        pass

    def save_to_json(self, path_to_json):
        pass

    def print_employees(self):
        """Print all employees to stdout in format:
        Company name
        ----------------
        1. Employee name (age), job_title @ office
        2. Employee name (age), job_title @ office
        ..."""
        pass


def main():
    nike = Company("Nike")
    print(nike)

    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    # Implement load_from_json, save_to_json and print_employees methods
    # Then uncomment the implemented methods
    adidas = Company("Adidas")
    #adidas.load_from_json("ex4-employees.json")
    # After loading from json, adidas should have all the employees from
    # json file
    print(adidas)
    # Print employees should now print all the employees
    #adidas.print_employees()

    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    print(adidas)
    #adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    print(adidas)
    #adidas.print_employees()

    # Saving employees db to a new file, the file should now have 2 more
    # employees (Bart and Lisa, since Homer and Marge were fired)
    #adidas.save_to_json("ex6-employees.json")

if __name__ == "__main__":
    main()

```

- Try running the starting code
- Try understanding the starting code
- Implement missing methods in `Company` class
- Save the file and the new database (`ex6-employees.json`) and commit both
  files.


