def say_hi():
    print("Helo User")

say_hi()

# passing parameters to funcitons

def hello_user(user,age):
    print("Hello there " + user + "!" + " You are " + str(age)) #since parameter age is passed as int we neet to change datatype to str.

hello_user("Mike", 34)
hello_user("steive", 39)

def cube(num):
    return num*num*num

cube_of_num = (cube(6)) #cube_of_num will store the function output 6 is the parameter passed to store it in num variable
print(cube_of_num)