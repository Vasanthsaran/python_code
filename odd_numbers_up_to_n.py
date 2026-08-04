
num1 = int(input("Up to which number you want to print odd numbers? "))
# count=1
print("The odd numbers up to ", num1, " are 1", end="", sep="")
count = 3
while (count <= num1):
    print(", ", count, sep="", end="")
    count = count+2

print(end=".\n")
