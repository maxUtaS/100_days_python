age = input("What is your current age?")

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
year = 90 - int(age)
day = round(year * 365)
week = round(year * 52)
month = round(year * 12)

message = f"You have {day} days, {week} weeks, and {month} months left."
print(message)