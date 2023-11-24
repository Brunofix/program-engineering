num = int(input("unesi djeljenik: "))
check= int(input("unesi djelitelj: "))
if num % check ==0:
    print(f"broj {num} je djeljiv sa {check}")
else:
    print(f"Broj{num} nije djeljiv sa {check}")
