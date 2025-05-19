# emoji set
emojis = {
    ":)": "🙂",
    ":(": "😔",
    "<3": "❤️",
    ":0": "😱",
    ":-|": "😐",
    "B-)": " 😎",
    "^⁠_⁠^": "😄",
    ":-3": "😙",
    ":⁠-⁠D": "😆",
    "(-:": "🙃",
    "-_-": "😑"
}
# emoji decoder 
def decode_emoji(inp_str):
    lst = inp_str.split(" ") # split the input 
    for i in range(len(lst)):
        # run a for loop, if item is found in emoji dict convert it to emoji 
        if lst[i] in emojis:
            lst[i] = emojis[lst[i]]
    return "".join(lst) # return a string joining the list

while True:
    choice = input("Enter your message or /q to quit the problem: ")
    if choice == "/q": 
        break
        quit()
    else:
        print(decode_emoji(choice))