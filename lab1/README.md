# Lab 1


## Interactive tutorial

For details see: [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)

1. Some Python intro
1. Using the Python Interpreter
    1. Invoking the Interpreter
1. An Informal Introduction to Python
    1. Simple data-types
        1. Numbers
        2. Strings
        3. Lists
1. More Control Flow Tools
    1. ` if ` Statements
    2. ` for ` Statements
    3. The ` range() ` Function
    4. ` break ` and ` continue ` Statements, and ` else ` Clauses on Loops
    5. ` pass ` Statements
    6. Defining Functions
    7. More on Defining Functions
    8. Intermezzo: Coding Style
1. Python IDEs and VMs
1. Data Structures
    1. More on Lists
    1. The ` del ` Statement
    1. Tuples and Sequences
    1. Sets
    1. Dictionaries
    1. Looping Techniques
    1. More on Conditions
    1. Comparing Sequences and Other Types


## Interactive exercises

Selected exercises from [PracticePython.org](https://www.practicepython.org/)

- 1-10, 13, 24

## Set up .gitignore

Make ` .gitignore ` file in the root of your repository. Add python
intermediate files for git to ignore:

```
/**/*/__pycache__/*
/**/*/*.pyc

```

## Your own work

Each exercise can be a different function with a sensible function name. Each
exercise can also be a different program with a single function. However, the
implementation of the task given in each exercise has to be in a function. From
the `main()` function you have to call the function that performs the work with
the arguments that demonstrate the desired functionality. An example would be a
program that returns a number of uppercase letters for a string:

```python
def uppercase_count(string):
    """Return the number of uppercase letters inside the string.

    Arguments:
    string - input string which will be checked
    """

    count = 0;
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in string:
        if char in allowed_chars:
            count += 1

    return count

def main():
    strings = [
            "pero", 
            "Pero",
            "PEROPERO",
            "WySiWyG"
    ]   

    for string in strings:
        print(f"String '{string}' has {uppercase_count(string)} uppercase letters")

if __name__ == "__main__":
    main()
```

Every function has to have a docstring, for info check [PEP 275](https://www.python.org/dev/peps/pep-0257/).
Regardles of the way you choose to implement the exercises (whether it be in
one file or in multiple files), every exercise has to be in its own commit,
with a sensible commit message.

Use this example as a template of how to implement your own exercises.


#### Exercise 1

Input the comma-separated integers and transform them into a list of integers.
Print the number of even ints in the given list. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
Use a function for counting evens.

        count_evens([2, 1, 2, 3, 4]) → 3
        count_evens([2, 2, 0]) → 3
        count_evens([1, 3, 5]) → 0


#### Exercise 2

Input the comma-separated integers and transform them into a list of integers.
Return the "centered" average of an list of ints, which we'll say is the mean
average of the values, except ignoring the largest and smallest values in the
list. If there are multiple copies of the smallest value, ignore just one copy,
and likewise for the largest value. Use int division to produce the final
average. You may assume that the list is length 3 or more.

        centered_average([1, 2, 3, 4, 100]) → 3
        centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
        centered_average([-10, -4, -2, -4, -2, 0]) → -3

#### Exercise 3

Input the comma-separated integers and transform them into a list of integers.
Given a list of ints, return True if the list contains a 2 next to a 2 somewhere.

#### Exercise 4

Input a string and pass it to the function. The function returns a tuple of
three values: a count of uppercase letters, a count of lowercase letters and a
count of numbers.

        char_types_count("asdf98CXX21grrr") → (3,8,4) 
