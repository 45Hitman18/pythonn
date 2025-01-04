## 1
i = int (input())

def factorial(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)

print(factorial(i))  


##2
i = int(input("enter a number: "))

def fibonacci(i):
    # base cases
    if i == 0:
        return 0
    elif i == 1:
        return 1
    # recursive case
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

print(f"the fibonacci number at position {i} is {fibonacci(i)}")




