
name = input("Unesi svoje ime: ")
pozdrav = f"Hi {name}!"
print("Koristeci f string:")
print(pozdrav)

# Using the String format() method
name = input("Unesi svoje ime: ")
pozdrav = "Hi {}!".format(name)
print("\nUsing the String format() method:")
print(pozdrav)


name = input("Unesi svoje ime: ")
pozdrav = "Hi %s!" % (name)
print("\nUsing the old string formatting method:")
print(pozdrav)
