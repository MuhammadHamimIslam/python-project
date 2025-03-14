helpMsg = """/balance -- to check the balance
/deposit -- to deposit money 
/withdrawal -- for money withdrawal 
/help -- to print this message 
/exit -- to leave the game
"""
balance = 0 # initial balance is 0

def deposit(): # function for deposit 
  global balance
  amount = int(input("Enter your amount: "))
  balance += amount 
  return f"{amount} is deposited to your account!"
  
def withdrawal(): # function for withdrawal 
  global balance # make balance to global 
  amount = int(input("Enter your amount: "))
  if balance < amount : return "Not enough money for withdrawal"
  else: # if sufficient money then withdrawal will be proceed 
    balance -= amount 
    return f"{amount} was taken as withdrawal"

print(helpMsg)

while True:
  command = input(">>")
  match command: 
    case "/balance":  print(f"Your current balance is: {balance}")
    case "/deposit": 
      print(deposit())
    case "/withdrawal": 
      print(withdrawal())
    case "/help": print(helpMsg)
    case "/exit": break
    case _: print("command not found!")
  