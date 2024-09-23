#taking list length from user
n=int(input("Enter the size of list: "))

#Empty list
list = []
for i in range(n):
    # taking list values from user
    num=int(input())
    list.append(num)

indx1=int(input("enter the index1: "))
indx2=int(input("enter the index2: "))

temp=list[indx1]
list[indx1]=list[indx2]
list[indx2]=temp
print(list)


