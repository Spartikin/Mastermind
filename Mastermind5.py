import random
name = None
play = None

"""display creator details"""
class GameMode_Selector():
    
    def __init__ (self):
        pass

    def display_details(self):
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
gm_selector = GameMode_Selector()
gamemode = gm_selector.display_details()
print ("gamemode ="  + str(gamemode))
        
"""if B is pressed"""
class Game_Options(GameMode_Selector):

    def __init__ (self):
        pass

    def select_game(self):
        """if A is pressed"""
        while gamemode == 'A' or gamemode =='a':
            print ('What would you like to do?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            """if neither p or q is pressed"""
            if play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')
                
            """if p is selected"""
            elif play == 'p':
                
                print("")
                print ('Player 1: What is your name?')
                Player_1_Name = input()
                print ("")
                print ('Player 2: What is your name?')
                Player_2_Name = input()
                print("")
                return

            elif play == 'q':
                print('goodbye!')
                return


        """if B is pressed"""
        while gamemode == 'B' or gamemode == 'b':
            print ('What would you like to do?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

        
            if play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

            elif play == 'p':
                print("")
                print ('Player 1: What is your name?')
                Player_1_name = input()
                print("")
                return

            elif play == 'q':
                print('goodbye!')
                return
    

        """if C is pressed"""
        while gamemode == 'C' or gamemode == 'c':
            print ('What would you like to do?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            if play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

            elif play == 'p':
                print("")
                print ('Player 1: What is your name?')
                Player_1_name = input()
                print("")
                return

            elif play == 'q':
                print('goodbye!')
                return

game_options = Game_Options()
game_options.select_game()

class player():
    def __init__ (self):
        pass


class Mastermind44():
    def __init__ (self):
        pass

class mastermind():
    def __init__ (self):
        pass



class Code_Maker():
    def __init__ (self, code_list, length):
        self.code_list = code_list
        self.length = length

class Code_Braker():
    def __init__ (self):
        pass



class Player_Guess():
    def __init__ (self):
        pass

class Peg():
    def __init__ (self):
        pass
        
    def pegs_colours(self, colours):
        colours = ['R', 'G', 'L', 'Y', 'W', 'B']

class Computer():
    def __init__ (self):
        pass

    def random_code (self, Peg, pegs, colours):
        pegs = random.choices(colours, k=4)
        print(pegs)

class Key_Peg():
    def __init__ (self):
        pass

    def peg_checker (self, checker):
        checker = ['W', 'B']

class Code(Computer):
    def __init__ (self):
        pass

    def Actual_Code(self, code):
        pass

class Code_Checker():
    def __init__ (self):
        pass

