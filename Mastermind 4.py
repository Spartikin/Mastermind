import random
name = None
play = None

"""display creator details"""
class GameMode_Selector():
    def display_details():
        print ('Welcome to Mastermind!')
        print ('Developed by Nicholas Tripodi-Baslis')
        print ('COMP 1046 Object-Orionted Programming')
        """ask the player if they would like to play Mastermind"""
        print ('Select which game you want to play: ')
        print ("(A) Original Mastermind for 2 Players")
        print ("(B) Original Mastermind for 1 Player")
        print ("(C) Mastermind44 for 4 Players")
        gamemode = input("")

        """if player input does not equal A OR B OR C, ask the question again"""
        while gamemode != 'A'and gamemode != 'a' and gamemode != 'B' and gamemode != 'b'and gamemode != 'C' and gamemode != 'c':
            print ('Select which game you want to play:')
            print ("(A) Original Mastermind for 2 Players")
            print ("(B) Original Mastermind for 1 Player")
            print ("(C) Mastermind44 for 4 Players")
            gamemode = input('')
        return gamemode



"""display details from top of screen"""
gamemode = GameMode_Selector.display_details()
print ("gamemode ="  + str(gamemode))
        
"""if B is pressed"""
class Game_Options(GameMode_Selector):
    def select_game():
        while gamemode == 'A' or gamemode =='a':
            print ('What would you like to do?ss')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            if play != 'p' and play != 'q':
                print ('What would you like to do?tt')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')


        """if B is pressed"""
        while gamemode == 'B' or gamemode == 'b':
            print ('What would you like to do?aa')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

        
            if play != 'p' and play != 'q':
                print ('What would you like to dobb?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

            elif play == 'p':
                print ('Player 1: What is your name?')
                name = input()

            elif play == 'q':
                print('goodbye!')
    

        """if C is pressed"""
        while gamemode == 'C' or gamemode == 'c':
            print ('What would you like to do?cc')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            while play != 'p' and play != 'q':
                print ('What would you like to do?CC')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

Game_Options.select_game()
# class Mastermind44():

#class mastermind():

#class player_Class():

#class Code_Maker():

# class Code_Braker():

# class Computer_Class():

# class Player_Guess():

# class Code_Peg():
#     length = 4
#     pegs = [random.choice('RGLYWB') for _ in range(length)]
#     print(*pegs)S

#     if colour [1] == 'R':
#         peg = 'Red'

#     elif colour [1] == 'G':
#         peg = 'Green'

#     elif colour [1] == 'L':
#         peg = 'Blue'

#     elif colour [1] == 'Y':
#         peg = 'Yellow'

#     elif colour [1] == 'W':
#         peg = 'White'

#     else:
#         peg = 'Black'

# class Key_Peg():

# class Code():

# class Code_Checker():



    
