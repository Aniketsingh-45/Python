# for open a file
# f= open("file.txt") # open is used to open the file
# data= f.read() # read is used to read the data from the file
# line=f.readlines() # readline is used to read the data from the file line by line
# print(line,type(line) ) # print the data and its type
# print(data)
# f.close() # close is used to close the file, if you open a file, you must close it, otherwise, it will be locked and you can't open it


# for write and make a file

# str="MY NAME IS ANIKET SINGH \n I M FAN OF ROHIT SHARMA" # string is used to store the data
# f=open("myfile.txt", "w") # open is used to open the file, w is used to write the data in the file
# f.write(str) # write is used to write the data in the file
# f.close()

# file print in loop
# f= open("file.txt")
# line= f.readline()
# while(line != ""): # while loop is used to print the data in the file line by line
#     print(line)
#     line=f.readline() # readline is used to read the data from the file line by line

# f.close()

# f=open("file.txt")
# print(f.read())
# f.close()
# the same can we written using with statement 

# with open("file.txt")as f: # as is used to assign the file object to the variable f
#     print(f.read())  # with statement is used to open the file and close it automatically, not need to close it manually


# practice que1

# f=open("file.txt")
# content=f.read()
# if("twinkel" in content): #if is used for check twinkel is present in file or not
#     print("yes it contain twinkel")
#     print(content)
# else:
#     print("not content")

#que 2

# def generateTable(n):
#     table= ""
#     for i in range(1,11):
#         table += f"{n} x {i}= {n*i}\n"
#     with open(f"tables/table_{n}.txt","w") as f:
#      f.write(table)

# for i in range(2,28):
#     generateTable(i)


# que 3

word= ["chor", "harami", "kutta", "suar"]
with open("file.txt")as f:
    content=f.read()
    for i in word:

     content= content.replace(i, "#"*len(i)) # replace is used to replace the word with new word

with open("file.txt", "w")as f:
    f.write(content)  # w is used to write the data in the file