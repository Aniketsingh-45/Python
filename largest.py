a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))

if a>b and a>c:
    print(f"{a} is a largest no.")

if b>a and b>c:
    print(f"{b} is largest no.")

if c>a and c>b:
    print(f"{c} is a largest no.")