import random
ask_user=input('Do you want to play the game>? , Y:yes,N:no')
chutiya_user= ask_user.strip().lower()
while True:
    if chutiya_user=='n':
     print('Have a nice day')
    elif chutiya_user=='y':
        secret_number= random.randint(1,100)
        guess_amount=0
        while guess_amount<10:
           guess_number= int(input('Guess:\t'))
           guess_amount+=1
           if guess_number== secret_number:
                print('You Won!!')
                break
           elif guess_amount<10:
                if guess_number<secret_number:
                    print('Try guessing a bit higher')
                else:
                    print('Try guessing a bit lower')
           elif guess_amount==10:
                print('You lost', "\n correct number was" ,secret_number)
                break
    try_again=input('Do you want to play again? Y:yes,N:no')
    if try_again.lower() == 'y':
       continue
    elif try_again.lower() == 'n':
       break
print('You took',guess_amount,'attempts')