#object oriented programming/oop

# class student: # class is used to define a class 
#     language="hindi" # class variable, can be accessed by all instances of the class
#     salary= 50000
#     rank="top"

# aniket= student() # object is used to create an object of a class
# aniket.name= "Aniket" # we can add new attributes to an object
# aniket.language= "english" # we can also change the class variable value for an object
# print(aniket.language,aniket.name, aniket.salary) # accessing the attributes of a class using object

# rahul=student() # creating another object of the same class
# print(rahul.language,rahul.salary, rahul.rank) # accessing the attributes of a class using object



# class emplyoe:
#     language="python"
#     salary=50000
#     exp= " 5 years"

#     def getInfo(self): # self is a reference to the current instance of the class and is used to access variables that belongs
#       print(f"the language is {self.language}.THE SAlary is {self.salary}. THE EXPERIENCE IS {self.exp}")

#     @staticmethod  #static method is used to define a static method in a class
#     def greet(): # this is a static method, it does not take any instance of the class as an argument
#        print("hello, welcome to the company")

# aniket=emplyoe()
# aniket.getInfo() # calling the method using object
# aniket.greet() # calling the method using object

# rahul=emplyoe()
# rahul.name="rahul"
# print(rahul.name)
# rahul.getInfo()

# class students():
#        roll= 23
#        marks=98
#        subject="maths"
      
#        def __init__(self, roll,subject,marks): # this is a dunder method in python which is automatically called when an object is created from a class
#         self.roll=roll
#         self.subject=subject
#         self.marks=marks
#         print("i am a student")



#         def getInfo(self):
#             print(f"the roll is {self.roll}. THE MARKS IS {self.marks}")
#         @staticmethod
#         def greet():
#             print("hello, welcome to the school")
            
# aniket=students(45,"science",8)
# print(aniket.subject, aniket.roll,aniket.marks)


# que1
# collecting data of programmer
# class progammer:
#     company="microsoft"

#     def __init__(self, name,age, salary):
#         self.name= name
#         self.age=age
#         self.salary=salary

# p=progammer("Aniket", 25,10000)
# print(p.name,p.company,p.salary,p.age)
# r=progammer("rohan", 25,10000)
# print(r.name,r.company,r.salary,r.age)

#que 2
#make calculator

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"square of no. is: {self.n*self.n}")  
#     def cube(self):
#         print(f"cube of no. is: {self.n*self.n*self.n}")  
#     def squareroot(self):
#         print(f"squareRoot of no. is: {self.n*1/2}")  

# p= calculator(9)
# p.square()
# p.cube()
# p.squareroot()

#que 3
#show ticket booking

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"ticket is booked from trainNo.{self.trainNo} from {fro} to {to}")
    def get(self):
        print(f"trainNo.{self.trainNo} is available")
    def getFare(self,fro,to):
        print(f"fare of trainNo.{self.trainNo} from {fro} to {to}")


t=train(2456)
t.book("delhi", "mumbai")
t.get()
t.getFare("delhi", "mumbai")