import random

print("this is part of DailyTask") 

Rock="""
    _______
---'   ____)
      (_____)
      (Rock_)
      (____)
---.__(___)
"""
Paper="""
     _______
---'    ____)____
           ______)
          _Paper_)
         _______)
---.__________)
"""
Scissors="""
    _______
---'   ____)____
          ______)
       _Scissors_)
      (____)
---.__(___)
"""

user_choice=input("what do  you choose? type 0 for Roke, 1 for Paper and 2 for Scissor : \n")
computer_choice=random.randint(0,2)

print(f"computer chose {computer_choice}")

if user_choice >=3 or user_choice <0:
    print("invalid number ")
elif user_choice ==0 and computer_choice ==2:
    print("user Win")
elif computer_choice ==0 and user_choice ==2:
    print("you lose")

elif computer_choice > user_choice:
    print("you lose")
elif computer_choice > user_choice:
    print("you win")
elif computer_choice == user_choice:
    print("It's drow!")



print("Dode")