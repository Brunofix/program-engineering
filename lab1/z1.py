##Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise,
# the expectation is that you explicitly write out the year (and therefore be out of date the next year).

name = input("Upisi ime:")
age = int(input("Upisi godine:"))
repeat=int(input("Koliko puta ponovim poruku?"))
age100= 2023- age +100
name_age= "Bok %s, godine %s ces imati sto godina"%(name, age100)

print(name_age)
for i in range(repeat):
    print(name_age)