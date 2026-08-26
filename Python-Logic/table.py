num=int(input("enter a number to find table: "))

for i in range(1, 11):
    print(f"{num} x {i}= {num*i}")


#by while loop

num=int(input("enter a number to find table: "))
 
i=1

while i<=10:
    print(f"{num} x {i}= {num*i}")
    i+=1
