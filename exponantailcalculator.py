#without function
base=int(input("Enter the base value: "))
expo=int(input("Enter the power value: "))
result=1

for i in range(expo):
    result = result * base
print(result)

#with function
def raise_to_power(base_value, pow_value):
    result = 1
    for i in range(pow_value):
        result = result * base_value
    return result

a=int(input("Enter the base value: "))
b=int(input("Enter the power value: "))
print(raise_to_power(a, b))

