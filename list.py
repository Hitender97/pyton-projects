thisislist = ['orange','apple','watermelon','kiwi']
numbers_list = [1,2,3,6,4,232.555,666]
thisislist.sort()
print (thisislist)
thisislist.reverse()
print (thisislist)
thisislist[1]='cherry'
print(thisislist)
print(thisislist[1:])
print(thisislist[1:3])
print(type(thisislist))
thisislist.extend(numbers_list)
print(thisislist)
thisislist.append("banana") #append will add the  value to the end of the list.
print(thisislist)
thisislist.insert(1, "banana") #insert will take the index and value.
print(thisislist)
thisislist.pop()    #pop function will remove the last element of list.
print(thisislist)
thisislist.remove(666)
print(thisislist)
#to empty the list use function clear thisislist.clear()
print(thisislist.count("apple"))
thisislist2=thisislist.copy()
print(thisislist2)

#Tuples - tuples are immutable once a tuple is created it can't be modified use when you know values are fix in program
coordinates=(3,4,5,2)
print(coordinates)
print(type(coordinates))

coordinates=[(3, 5),(3,6),(2,8)] #tuples inside list
print(coordinates)
print(type(coordinates))

        