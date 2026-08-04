
num1 = int(input("How many odd numbers you want to print? "))
count = 1
print("The first ", num1, " odd numbers are ", count, sep="", end="")
count = 3
limit = 2
while (limit <= num1):
    print(", ", count, sep="", end="")
    count = count+2
    limit = limit+1

print(end=".\n")
