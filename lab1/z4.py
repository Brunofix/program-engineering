#   Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#   (If you don’t know what a divisor is, it is a number that divides evenly into another number.
#   For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#

number=int(input("Unesi broj:"))
list_divisors = []

for div in range(1,number):
    if number % div ==0:
        list_divisors.append(div)
        print(div)