num= int(input("Enter the no.: "))
fact=1
if num<0:
    print("no. is negative")
 
if num==0 or num==1:
    print(1)

if num>1:
    for i in range(1, num+1):
        fact=fact*i

    print(fact) 

#by recursion

def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)

num= int(input("Enter the no.: "))

factorial=fact(num)
print(factorial)



def fact(num):
    if num==0 and num==1:
        print(1)

    elif num>1:
        fact=1
        for i in range(1, num+1):
            fact=fact*i

        print(fact)

num= int(input("Enter the no.: "))
fact(num)