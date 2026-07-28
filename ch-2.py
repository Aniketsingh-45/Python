# DataTypes
a= 1; #a is a integer
t=type(a) #t is a type object which is use to check the type of a
print(t)
k=float(a) #float () function is used to convert the integer into a float
print(k)

b=3.666; #b is a float
t=type(b)
print(t)
k=int(b) #int() function is used to convert the float into an integer
print(k)

c= "aniket"; #c is a string
t=type(c)
print(t)

d= False; #d is a boolean
t=type(d)
print(t)

e=None; #e is None type
t=type(e)
print(t)


# Operators
print(not(True));# prints False USING NOT OPERATOR
print(5>4 & 5<4);# prints True USING AND OPERATOR : AND = "&" IF BOTH CONDITIONS ARE TRUE THEN IT WILL RETURN TRUE ELSE FALSE
print(2>1 | 8<6); # prints True USING OR OPERATOR : OR = "|" IF ANY OF THE CONDITIONS ARE TRUE THEN IT WILL RETURN TRUE ELSE FALSE

#assignment operators
x=5; #initializing x with 5
x+=3; #x is now 8
print(x)

#input function
a= input("enter the no.")
n=input("enter 2nd no.")
print(a+n) #prints the string of a and n , if i take a=5; b=5 then it will print 55

a= int (input("enter the no."))
b=int (input("enter 2nd no."))
print(a+b)  #prints the sum of a and b using int() function


#practice que 2
a= int(input("enter 1st no. :"))
b= int(input("enter 2nd no. :"))
print("remainder of a/b =",a%b)


#find average of two no.

a= int(input("enter 1st no. :"))
b= int(input("enter 2nd no. :"))
c=(a+b)/2
d= a**3
print("average of a and b =",c,d)