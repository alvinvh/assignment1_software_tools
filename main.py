import random, time, sys

def intro():
    print("########################################")
    print("Welcome to the Scissor, Paper, Rock game")
    print("########################################")
    print("To play please input number 'P'")
    print("To quit please input 'Q'")
    while True:
        try:    # input validation
            Userinput = input()
            if Userinput.upper() == 'P':    # p to play
                return True
            elif Userinput.upper() == 'Q':  # q to quit
                return False
            else:
                raise ValueError

        except (ValueError, TypeError):
            print("Please input 'P' to play or 'Q' to quit")

def NPC_Choice():
    return random.randint(1,3)    # randomize NPC choice


def userinput(round):
    print("Round {}!!".format(round))
    print("************")
    print("Please choose your choice:\n"
          "1. Rock\n"
          "2. Paper\n"
          "3. Scissor")
    NPC_choice = NPC_Choice()
    print("Please input 1, 2, 3, or 'Q' to exit!")
    list_of_option = ['1','2','3']  # expected user input
    while True:
        try:    # inout validation
            user = input()
            if user == "q" or user == "Q":
                sys.exit()  # quit the game
            elif user not in list_of_option:
                raise ValueError
            user = int(user)
            print("NPC is choosing!")
            for i in range(2):
                print("...")
                time.sleep(0.5)
            return user, NPC_choice
        except (ValueError, TypeError):
            print("Please check your input! only enter 1, 2, 3, or 'Q' to exit")


def comparison(user, NPC_choice):   # function to decide the winner
    if NPC_choice == user:
        return "Draw"
    elif NPC_choice == 1:
        if user == 2:
            return "NPC choose Rock, Paper covers Rock\n" \
                   "User Win!"
        elif user == 3:
            return "NPC choose Rock, Rock smashes Scissor\n" \
                   "User Lose!"
    elif NPC_choice == 2:
        if user == 1:
            return "NPC choose Paper, Paper covers Rock\n" \
                   "User Lose!"
        elif user == 3:
            return "NPC choose Paper, Scissor cuts Paper\n" \
                   "User Win!"
    elif NPC_choice == 3:
        if user == 1:
            return "NPC choose Scissor, Rock smashes Scissor\n" \
                   "User Win!"
        elif user == 2:
            return "NPC Choose Scissor, Scissor cuts Paper\n" \
                   "User Lose!"



def userinput_2(result):    # function to play again
    print(result)
    print("Do you want to play again?")
    while True:
        try:    # input validation
            u_input = input("enter 'Y' to play again 'N' to exit  ").lower()
            if u_input == 'y' or u_input == 'n':
                return u_input
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("Please check your input")

def repeat(selection):
    if selection == 'y':
        print("\n\n\n\n\n")
        return True
    elif selection == 'n':
        return False
    else:
        return False

def score(score_user = 0, score_npc = 0, rounds = 1):   # function to count the score and rounds
    if score_user >= 5 or score_npc >= 5:   # whoever have 5 points first win
        if score_user > score_npc:
            return "User Win!"
        else:
            return "NPC Win!"
    user, NPC = userinput(rounds)
    result = comparison(user, NPC)
    print(result)
    rounds +=1  # increment the round by 1
    if "User Win!" in result:
        score_user += 1
        print("Score:\n"
              "User {}\n"
              "NPC {}\n\n".format(score_user,score_npc))
        return score(score_user, score_npc, rounds) # recursive function
    elif "User Lose!" in result:
        score_npc += 1
        print("Score:\n"
              "User {}\n"
              "NPC {}\n\n".format(score_user, score_npc))
        return score(score_user, score_npc, rounds) # recursive function
    else:
        print("Score:\n"
              "User {}\n"
              "NPC {}\n\n".format(score_user, score_npc))
        return score(score_user, score_npc, rounds) # recursive function


#Please remove """ to start the game
"""a = intro()
while a:
    result = score()
    option = userinput_2(result)
    a = repeat(option)
"""

