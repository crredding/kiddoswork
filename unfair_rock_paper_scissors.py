def unfair_r_p_s():
    import random
    AI_choices = ("rock", "paper", "scissors")
    player_choices = ("rock", "paper", "scissors", "quit")
    player_score = 0
    AI_score = 0
    Prps = ""
    while Prps != "quit":
        #Take the player input and initiate the Ai choice
        Prps = input("do you chose rock, paper, scissors or quit?").lower()
        while Prps not in player_choices:
            print("Incorrect selection. Please try again.")
            Prps = input("do you chose rock, paper, scissors or quit?").lower()
        Arps = random.choice(AI_choices)
        #Tell the player what they chose
        print("The computer chose " + Arps + " and you chose " + Prps + ".")
        if Prps != "quit":
            #Tie logic
            if Arps == Prps:
                if player_score != 0:
                    player_score -= 1
                if AI_score != 0:
                    AI_score -= 1
                print("It's a tie!")
            #Combat logic    
            #Computer chooses scissors
            elif Arps == "scissors":
                if Prps == "paper":
                    AI_score += 1
                    print("the computer wins!")
                else:
                    player_score += 1
                    print("you win!")
            #Computer chooses rock
            elif Arps == "rock":
                if Prps == "paper":
                    player_score += 1
                    print("you win!")
                else:
                    AI_score += 1
                    print("the computer wins!")
            #Computer chooses paper
            else :
                if Prps == "rock":
                    AI_score += 1
                    print("the computer wins!")
                else:
                    player_score += 1
                    print("you win!")

    print("The final score is: player: " + str(player_score) + " computer: " + str(AI_score) + ".")
    
    if AI_score > player_score:
        print("you lose:(")
    elif AI_score < player_score:
        print("you win:)")
    else:
        print("you tie :|")

if __name__ == "__main__":
    unfair_r_p_s()
