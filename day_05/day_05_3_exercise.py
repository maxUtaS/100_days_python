sum_numbers = 0
for number in range(1, 101):
  if(number % 2 == 0):
    sum_numbers += number
print(sum_numbers)

total = 0
for number in range(2, 101, 2):
  total += number
print(total)