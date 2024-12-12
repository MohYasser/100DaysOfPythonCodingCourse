import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#----------------------------------------------------
array=[rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

user_num=int(input())
while not (user_num==0 or user_num==1 or user_num==2):
    print("Please enter a valid number")
    user_num = input()

computer_num = random.randint(0,2)

print(array[user_num])
print("Computer chose: \n")
print(array[computer_num])

if(user_num==0 and computer_num==2) or (user_num==1 and computer_num==0) or (user_num==2 and computer_num==1):
    print("You win!")
elif (user_num==0 and computer_num==0) or(user_num==1 and computer_num==1) or (user_num==2 and computer_num==2):
    print("It's a draw")
else:
    print("You lose")














