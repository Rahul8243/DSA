# Take upper limit
n = int(input("Enter the upper limit: "))

even_numbers = []
squares = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)
        squares.append(i ** 2)

print("\nEven Numbers:", even_numbers)
print("Squares:", squares)
print("Total even numbers:", len(even_numbers))
