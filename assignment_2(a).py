# Take input from the user
n = int(input("Enter a number: "))

print("\nNumbers from 1 to", n, "using for loop:")
for i in range(1, n + 1):
    print(i, end=" ")

print("\n\nNumbers from", n, "to 1 using while loop:")
while n >= 1:
    print(n, end=" ")
    n -= 1
