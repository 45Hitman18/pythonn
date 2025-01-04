# simple if statement: checks a single condition
num = int(input())
if num > 5:
    print("the number is greater than 5")


# if-else statement: checks a condition and provides an alternative
num = int(input())
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


# if-elif-else statement: checks multiple conditions in sequence
marks = int(input())

if marks >= 90:
    print("grade: a")
elif marks >= 75:
    print("grade: b")
else:
    print("grade: c")


# nested if statement: an if statement inside another if
age = int(input())
if age >= 18:
    if age < 21:
        print("you are an adult, but not old enough to drink in some countries")
    else:
        print("you are an adult")
else:
    print("you are a minor")
