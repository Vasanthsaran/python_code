num1 = int(input("Up to which number you want to print natural numbers? "))
count = 1
print("The first ", num1, " natural numbers are ", count, end="", sep="")

count = 2
while (count <= num1):
    print(", ", count, end="", sep="")
    count = count+1

print(end=".\n")
