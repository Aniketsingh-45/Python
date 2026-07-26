lower=int(input("enter range start: "))
upper= int(input("enter range end: "))

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break
        else:
            print(num)