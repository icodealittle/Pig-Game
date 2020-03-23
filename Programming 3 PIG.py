import random

def main():
    #Human one is the user input – rolling the dies, whereas Human two is the computer.
    players = ['Human One', 'Human Two'] 
    turn_score = 0
    turn_score1 = 0
    #Shuffling turn between the players
    random.shuffle(players)

    while players:
        #Using i as a vraible for one of the player (Human one = user input 'r')
        for i in players:
            pl_input = input('It is your turn, Human One\n' +
                             'R – Roll\n' + 'H – Hold\n' +
                             'Enter your choices: ')
            choice = pl_input.upper()
        # if the player choose option 'r', they allow the computer generate random number for their round.
            if pl_input == 'r':
        #If player reach to 20 first, he/she win the round
                while turn_score <= 20:
        # random.randint means that the computer only allow to generate integers within the range 1 to 6.
                    roll = random.randint(1, 6)
        # The dice have to be roll to any integer that is equal to 1
                    if roll != 1:
                        turn_score += roll
        # Scores is calculate via a combination of their turn score (the number of dice rolled)
                        print('You rolled: ', roll)
                        print('Points in this round: ', turn_score)
                        break
        #If the dice roll = 1, the player lose that round.
                    if roll == 1:
                        print('You rolled a', roll)
                        print('wah wah waaahhhhh!!!!!! GAVE OVER!')
                        break
        # if the user select 'h', he/she chooses to skip their turn
                    if pl_input == 'h':
                        print('You skipped your turn.\n' +
                              'Your total score is: ', total_score)
                        total_score += turn_score
                        print('Turn score is: ', turn_score)
                        print('Final score is: ', total_score)
                        return total_score
                    if turn_score == 20:
                        print('You Won!!!')
                        return pl_input
            else:
                print('It is ' + str(i) + ' turn. ')
                while turn_score <= 20:
                    roll = random.randint(1, 6)
                    if roll != 1:
                        turn_score1 += roll
                        total_score = turn_score1 + roll
                        print( str(i) + ' rolled a ', roll)
                        print('Points in this round: ', turn_score1)
                        break
                    if roll == 1:
                        print('You rolled a ', roll)
                        print('wah wah waaahhhhh!!!!!! GAVE OVER!')
                        break
                    if pl_input == 'h':
                        print('You skipped your turn.\n' +
                              'Your total score is: ', total_score)
                        total_score += turn_score
                        print('Turn score is: ', turn_score)
                        print('Final score is: ', total_score)

main()
                
                             
                
