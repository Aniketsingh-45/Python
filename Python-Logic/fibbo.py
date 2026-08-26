
a=0
b=1
num=int(input("enter a no.: "))

if num==1:
    print(a)

else:
  print(a)
  print(b)
  for i in range(2, num):
    c=a+b
    a=b
    b=c
    
    print(c)



def fibbo(num):
  if num==0:
    return 0
  elif num==1:
    return 1

  else:
    return fibbo(num-1)+fibbo(num-2)

term=int(input("enter the no.: "))

sum=0

for i in range (term):
  num=fibbo(i)
  print(num, end="  ")
  sum=sum+num

print("\n\nsum of fibbo: ",sum)

