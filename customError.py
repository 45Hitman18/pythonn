class CustomError(Exception):
    pass

try:
    x = -5
    if x < 0:
        raise CustomError("number must be positive!")
except CustomError as e:
    print(f"caught a custom error: {e}")
