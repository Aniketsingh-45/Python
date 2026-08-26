# '''
# for rock you type: "r" 
# for paper you type: "p"
#  for scissors you type: "s"

# '''
# # import random
# computer= random.choice(["r", "p", "s"])
# user = input("Enter a choice (Rock: r ,Paper: p, scissor: s): ").lower()
# print(f"\nComputer chose: {computer}, you chose: {user}\n")


# if (user == computer):
#     print("Match draw")
# else:
#      if(user== "r" and  computer=="s"):
#        print("YOU WIN!!")
#      elif(user=="r" and computer=="p"):
#           print("YOU LOSE!!")
#      elif(user=="p" and computer=="r"):
#           print("YOU WIN!!")
#      elif(user=="p" and computer=="s"):
#           print("YOU LOSE!!")
#      elif(user=="s" and computer=="p"):
#          print("YOU WIN!!")
#      elif(user=="s" and computer=="r"):
#          print("YOU LOSE!!")
#      else:
#          print("Invalid input")
         
         
import random
while True:
    computer = random.choice(["r", "p", "s"])
    user = input("Enter a choice (Rock: r, Paper: p, Scissor: s) or 'q' to quit: ").lower()
    if user == 'q':
        print("Thanks for playing!")
        break
    if user not in ["r", "p", "s"]:
        print("Invalid input. Please enter r, p, or s.")
        continue
    if user == computer:
        print("Match draw")
    elif user == "r" and computer == "s":
        print(f"YOU WIN!! Computer chose: {computer}, you chose: {user}")
    elif user == "r" and computer == "p":
        print(f"YOU LOSE!! Computer chose: {computer}, you chose: {user}" )
    elif user == "p" and computer == "r":
        print(f"YOU WIN!! Computer chose: {computer}, you chose: {user}")
    elif user == "p" and computer == "s":
        print(f"YOU LOSE!! Computer chose: {computer}, you chose: {user}")
    elif user == "s" and computer == "p":
        print(f"YOU WIN!!  Computer chose: {computer}, you chose: {user}")
    elif user == "s" and computer == "r":
        print(f"YOU LOSE!! Computer chose: {computer}, you chose: {user}")
