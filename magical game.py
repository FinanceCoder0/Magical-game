a=int(input("Think some numbers of balls Between 1 to 10:"))
b=int(input("Add the same balls of your friend:"))
import random
list=[2,4,6,8,10]
x = random.choice(list)
print("add my",x,"balls")
y=a+b+x
z=y/2
print("Drop half of balls")
print("Return friend's balls to him")
total=z-b
d=input("Do you want to know how many balls kar left:")
d=d.lower()
if d=="yes":
    print(int(total),"balls are left")
    print("Thanks for playing")
else:
    print("Thanks for playing")


