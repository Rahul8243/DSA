# Enter your name using input function
name = input("Enter your name: ")
print("Hello,", name + "!")

# Addition of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2
print("The sum of", num1, "and", num2, "is:", total)

# Grading according to the marks
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: Fail")

# Average of numbers
count = int(input("How many numbers? "))
total = 0

for i in range(count):
    num = float(input("Enter number: "))
    total += num  # shorthand for total = total + num

average = total / count
print("Average is:", average)
