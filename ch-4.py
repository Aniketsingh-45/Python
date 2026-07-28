#lists= lists are muteable and can be changed after creation it is ordered collection of items

# friends=["aniket", 85, 9.5, "orange", 3.14, "python", 100] #list of mixed data types
# print(friends)
# print(friends[4]) #accessing a specific element in the list by using [index]
# friends[3]="apple" #modifying a specific element in the list by using [index]
# print(friends)
# print(friends[2:5]) # accessing a range of elements in the list by using [start:stop]
# friends.append("rahul") #adding an element at the end of the list
# print(friends)


# l1= [1,27,13,74,45,18] #list of integers
# l1.sort() #sorting the list in ascending order
# print(l1) 
# l1.reverse() #reversing the list
# print(l1)
# l1.insert(4, 66 ) #inserting an element at a specific position in the list
# print(l1)
# l1.pop(3) #removing an element at a specific position in the list
# print(l1)
# l1.remove(74) #removing an element from the list by value



#tuple= tuples are immutable and cannot be changed after creation it is ordered collection of items
# t1=(1,27,"aniket", 6.6, "ball",27) #tuple of integers
# print(type(t1))
# print(t1)
# no= t1.count(27) #counting the number of occurrences of a specific element in the tuple
# print(no)
# t2=(1,) #tuple with single element
# print(type(t2))
# a=(44,56,66,"apple",88)
# i= a.index(66) #finding the index of a specific element in the tuple
# print(i)
# print(len(a)) #finding the length of the tuple


#practice que 1

# fruits=[] #empty list

# f1= input("enter fruit name :")
# fruits.append(f1)
# f1= input("enter fruit name :")
# fruits.append(f1)
# f1= input("enter fruit name :")
# fruits.append(f1)
# f1= input("enter fruit name :")
# fruits.append(f1)
# f1= input("enter fruit name :")
# fruits.append(f1)
# print(fruits) 


#que 2

# mark=[] #empty list

# f1= int(input("enter marks :"))
# mark.append(f1)
# f1= int(input("enter marks :"))
# mark.append(f1)
# f1= int(input("enter marks :"))
# mark.append(f1)
# f1= int(input("enter marks :"))
# mark.append(f1)
# f1= int(input("enter marks :"))
# mark.append(f1);

# mark.sort() #sort the list in ascending order
# print(mark)  #printing the list of marks


#que 3

l=(1,22,33,44,12)
print(sum(l)) #sum of all elements in the tuple