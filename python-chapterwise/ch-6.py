#conditional -statement

# a= int(input("Enter your age: "))

# if(a>=18): # if the age is greater than or equal to 18
#     print("You are eligible to vote")
#     print("Make sure you have your voter id card with you")

# elif(a<0): #elif the age is less than 0
#         print("Invalid age")
#         print("sahi se age daalo")
# elif(a==0): #elif the age is equal to 0
#      print("you are a baby")
# else: #if the age is between 0 and 18
#     print("You are not eligible to vote")
#     print("Abhi munna hai tu")


#practice que 1

# a=int(input("enter the no. :"))
# b=int(input("enter the no. :"))
# c=int(input("enter the no. :"))
# d=int(input("enter the no. :"))
 
# if(a>b and a>c and a>c):
#     print(a)
# elif(b>a and b>c and b>d):
#     print(b)
# elif(c>a and c>b and c>d):
#     print(c)
# else:
#     print(d)
   
#que 2
# marks1=int(input("ENTER YOUR MARKS: "))
# marks2=int(input("ENTER YOUR MARKS: "))
# marks3=int(input("ENTER YOUR MARKS: "))

# mark_per= 100*((marks1 + marks2 + marks3))/300


# if(mark_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you are pass", mark_per)
# else:
#     print("you are fail", mark_per)

#que3
# spam=input("enter your msg: ")

# if(spam=="make a lot of money" or spam=="buy now" or spam== "click here"):
#     print("this is spam")
# else:
#     print(spam)


#que 4

# s= input("enter your name: ")
# if(len(s)<10):
#     print("your name is short")
# else:
#   print("your name is long")


#que 5
# l=["aniket", "rahul", "sachin", "saurav", "dhoni"]
# inp= input("enter your name: ")
# if(inp in l):
#     print("you are a cricketer")
# else:
#     print("you are not a cricketer")

#que 6

name=input("post: ")
if("aniket".lower() == name.lower()):
    print("this is talking about aniket")
else:
    print("this is not talking about aniket")