number=[]
output={}
no=input("Enter numbers separated by space: ")
number=no.split(",")
print("The list of numbers is:",number)
count_even=0
count_odd=0
for i in number:
    i=int(i)
    if i%2==0:
        print(f"{i} is even")
        output[i]="even"
        count_even +=1
    else:
        print(f"{i} is odd")
        output[i]="odd"
        count_odd +=1

print("Total even numbers are:",count_even)
print("Total odd numbers are:",count_odd)
print("The output dictionary is:",output)


