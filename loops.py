# for loop: iterates over a sequence (e.g., list, string, or range)
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print("fruit:", i)


# for loop with range: iterates over numbers in a range
for i in range(1, 6):  # from 1 to 5 (end is exclusive)
    print("number:", i)


# while loop: runs as long as a condition is true
count = 1
while count <= 5:
    print("count:", count)
    count += 1  # increment


# nested loops: loop inside another loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
