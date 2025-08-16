# Input 10 numbers
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Counters
positive = 0
negative = 0
zeros = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1

# Display results
print("\nNumbers Entered:", numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zeros)
