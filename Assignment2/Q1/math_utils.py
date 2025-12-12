def Area_circle(radius):
    from math import pi
    if radius < 0:
        print("radius cannot be negative..^_^")
    else:
        return pi*(radius*radius)
    
def Area_rectangle(l,b):
    if l<0 or b<0:
        print("length or breadth cannot be negative..^_^")
    else:
        return l*b
    
def Area_traingle(b,h):
    if b<0 or h<0:
        print("base or height cannot be negative..^_^")
    else:
        return 0.5*b*h
    

if __name__ == "__main__":
    print("This is math_utils module")
    r=float(input("Enter radius of circle: "))
    print("Area of circle is:",Area_circle(r))
    l=float(input("Enter length of rectangle: "))
    b=float(input("Enter breadth of rectangle: "))
    print("Area of rectangle is:",Area_rectangle(l,b))
    base=float(input("Enter base of triangle: "))
    h=float(input("Enter height of triangle: "))
    print("Area of triangle is:",Area_traingle(base,h))