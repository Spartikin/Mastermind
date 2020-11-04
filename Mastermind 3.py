class GameMode_Selector():
    def get_details(self, gamemode):
        self.gamemode = gamemode

    def display_details():
        print ('Welcome to Mastermind!')
        print ('Developed by Nicholas Tripodi-Baslis')
        print ('COMP 1046 Object-Orionted Programming')
        print ("")
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


        if gamemode == 'A' or 'a':
            print ('What would you like to dott?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            if play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

        """if B is pressed"""
        if gamemode == 'B' or 'b':
            print ('What would you like to dobb?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

        
            # if play != 'p' and play != 'q':
            #     print ('What would you like to do?')
            #     print ('(p)lay the game')
            #     print ('(q)uit')
            #     play = input ('')

            if play == 'p':
                print ('Player 1: What is your name?')
                name = input("")

            elif play == 'q':
                print('goodbye!')

        # while gamemode == 'b' or'b':
        #     Game_Options.test()




# """if B is pressed"""
# class Game_Options(GameMode_Selector):
#     def test():
#         while gamemode == 'A' or 'a':
#             print ('What would you like to do?')
#             print ('(p)lay the game')
#             print ('(q)uit')
#             play = input ('')

#             if play != 'p' and play != 'q':
#                 print ('What would you like to do?')
#                 print ('(p)lay the game')
#                 print ('(q)uit')
#                 play = input ('')

#         """if B is pressed"""
#         while gamemode == 'B' or 'b':
#             print ('What would you like to do?')
#             print ('(p)lay the game')
#             print ('(q)uit')
#             play = input ('')

        
#             if play != 'p' and play != 'q':
#                 print ('What would you like to do?')
#                 print ('(p)lay the game')
#                 print ('(q)uit')
#                 play = input ('')

#             elif play == 'p':
#                 print ('Player 1: What is your name?')
#                 name = input()

#             elif play == 'q':
#                 print('goodbye!')

GameMode_Selector.display_details()
