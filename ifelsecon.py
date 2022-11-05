is_male = input("Enter yes if you are male: ")
is_tall = input("Enter yes your height is greater than 5.7: ")

if is_male == "yes" and is_tall == "yes":
    print("You are tall male")
elif is_male == "yes" and is_tall != "yes":
    print("You are male but not tall")
elif is_male != "yes" and is_tall == "yes":
    print("You are not male but tall person")
else:
    print("You are not male and not tall")


######compare 3 num to find larger number ####

def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print("this program will compare 3 numbers are return which is greater")
a=int(input("Enter value for num1: "))
b=int(input("Enter value for num2: "))
c=int(input("Enter value for num3: "))
print(max_num(a,b,c))
