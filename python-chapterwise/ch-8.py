#function

# def add():  # function definition
#     a=int(input("enter the no."))
#     b=int(input("enter the no."))
#     c=a+b
#     print(c)

# add() #function call
# print("adding")
# add()


# def fun(name, end): #() is used to pass arguments 
#     print("good day " + name) # function definition
#     print(end)
# fun("aniket", "happy")
# fun("ayush", "good") # function call


# recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
    

# n= int(input("enter the no. "))    

# print(f"the factriol of {n} is {fact(n)}")


# practice que 1

# a= int(input("enter the no. "))
# b= int(input("enter the no. "))
# c= int(input("enter the no. "))

# def find(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>c and b>a):
#         return b
#     else:
#         return c
# print(f"The largest numer is: {find(a,b,c)}")



# que 2
# f= int(input("enter the farenhiet: "))
# def celcius(f):
#     return 5*(f-32)/9
# print(f"the temperature is: {celcius(f)}")


# que 3
n= int(input("enter the no. "))
def add(n):
    if (n == 0 or n == 1):
        return n
    else:
        return add(n-1)+n
print(f"the sum of {n} is {add(n)}")
    
