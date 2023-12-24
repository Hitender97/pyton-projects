# this will print 90o triangle in numeric format
n=int(input("enter the value of n: "))

for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print()

# this will print 90o triangle in capital alphabet format
m=int(input("Enter the value of m: "))

for i in range(1, m+1):
    for j in range(1, i+1):
        print((chr(64 + j)), end="")
    print()

# this will print equilateral triangle in numeric format
l=int(input("Enter the value of l: "))

for i in range(1, l+1):
    print (" " * (l-i), end="")

    for j in range(1, 2 * i):
        print(j, end="")
    print()
