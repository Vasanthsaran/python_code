

num1 = int(input("How many even numbers you want to print? "))
count = 0

print("The first ", num1, " even numbers are ", count, end="", sep="")
count = 2
limit = 2
while (limit <= num1):
    print(", ", count, end="", sep="")
    count = count+2
    limit = limit+1

print(end=".\n")
