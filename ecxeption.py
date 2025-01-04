try:
    # code that may raise an exception
    num = int(input("enter a number: "))
    result = 10 / num
    print("result:", result)
except ZeroDivisionError:
    print("error: you can't divide by zero!")
except ValueError:
    print("error: please enter a valid number!")
finally:
    # this block will always execute
    print("thank you for using the program!")
