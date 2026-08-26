#que 1

a=int(input("enter THE length:"))
b=int(input("enter the breadth:"))
area=a*b
parimeter=2*(a+b)
print("area of rectangle is",area)
print("perimeter of rectangle is",parimeter)


#que 2

x=int(input("radius of circle"))
area=3.14*x**2
peri=3.14*2*x
print("area of circle is",area)
print("perimeter of circle is",peri)


#que 3

h=int(input("enter hour: "))
m=int(input("enter minute: "))
s=int(input("enter second: "))

second= h * 3600 + m * 60 + s
print("total second is",second)
