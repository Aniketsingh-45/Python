num=int(input("enter the number: "))


temp=num
count=0

while temp>0:
    
    digit=temp%10
    count+=1
    temp=temp//10

temp=num
total=0

while temp>0:
    digit=temp%10
    total=total+digit**count
    temp=temp//10

if total==num:
    print("armstrong no. ")

else:
    print("not")
    



