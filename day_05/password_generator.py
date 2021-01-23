#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# list with letters, numbers and symbols
passwort_list = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# random letter
user_passwort = ""

#for index in range(0, nr_letters):
#  letter = random.randint(0, len(letters) - 1)
#  user_passwort += passwort_list[0][letter]
#  rand_position = random.randint(0, len_passwort - 1)

# random symbol
#for index in range(0, nr_symbols):
#  symbol = random.randint(0, len(symbols) - 1)
#  user_passwort += passwort_list[1][symbol] 
# random numbers
#for index in range(0, nr_numbers):
#  number = random.randint(0, len(symbols) - 1)
#  user_passwort += passwort_list[2][number]

#print(f"Eazy Level {user_passwort}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#easy_passwort = ""
#for index in range(0, nr_letters):
#  letter = random.choice(letters)
#  easy_passwort += letter
#for index in range(0, nr_symbols):
#  symbol = random.choice(symbols)
#  easy_passwort += symbol
#for index in range(0, nr_numbers):
#  number = random.choice(numbers)
#  easy_passwort += number

#print(easy_passwort)


hard_passwort = []
for index in range(0, nr_letters):
  letter = random.choice(letters)
  hard_passwort.append(letter)
for index in range(0, nr_symbols):
  symbol = random.choice(symbols)
  hard_passwort.append(symbol)
for index in range(0, nr_numbers):
  number = random.choice(numbers)
  hard_passwort.append(number)
# print ', '.join(mylist)
print(''.join(hard_passwort))

random.shuffle(hard_passwort)
passwort = ""
for char in hard_passwort:
  passwort += char
print(f"Your hard passwort is {passwort}")