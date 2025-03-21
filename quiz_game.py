def quiz(question, options, answer): 
    attempt = 0
    print(question)
    for opt in options: 
        print(opt, end = "\t")
    while attempt <= 5:
        usersAnswer = input("Enter your answer: ")
        if usersAnswer in answer: 
            print("You nailed it!")
            break
        else:
            print("Try again!")
            attempt += 1
    else:
        print("Max attempt reached!")


def main(): 
    # quiz 1
    print("Answer the quiz no 1")
    quiz("Who's the father of algorithm?", ("Al khawarejmi", "Newton", "Einstein", "Libnez"), "Al khawarejmi")



if __name__ == "__main__": 
    main()
    
