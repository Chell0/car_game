command = ""
started = True
# stopped = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        # check to see if the car is already started
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        # check if the car is already stopped
        # if stopped:
        if not started:
            print("Car is already stopped!")
        else:
            # stopped = True
            started = False
            print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't know what that is :(")

