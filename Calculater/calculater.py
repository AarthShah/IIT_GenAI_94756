import Arithmetic 


name=input("Enter your name: ")
print(f"HELLO {name} : Welcome to the calculator program")

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

ch=int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n Your choice : "))

if ch==1:
    print(f"The sum of {x} and {y} is {Arithmetic.add(x,y)}")
elif ch==2:
    print(f"The difference of {x} and {y} is {Arithmetic.subtract(x,y)}")

elif ch==3:
    print(f"The product of {x} and {y} is {Arithmetic.multiply(x,y)}")

elif ch==4:
    print(f"The quotient of {x} and {y} is {Arithmetic.divide(x,y)}")

else:
    print("Invalid Choice")