# simple car game using match case
helpMsg = """/start -- to start the car
/stop -- to stop the car
/help -- to print this message 
/exit -- to leave the game """
isStarted = False

print(f"""
car game started
---------------------------------------------
{helpMsg}
---------------------------------------------
""")

while True:
  command = input(">> ")
  match command: 
    case "/start":
      if isStarted:
        print("car's already started!")
      else:
        print("car started!")
        isStarted = True
    case "/stop":
      if isStarted:
        print("car stopped!")
        isStarted = False
      else:
        print("car's already stopped!")
    case "/exit":
      print("Successfully left the game!")
      break
    case "/help":
      print(helpMsg)
    case _:
      print("command not found!")
