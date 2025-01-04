# for loop

n = int(input())

# initialize first two terms
a, b = 0, 1
fibonacci_sequence = [a]

for i in range(1, n):
    a, b = b, a + b
    fibonacci_sequence.append(a)

print("fibonacci sequence:", n,fibonacci_sequence)



## WHILE loop

n = int(input())

# initialize first two terms
a, b = 0, 1
fibonacci_sequence = [a]

while len(fibonacci_sequence) < n:
    a, b = b, a + b
    fibonacci_sequence.append(a)

print("fibonacci sequence:", fibonacci_sequence)



