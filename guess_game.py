import random 

num1 = int(input("Enter your minimum value:"))
num2 = int(input("Enter your maximum value: "))

if num1 >= num2:
  print("Maximum value can't be greater than or equal to minimum value")

attempt = 0
rand = random.randrange(num1, num2)

while attempt != 3:
  guessedNum = int(input(f"guess your number between {num1} to {num2}:"))
  if guessedNum == rand:
    print("You nailed it")
    break
  else:
    if guessedNum > rand:
      print("Too high!")
    elif guessedNum < rand:
      print("Too low")
    attempt += 1
else:
  print(f"You couldn't guess the number! It's {rand}")