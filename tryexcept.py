try:
    num= 10/0
    number = int(input("Enter the number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as valueerr:
    print(valueerr)