from random import randint
def printMessage():
    print("WELCOME TO ROCK, PAPER AND SCISSORS")
    print("1. Play the Game")
    print("2. Learn how to play")
    print("3. Exit")
def winner(player,computer):
    if(player=='Rock'):
        if(computer=='Rock'):
            print("Computer chose rock, it is a tie!")
            return 0
        elif(computer=='Paper'):
            print("Compuer chose paper, computer won!")
            return -1
        else:
            print("Computer chose scissors, you won!")
            return 1
    elif(player=='Paper'):
        if(computer=='Rock'):
            print("Computer chose rock, you won!")
            return 1
        elif(computer=='Paper'):
            print("Computer chose paper, it is a tie")
            return 0
        else:
            print("Computer chose scissors, computer won!")
            return -1
    elif(player=='Scissors'):
        if(computer =='Rock'):
            print("Computer chose rock, computer won!")
            return -1
        elif(computer =='Paper'):
            print("Computer chose paper, you won!")
            return 1
        else:
            print("Computer chose scissors, it is a tie")
            return 0
def computerChoose():
    number=randint(1,3)
    if(number==1):
        return 'Rock'
    elif(number==2):
        return 'Paper'
    else:
        return 'Scissors'
def main():
    player_points=0
    computer_points=0
    player_choice=input("Make your choice (Rock/Paper/Scissors)\n")
    computer_choice=computerChoose()
    b=True
    while(b):
        change=winner(player_choice,computer_choice)
        if(change==1):
            player_points+=1
        elif(change==-1):
            computer_points+=1
        print("Player points= "+str(player_points)+" computer points= "+str(computer_points))
        if(player_points==3 or computer_points==3):
            break
        else:
            player_choice=input("Make your choice (Rock/Paper/Scissors)\n")
            computer_choice=computerChoose()
    if(player_points==3):
        print("CONGRATULATIONS, YOU WON!!")
    else:
        print("COMPUTER WON!!")
        
choice=0
while(choice!=3):
    printMessage()
    choice=int(input("Choose between (1/2/3)\n"))
    if(choice==1):
        main()
    elif(choice==2):
        print("When prompted you enter your choice, whether it is Rock, Paper or Scissors. The computer makes its choice at the same time. Then the winner is displayed. The one who reaches 3 points first, WINS!!")
    elif(choice==3):
        print("Thank You for playing with us")
    else:
        print("Invalid Choice, choose between (1/2/3)")
