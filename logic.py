c=0
def myfun():
    global c

    print("hello", c)
    c=c+1
    myfun()
    print("hii")

  


myfun()


def fact(num):
  if num==0 and num==1:
    return 1
  else:
    return num*fact(num-1)

num=int(input("enter the no: "))
print(fact(num))

