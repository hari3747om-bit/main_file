play_game= input('Do you want to play the game? Yes or no').lower()
count_start=0
count_stop=0
if play_game=='yes':
    while  True:
        initiate=input('>').lower()
        if initiate=='start':
            count_start+=1
            count_stop=0
            if count_start>1:
                print('The car is already started')
            elif count_start==1:
                print('The car is started')
        elif initiate=='stop':
            count_stop+=1
            count_start=0
            if count_stop>1:
                print('The car is already stopped')
            elif count_stop==1:
                print('The car is stopped')
        elif initiate=='help':
            print("""
Start: to start the car
Stop: to stop the car
Quit: to quit the game
                  """)
        elif initiate=='quit':
            break
elif play_game=="no":
    print('Have a nice day')