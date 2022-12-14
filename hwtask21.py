import random
def game ():
    print ('There are 117 candies on the table.'
    'You and your opponent can take up to 28 candies in their turn.' 
    'Whose turn is first is decided randomly.'
    'The player who takes last candies from the table gets all candies')
    print ('Player A vs. Player B')
    first = random.randint (0,1)
    if first == 0:
        winner = False
        print ('Player A starts')
    elif first == 1:
        winner = True
        print ('Player B starts')
    candy_left = 117
    while candy_left > 0:
        print ('')
        print (f'Candy left: {candy_left}')
        if winner == True:
            print (f"Player B 's turn")
        else: 
            print (f"Player A 's turn")
        temp = int(input('enter the number of candies you would like to take (1-28): ' ))
        candy_left = candy_left - temp
        if winner == True:
            winner = False
        elif winner == False:
            winner = True
    if winner == True:
        result = 'Player A has won'
    else: result = 'Player B has won'
    return result


def game_vs_bot ():
    print ('There are 117 candies on the table.'
    'You and computer can take up to 28 candies in their turn.' 
    'Whose turn is first is decided randomly.'
    'The player who takes last candies from the table gets all candies')
    print ('Player A vs. Computer')
    first = random.randint (0,1)
    if first == 0:
        winner = False
        print ('Player A starts')
    elif first == 1:
        winner = True
        print ('Computer starts')
    candy_left = 117    
    while candy_left > 0:
        print ('')
        print (f'Candy left: {candy_left}')
        if candy_left <= 28 and winner == True:
            temp = candy_left
            print (f'Computer has taken {temp} candies')
        else:
            if winner == True:
                print (f"Computer's turn")
                temp = random.randint (1, 28)
                print (f'Computer has taken {temp} candies')
            else: 
                print (f"Player A 's turn")
                temp = int(input('enter the number of candies you would like to take (1-28): ' ))
        candy_left = candy_left - temp
        if winner == True:
            winner = False
        elif winner == False:
            winner = True
    if winner == True:
        result = 'Player A has won'
    else: result = 'Computer has won'
    return result
