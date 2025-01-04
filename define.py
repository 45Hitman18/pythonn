# define a function to calculate sum of multiple numbers
def calculate_sum(*args):
    return sum(args)

# example usage with multiple sets of values
result1 = calculate_sum(5, 10, 15)
result2 = calculate_sum(3, 7, 11, 20)
result3 = calculate_sum(2, 4, 6)

print("sum of set 1:", result1)
print("sum of set 2:", result2)
print("sum of set 3:", result3)


##calculate_sum is used to calculate the sum for each separate set of numbers.