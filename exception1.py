a = int(input("enter first value"))
b = int(input("enter first value"))
try:
    print(a/b)
except ZeroDivisionError:
    print('cant write zero')
except ValueError:
    print("operation is done")