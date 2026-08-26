# # dictionary it is a collection of key value pairs it is unordered and mutable data type
# d={} # empty dictionary
# marks= {
# "harry": 45,
# "mary": 47,
# "john": 52,
# "jane": 40 
# }
# print(marks, type(marks))  
# print(marks["harry"])
# print(marks.items()) # returns a list of a tuple for each key value pair
# print(marks.keys()) # returns a view object that displays a list of all keys in the dictionary, output : dict_keys(['harry', 'mary', 'john', 'jane'])
# print(marks.values()) # returns a view object that displays a list of all values in the dictionary
# marks.update({"harry":65, "aniket": 70}) # update the dictionary with new key value pairs
# print(marks) # {'harry': 65, 'mary': 47, 'john
# print(marks.get("aniket")) # returns the value for the given key if it exists in
# marks.pop("harry") # removes the key value pair for the given key and returns the value of that 
# print(marks) # remove harry from the dictionary
# marks.popitem() 
# print(marks) # remove the last item from the dictionary
# print(marks.len)

#sets it is a collection of unique elements it is unordered and mutable data type
# e= set() # empty set
# marks= {22, 44, 56, 7, 7,22, "aniket"} # set not consider the repeated no.
# print(marks) 
# marks.add(4545) # add an element to the set
# print(marks)
# marks.remove(22) # remove an element from the set
# print(marks) # {44, 56, 7, 4545, 'anik
# print(marks.clear()) # remove all elements from the set


# s1={45,55,8,99,67,43,90}
# s2={99,55,88,45,67}
# print(s1.union(s2)) # returns a new set with elements from both sets not repeated no.

# print(s1.intersection(s2)) # returns a new set with elements common to both sets
# print(s1.difference(s2)) # returns a new set with elements in s1 but not
# print(s1.issubset({22,45})) # returns True if all elements of s1 are present in the given set else returns False
# print(s1.issuperset({8,45})) # returns True if all elements of th



#practice que1

# que= {
#     "madad": "help",
#     "kursi": "chair",
#     "dabba": "box",
# }
# inp= input("enter the word: ") # input the word
# print(que[inp]) # print the meaning of the word
# print(que["madad"])
# print(que.keys())
# print(que.values())
# print(que.items())
# que["kursi"]="table" # update the value of the key
# print(que)
# que["aniket"]="aniket" # add a new key value pair
# print(que)

# que 2  make a diractory by taking input and print the diractory
# s= set()
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# n=int(input("enter the number of elements: "))
# s.add(int(n))
# print(s)

# que 3
# l= (5,6,9,88)
# print(len(l))


#que 4
#take input from user and print 
# s={}

# inputs= input("enter the name: ")
# name= input("enter the language: ")
# s.update({inputs:name})

# inputs= input("enter the name: ")
# name= input("enter the language: ")
# s.update({inputs:name})

# inputs= input("enter the name: ")
# name= input("enter the language: ")
# s.update({inputs:name})

# inputs= input("enter the name: ")
# name= input("enter the language: ")
# s.update({inputs:name})
# print(s)

