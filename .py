print("Welcome to Affan's Assistant!!!")
print("If you need help type 'help'")
quit = False
while not quit:
    command = input(">")
    if command.lower() == "quit":
        quit = True
        print("Program Ended")
    elif command.lower() == "help":
        print("""
        help - find commands for affan's assistant
        calculate - to use a calculator
        smack - to smack ammaar and zayaan if you do this the program will end  at the end.
        Secret Project - enter a password to enter this program!""")
    elif command.lower() == "secret project":
        password = input("Enter the Password:")
        if password.lower() == "qwerty":
            print("Ammaar is a good doggy!!")
            quit = True


        else:
            print("Wrong Password TRY AGAIN!!!")
    elif command.lower() == "smack":
        quit = True
        smack = input("Who Shall you hit Ammaar or Zayaan?")
        if smack.lower() == "ammaar":
            print("Ammaaar is a good doggy!")
        if smack.lower() == "zayaan":
            print("Zayaan is a good doggy!")
    elif command.lower() == "calculate":
        cal = input("Enter (a)dd,(s)ubtract,(m)ultiply, and (d)ivide: ")
        if cal.lower() == "a":
            var1 = int(input("Enter the first Variable:"))
            var2 = int(input("Enter the second Variable:"))
            print(f"The solution is {var1+var2}")
        if cal.lower() == "s":
            var1 = int(input("Enter the first Variable:"))
            var2 = int(input("Enter the second Variable:"))
            print(f"The solution is {var1-var2}")
        if cal.lower() == "m":
            var1 = int(input("Enter the first Variable:"))
            var2 = int(input("Enter the second Variable:"))
            print(f"The solution is {var1*var2}")
        if cal.lower() == "d":
            var1 = int(input("Enter the first Variable:"))
            var2 = int(input("Enter the second Variable:"))
            print(f"The solution is {var1/var2}")
    else:
         print("Type help to get a list of commands!!!")