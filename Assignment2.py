# Task 1

number=int(input("Enter a Number:"))
if number%2==0: 
     print(f"{number} is an Even Number")

else: 
     print(f"{number} is an Odd Number")

# Task 2


print("To Get The Integer Sum between 2 Numbers ")
startNumber=int(input("Enter starting Number:"))
EndNumber=int(input("Enter starting Number:"))
sum=0
for i in range(startNumber,EndNumber+1,1):
    sum=sum+i

print(f"The Sum of numbers from {startNumber} to {EndNumber} : {sum}")
