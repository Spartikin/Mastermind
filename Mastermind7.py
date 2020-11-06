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
       # return gamemode
        test3 = Game_Options()
        if gamemode == 'a':
            test3.select_game_A()
        elif gamemode == 'b':
            test3.select_game_B()
        elif gamemode == 'c':
            test3.select_game_C()
        

class Game_Options(GameMode_Selector):

    def __init__ (self):
        super().__init__()
    
    def select_game_A(self):
        # test3 = GameMode_Selector()
        # test3.display_details()
        
        """if A is selected"""
        gamemode = 'a'
        while gamemode == 'A' or gamemode == 'a':
            print ('What would you like to do?a')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            """if neither p or q is selected"""
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
                return Player_1_Name, Player_2_Name

                """if q is selected"""
            elif play == 'q':
                print('goodbye!')
                return

    def select_game_B(self):
        gamemode = 'b'
        """if B is Selected"""
        while gamemode == 'B' or gamemode == 'b':
            print ('What would you like to do?b')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            """if neither p or q is selected"""
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
                return Player_1_name

            elif play == 'q':
                print('goodbye!')
                return
    
    def select_game_C (self):
        """if C is pressed"""
        gamemode = 'c'
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
                Player_1_Name = input()
                print ("")
                print ('Player 2: What is your name?')
                Player_2_Name = input()
                print("")
                print ('Player 3: What is your name?')
                Player_3_Name = input()
                print ("")
                print ('Player 4: What is your name?')
                Player_4_Name = input()
                print("")
                return Player_1_Name, Player_2_Name, Player_3_Name, Player_4_Name

            elif play == 'q':
                print('goodbye!')
                return



"""display details from top of screen"""
gm_selector = GameMode_Selector()
gm_selector.display_details()

