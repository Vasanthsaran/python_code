num1 = int(input("Up to which number you want to print even numbers? "))

count = 0
print("The even numbers up to ", num1, " are ", count, end="", sep="")
count = count+2
while (num1 >= count):
    print(", ", count, end="", sep="")
    count = count+2

print(end=".\n")
