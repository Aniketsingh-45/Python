while True:
 num=int(input("enter a no. to check a prime or not: "))

 if num==1:
    print("number is not prime")

 if num>1:
    for i in range(2, num):
       if num%i==0:
           print("not prime")
           break
    else:
           print("prime")



lst=[10,20,30,40]
product=1

for ele in lst:
    product*=ele

print(product)
