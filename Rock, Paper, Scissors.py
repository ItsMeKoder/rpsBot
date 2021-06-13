#!/bin/python3
import time
from random import randint
from termcolor import colored
import sys
global verbose
from os import system
def setup():
    system("clear")
    if verbose:
        print(colored("[Start] Initializing Variables....","yellow"))
    global round
    round = int(input(colored('Number of rounds : ',"cyan")))

    global CPoints 
    global PPoints

    CPoints=0
    PPoints=0

    global possible
    possible=['r','p','s']
    global poss
    global player
    global computer
    if verbose:
        print(colored("[Done] Initializing Variables...","yellow"))
        time.sleep(1)
        system("clear")

def ask():
    if verbose:
        print(colored("[Start] Waiting for input","yellow"))
    print(colored("rock(r),paper(p),scissors(s) : ", "cyan"),end="")
    pl = input()
    if verbose:
        print(colored("[Done] Got Input","yellow"))

    if verbose:
        print(colored("[Start] Getting Random number for me to create my input","yellow"))
    chosen = randint(1,3)
    if verbose:
        print(colored("[Done] Getting Random number for me to create my input","yellow"))
    if chosen == 1:
        c = 'r'
        if verbose:
            print(colored("[Done] creating my input","yellow"))
    elif chosen == 2:
        c = 'p'
        if verbose:
            print(colored("[Done] creating my input","yellow"))
    elif chosen == 3:
        c = 's'
        if verbose:
            print(colored("[Done] creating my input","yellow"))

    
    if verbose:
            print(colored("[Done] Printing the inputs","yellow"))

    print(colored(pl,"green"), 'vs', colored(c,"blue"))

    if pl not in possible:
        p=False
    else:
        p=True
    return [p,pl,c]

def start():
    if verbose:
        print(colored("[Start] Starting the Game","yellow"))
    PPoints=0
    CPoints=0
    for i in range(0,round):
        x=ask()
        poss=x[0] 
        player=x[1]
        computer=x[2]

        while not poss:
            print(colored("[ERROR] You have entered an invalid character!",'red'))
            x=ask()
            poss=x[0]
            player=x[1]
            computer=x[2]

            
        if poss:
            if player == computer:
                print
                print(colored('DRAW!!!!!',"cyan"))

            elif player == 'r'and computer == 's':
                print(colored('Player wins!!!!!',"green"))
                PPoints=+1

            elif computer == 'p' and player == 'r':
                print(colored('Computer wins!!!!',"red"))
                CPoints=+1

            elif player == 'p' and computer == 'r':
                print(colored('Player wins!!!!!',"green"))
                PPoints=+1

            elif computer == 's'and player == 'p':
                print(colored('Computer wins!!!!',"red"))
                CPoints=+1

            elif player == 's' and computer == 'p':
                print(colored('Player wins!!!!!',"green"))
                PPoints=+1

            elif computer == 's'and player == 'p':
                print(colored('Computer wins!!!!',"red"))
                CPoints=+1
            print(colored("Player Points : "+str(PPoints),"cyan"))
            print(colored("Computer Points : "+str(CPoints),"cyan"))
    if verbose:
        print(colored("[Done] The game has ended\n [Start] Printing the results","yellow"))
    if PPoints > CPoints:
        print(colored("\n====================Congrats! You won!====================","green"))
    elif PPoints == CPoints:
        print(colored("\n====================Draw!====================","yellow"))
    else:
        print(colored("\n====================Uh Oh! You have lost....====================","red"))
    if verbose:
        print(colored("[Done] Printed the results","yellow"))


if __name__ == '__main__':
    if "--verbose" in sys.argv or "-v" in sys.argv:
        verbose=True
    else:
        verbose=False
    try :
        setup()
        
    except KeyboardInterrupt:
        print(colored("\n[ERROR] : User Interrupted using Keyboard", "red"))
        quit()
    try :
        start()
        
    except KeyboardInterrupt:
        print(colored("\n[ERROR] : User Interrupted using Keyboard", "red"))
        quit()