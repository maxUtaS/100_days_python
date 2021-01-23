import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Get the total number of items in list.
num_items = len(names)

#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)

#Pick out random person from list of names using the random number.
pay_person = names[random_choice]

print(f"{pay_person} is going to buy the meal today! ")