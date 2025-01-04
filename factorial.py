# calculate factorial using for loop

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"factorial of {num} is: {factorial}")



# calculate factorial using while loop

num = 5
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"factorial of {num} is: {factorial}")

