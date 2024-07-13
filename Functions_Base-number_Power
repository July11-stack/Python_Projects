def square(num, pow):
    result = num ** pow
    print(result)


def quit(num):
    if num.lower() == "quit":
        print("Program ended")


def quit2(pow):
    if pow.lower() == "quit":
        print("Program Ended Error 101!")



num = input("Enter the Base Number:")  # Allow input as string to handle "quit"
quit(num.lower())  # Call quit function with lowercase num

if num.lower() != "quit":
    num = int(num)  # Convert num to int if not "quit"
    pow = input("Enter the power:")  # Allow input as string to handle "quit"
    quit2(pow.lower())  # Call quit2 function with lowercase pow

    if pow.lower() != "quit":
        pow = int(pow)  # Convert pow to int if not "quit"
        square(num, pow)  # Call square function with num and pow
