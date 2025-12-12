import math_utils as mu



print(" Welcome to Area Calculation Program \n 1) Area of Circle \n 2) Area of Rectangle \n 3) Area of Triangle ")
choice=int(input("Enter your choice : "))

if choice==1:
    r=float(input("Enter Radius of Circle : "))
    print("Area of Circle is : ",mu.Area_circle(r))

elif choice==2:
    l=float(input("Enter length of Rectangle "))
    b=float(input("Enter breadth of Rectangle "))
    print("Area of Rectangle is : ",mu.Area_rectangle(l,b))

elif choice==3:
    b=float(input("Enter base of Triangle "))
    h=float(input("Enter height of Triangle "))
    print("Area of Triangle is : ",mu.Area_traingle(b,h))

else:
    print("Invalid Choice..^_^")