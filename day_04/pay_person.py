import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#names_len = len(names) - 1

#ran_index = random.randint(0, names_len)
pay_person = random.choice(names)

print(f"{pay_person} is going to buy the meal today!")


