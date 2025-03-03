# simple car game using if else elif

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
  if command == "/start":
    if isStarted:
      print("car's already started!")
    else:
      print("car started!")
      isStarted = True
  elif command == "/stop":
    if isStarted:
      print("car stopped!")
      isStarted = False
    else:
      print("car's already stopped!")
  elif command == "/exit":
    print("Successfully left the game!")
    break
  elif command == "/help":
    print(helpMsg)
  else:
    print("command not found!")
