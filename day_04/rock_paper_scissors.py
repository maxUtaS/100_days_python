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

chose_list = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)

user_choice_int = int(user_choice)
if(user_choice_int < 0 or user_choice_int >= 3 ):
  print("You typed an invalid number, you lose!")
else:
  choice1 = chose_list[user_choice_int]
  choice2 = chose_list[computer_choice]
  print(f"{choice2} \n Computer chose.")
  print(f"{choice1} \n Your chose.")

  if user_choice_int >= 3 or user_choice_int < 0: 
      print("You typed an invalid number, you lose!") 
  elif user_choice_int == 0 and computer_choice == 2:
      print("\t!!!You win!!!")
  elif computer_choice == 0 and user_choice_int == 2:
      print("\t!!!You lose!!!")
  elif computer_choice > user_choice_int:
      print("\t!!!You lose!!!")
  elif user_choice_int > computer_choice:
      print("\t!!!You win!!!")
  elif computer_choice == user_choice_int:
      print("It's a draw")
