num1 = int(input("Enter a number to compute it's factorial: "))
count = num1
factorail = 1
while (count > 0):
    factorail = count*factorail
    count = count-1
print("The factorial of ", num1, " is ", factorail, end=".\n", sep="")
