# A car game
car_task = ''
started = False

while True:
    car_task = input("> ").lower()
    if car_task == 'start':
        if started:
            print("Car is already started!, don't burn my Kick starter")
        else:
            started = True
            print("Car Started...")
    elif car_task == "stop":
        if not 'started':
            print('Sorry, Car is already stopped')
        else:
            started = False
            print('car Stopped')
    elif car_task == "help":
        print('''
Start - To Start the car
stop - To stop the car
quit - To quit the game
''')
    elif car_task == "quit":
        break
    else:
        print("Sorry, I don't Know what you want me to do")