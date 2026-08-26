#strings

a= "aniket"
change=a[0:4]   #[] operator is used to get the substring of a string, 0 :4 means from index 0 to 4 
print(change)
len= len(a)  #len() function is used to get the length of a string
print(len)
c=a[3] #a[3] means get the character at index 3
print(c)
print(a[-6:-3]) #a[-6:-3] means get the substring from index -6 to -3, consider -1 as last index

#string function
name= "Rohit Sharma"
print(name[1:4:2]) #a[1:4:2] means get the substring from index 1 to 4  
print(name.endswith("lo")) #a.endswith("lo") means check if the string ends with "lo"
print(name.startswith("Ro")) #a.startswith("Ro") means check if the string starts with "Ro"
print(name.upper()) #a.upper () means convert the string to upper case
print(name.lower()) #a.lower() means convert the string to lower case
replace= name.replace("Sharma", "Singh") #a.replace("Sharma", "Singh") means replace "Sharma
print(replace)

line= "I love python programming\n it\tis \"fun\"" #\n means new line, \t means tab, \" means double quote
print(line)


#practice que1
b=input("enter your name:");
print(f"Good morning {b}") #f string is used to insert the value of a variable inside a string

#que2
letter= '''dear <|name|>,
           you are selected!
           <|date|>'''
print(letter.replace("|name|","Aniket").replace("|date|","22-12-2024")) # REPLACE () function change the value of a string to another string

#que3
name= "Rohit  Sharma"
print(name.find("  "))  #find() function is used to get the index of a substring in a string
print(name.replace("  ", " ")) #replace() function is used to replace a substring in a string with another substring