import sys

b1 = '1'
b2 = '2'
b3 = '3'
b4 = '4'
b5 = '5'
b6 = '6'
b7 = '7'
b8 = '8'
b9 = '9'

def the_arena():
    print("|____"+ b1 +"____|____"+ b2 +"___|____"+ b3 +"____|")
    print("|____"+ b4 +"____|____"+ b5 +"___|____"+ b6 +"____|")
    print("|____"+ b7 +"____|____"+ b8 +"___|____"+ b9 +"____|")

### Player 1 chooses what letter will represent them    
chosen_letter = 0
while chosen_letter == 0:
    player_1 = input('Player 1 do you want to be X or O: ')
    if player_1 == 'X':
        player_2 = 'O'
        chosen_letter += 1
    elif player_1 == 'O':
        player_2 = 'X'
        chosen_letter += 1
    elif player_1 != 'X' or 'O':
        print('Choose X or O')

### These are the individual moves
decision1_made = 1
def p1_placement1():    
    global decision1_made
    decision1_made = 1
    while decision1_made == 1:
        p1_choice1 = input('which box do you want to put your ' + player_1 + ' player 1: ')
        if p1_choice1 == '1':
            decision1_made += 1
            global b1
            if b1 == '1':
                b1 = player_1
                the_arena()
            elif b1 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '2':
            decision1_made += 1
            global b2
            if b2 == '2':
                b2 = player_1
                the_arena()
            elif b2 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '3':
            decision1_made += 1
            global b3
            if b3 == '3':
                b3 = player_1
                the_arena()
            elif b3 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '4':
            decision1_made += 1
            global b4
            if b4 == '4':
                b4 = player_1
                the_arena()
            elif b4 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '5':
            decision1_made += 1
            global b5
            if b5 == '5':
                b5 = player_1
                the_arena()
            elif b5 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '6':
            decision1_made += 1
            global b6
            if b6 == '6':
                b6 = player_1
                the_arena()
            elif b6 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '7':
            decision1_made += 1
            global b7
            if b7 == '7':
                b7 = player_1
                the_arena()
            elif b7 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '8':
            decision1_made += 1
            global b8
            if b8 == '8':
                b8 = player_1
                the_arena()
            elif b8 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1
        elif p1_choice1 == '9':
            decision1_made += 1
            global b9
            if b9 == '9':
                b9 = player_1
                the_arena()
            elif b9 == 'X' or 'O':
                print('This block is already chosen')
                decision1_made -= 1



decision_made = 1
def p2_placement1():
    global decision_made
    decision_made = 1
    while decision_made == 1:
        p2_choice1 = input('which box do you want to put your ' + player_2 + ' player 2: ')
        if p2_choice1 == '1':
            decision_made += 1
            global b1
            if b1 == '1':
                b1 = player_2
                the_arena()
            elif b1 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '2':
            decision_made += 1
            global b2
            if b2 == '2':
                b2 = player_2
                the_arena()
            elif b2 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '3':
            decision_made += 1
            global b3
            if b3 == '3':
                b3 = player_2
                the_arena()
            elif b3 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '4':
            decision_made += 1
            global b4
            if b4 == '4':
                b4 = player_2
                the_arena()
            elif b4 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '5':
            decision_made += 1
            global b5
            if b5 == '5':
                b5 = player_2
                the_arena()
            elif b5 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '6':
            decision_made += 1
            global b6
            if b6 == '6':
                b6 = player_2
                the_arena()
            elif b6 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '7':
            decision_made += 1
            global b7
            if b7 == '7':
                b7 = player_2
                the_arena()
            elif b7 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '8':
            decision_made += 1
            global b8
            if b8 == '8':
                b8 = player_2
                the_arena()
            elif b8 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1
        elif p2_choice1 == '9':
            decision_made += 1
            global b9
            if b9 == '9':
                b9 = player_2
                the_arena()
            elif b9 == 'X' or 'O':
                print('This block is already chosen')
                decision_made -= 1

### This code helps determine the winner of the game through standard tic tac toe rules
def game_rules():
    if b1 == b2 == b3:
        print('game over player 1 wins ')
        sys.exit()
    elif b4 == b5 == b6:
        print('game over player 1 wins ')
        sys.exit()
    elif b7 == b8 == b9:
        print('game over player 1 wins ')
        sys.exit()
    elif b1 == b4 == b7:
        print('game over player 1 wins ')
        sys.exit()
    elif b2 == b5 == b8:
        print('game over player 1 wins ')
        sys.exit()
    elif b3 == b6 == b9:
        print('game over player 1 wins ')
        sys.exit()
    elif b7 == b5 == b3: 
        print('game over player 1 wins ')
        sys.exit()
    elif b1 == b5 == b9:
        print('game over player 1 wins ')
        sys.exit()

def game_rules2():
    if b1 == b2 == b3:
        print('game over player 2 wins ')
        sys.exit()
    elif b4 == b5 == b6:
        print('game over player 2 wins ')
        sys.exit()
    elif b7 == b8 == b9:
        print('game over player 2 wins ')
        sys.exit()
    elif b1 == b4 == b7:
        print('game over player 2 wins ')
        sys.exit()
    elif b2 == b5 == b8:
        print('game over player 2 wins ')
        sys.exit()
    elif b3 == b6 == b9:
        print('game over player 2 wins ')
        sys.exit()
    elif b7 == b5 == b3: 
        print('game over player 2 wins ')
        sys.exit()
    elif b1 == b5 == b9:
        print('game over player 2 wins ')
        sys.exit()

### This code executes all the code that was created earlier to make the tic tac toe game
def game_over():
    p1_placement1()
    p2_placement1()
    p1_placement1()
    p2_placement1()
    p1_placement1()
    game_rules()
    p2_placement1()
    game_rules2()
    p1_placement1()
    game_rules()
    p2_placement1()
    game_rules2()
    p1_placement1()
    game_rules()

game_over()

###congratulations you finished your first game/project

