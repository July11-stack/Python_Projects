i = 0;
while i < 10:
    begin = input(">")
    if begin == "help":
        print('''
    start - to start the car
    stop - to stop the car
    quit - to exit
    guess - play a guess game
    ''')
    elif begin.lower() == "quit":
        print("Program has ended!")
        break
    elif begin.lower() == "start":
        print("Car started...")
    elif begin.lower() == "stop":
        print("Car stopped")
    elif begin.lower() == "guess":
        count = 0
        while count < 5:
            guess = int(input("Enter your guess: "))
            zaid = 9
            count+=1
            if(zaid==guess):
                print("You won the game!")
                break
            if(count == 5):
                print("You lost the game!")


    else:
        print("Enter help for commands!")
#Before I had put everything as a If statement instead of elif so it gave a error and kept on printing out "Enter help for commands!" I fixed it by putting elif for each statement after the first one keep this in mind!!!

