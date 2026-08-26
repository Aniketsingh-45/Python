# while loop
# i=1
# while(i<=10):
#     print(i)
#     i=i+1;

# l= [34, "aman", "aniket", 56, 88.8]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i=i+1;


# for loop

# i=1;
# for i in range(1,11):
#     print(i);

# for i in range(10): # for loop with range function range (10) generates numbers from 0 to 9 start 0,9
#     print(i);

# for i in range(0,50,4): # for loop with range function range (0,50,4) and start 0 to 50 and step 4 
#     print(i); # for loop with range function range (0,50,4) generates numbers

# l=[11,56,77,88]
# for i in l:
#     print(i) # for loop with list and print each element of list

# t=(66,99,7,"aniket")
# for i in t:
#     print(i) # for loop with tuple and print each element of tuple

# s="aniket"
# for i in s:
#     print(i) # for loop with string and print each character of string

#for loop with else
# a=[11,98,78,"aniket"]

# for i in a:
#     print(i);
# else:
#     print("aniket in list"); 

#for loop witn break and continue

# for i in range(1,50):
#     if(i==23):
#         break # break use for exit the loop
#     print(i) # for loop with break and print no. to 22


# for i in range(30):
#     if(i==23):
#         continue # continue use for skip the current iteration
#     print(i) # for loop with continue and print all no. except 23

# pass method

# for i in range(1,50):
#     pass  # pass use for do nothing in loop

# i=0
# while(i<45):
#     print(i) # while loop with print all no. from 1 to 44
#     i=i+1;



# practice que 1

# a= int(input("enter the number: "))

# for i in range(a,a*11,a):
#     print(f" {a} x {i}=",i);
# #another way to solve this problem

# a=int(input("enter the number: "))
# for i in range(1,11):
#    print(f"{a} x {i}= {a*i}") # f string use for print the string with variable value

# a=int(input("enter the number: "))
# i=1;
# while(i<11):
#     print(f" {a} x {i} = {a*i}")
#     i=i+1; # while loop with print all multiplication of number from 1 to 10

# practice que 2
# l=["aniket", "rohan", "ayush", "saurav"]

# for i in l:
#     if(i.startswith("a")):
#         print(f"hello {i}"); # for loop with print hello to all name start with a

# practice que 3

# a= int(input("enter no."))

# for i in range(2,a):
#     if(a%i==0):
#         print("no. is not prime")
#         break
# else:
#   print("number is prime") # for loop with check the number is prime or not

# practice que 4

# n = int(input("enter no. "))
# total = 0
# i = 1
# while (i <= n):
#     total += i
#     i = i + 1
# print(total)

# practice que 5

# n = int(input("Enter a positive integer: "))
# f=1
# for i in range(1, n+1):
#         f = f * i
# print(f"The factorial of {n} is {f}")

# practice que 6
# n = int(input("Enter a positive integer: "))
# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
    # print("")

# practice que 7
# n = int(input("Enter a positive integer: "))
# for i in range(1, n+1):
#      print("*" * i, end="")
#      print("")

# practice que 8
# n = int(input("Enter a positive integer: "))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#      print("*" * n)
#     else:
#        print("*", end="")
#        print(" " * (n-2), end="")
#        print("*", end="") # end =" " to print on same line
#        print("")
    

#practice que 9
n = int(input("Enter a positive integer: "))
for i in range(1, 11):
    print(f"{n}X{11-i}= {n*(11-i)}")
    
