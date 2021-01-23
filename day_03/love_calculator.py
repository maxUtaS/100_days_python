
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count1 = 0
count2 = 0
combined_string = name1 + name2
lower_case_string = combined_string.lower()

# T
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

count1 = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")

count2 = l + o + v + e

love_less = int(str(count1) + str(count2))

if(love_less < 10 or love_less > 90):
  print(f"Your score is {love_less}, you go together like coke and mentos.")
elif(love_less >= 40 and love_less <= 50):
  print(f"Your score is {love_less}, you are alright together.")
else:
  print(f"Your score is {love_less}")