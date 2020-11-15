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
        if gamemode == 'a' or gamemode == 'A':
            test3.select_game_A()
        elif gamemode == 'b' or gamemode == 'B':
            test3.select_game_B()
        elif gamemode == 'c' or gamemode == 'C':
            test3.select_game_C()
        

class Game_Options(GameMode_Selector):

    def __init__ (self):
        super().__init__()
    
    def select_game_A(self):
        # test3 = GameMode_Selector()
        # test3.display_details()
        
        """if A is selected"""
        gamemode = 'a'
        if gamemode == 'A' or gamemode == 'a':
            print ('What would you like to do?a')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            """if neither p or q is selected"""
            while play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')
                
            """if p is selected"""
            name = player()
            if play == 'p':
                name.player_chose_a()
            

                """if q is selected"""
            elif play == 'q':
                print('goodbye!')
                return

    def select_game_B(self):
        gamemode = 'b'
        """if B is Selected"""
        if gamemode == 'B' or gamemode == 'b':
            print ('What would you like to do?b')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            """if neither p or q is selected"""
            while play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

            """if p is selected"""
            name2 = player()
            if play == 'p':
                name2.player_chose_b()
            

            elif play == 'q':
                print('goodbye!')
                return
    
    def select_game_C (self):
        """if C is pressed"""
        gamemode = 'c'
        if gamemode == 'C' or gamemode == 'c':
            print ('What would you like to do?')
            print ('(p)lay the game')
            print ('(q)uit')
            play = input ('')

            while play != 'p' and play != 'q':
                print ('What would you like to do?')
                print ('(p)lay the game')
                print ('(q)uit')
                play = input ('')

            """if p is selected"""
            name3 = player()
            if play == 'p':
                name3.player_chose_c()
            

            elif play == 'q':
                print('goodbye!')
                return

class player(Game_Options):
    def __init__ (self):
        super().__init__()

    def player_chose_a (self):
        play = 'p'
        if play == 'p':
            print("")
            print ('Player 1: What is your name?')
            Player_1_Name = input()
            print ("")
            print ('Player 2: What is your name?')
            Player_2_Name = input()
            print("")
            game2 = Code2(Peg, Player_Guess, Key_Peg, Computer)
            game2.guesses(Peg)
            return Player_1_Name, Player_2_Name

    def player_chose_b (self):
        play = 'p'
        if play == 'p':
            print("")
            print ('Player 1: What is your name?')
            Player_1_name = input()
            print("")
            name5 = Code_Checker(Peg, Player_Guess, Key_Peg, Computer)
            name5.check_guess(Peg)
            return Player_1_name

    def player_chose_c (self):
        play = 'p'
        if play == 'p':
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


class Mastermind44():
    def __init__ (self):
        pass

class mastermind():
    def __init__ (self, player_Guess, Code_Checker):
        self.player_Guess = ""
        self.Code_Checker = Code_Checker

    def storage (self):
        guess = input
        chec = Code_Checker(Peg, Player_Guess, Key_Peg, Computer)
        chec.check_guess


class Peg():
    def __init__ (self, colours):
        self.colours = colours
        
    def pegs_colours(self, colours):
        colours = ['R', 'G', 'L', 'Y', 'W', 'B']

class Code_Maker(Peg):
    def __init__ (self):
        pass
    def Maker(self):
        num = None
        print("Welcome Tom Turbo, you need to create a code that consists of four pegs.")
        print("Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,")
        print("or (B)lack. Specify the code by specifying four characters where each")
        print("character indicates a colour as above. For example, WWRG represents the")
        print("code White-White-Red-Green. You need to enter the code twice. No character")
        print("is shown on the screen so Supermind cannot see it.")
        print("")
        while num == None:
            print("Enter the code now:")
            code1 = input("")

            print("")
            print ('Enter the same code again:')
            code2 = input("")
            if code1 == code2:
                num = code2
                print("")
                print ("The code was stored.")
                print (num)

            else:
                print('code did not match')

        game2 = Code2(Peg, Player_Guess, Key_Peg, Computer)
        game2.guesses(Peg)



class Code_Braker():
    def __init__ (self):
        pass
    def attempts (self):
        pass

class Key_Peg():
    def __init__ (self, checker):
        self.checker = checker

    def peg_checker (self, checker):
        checker = ['W', 'B']
        key = ''.join(checker)
        return key    

class Computer(Peg):
    def __init__ (self):
        pass

    def random_code (self, colours):
        pegs = random.choices(colours, k=4)
        num = ''.join(pegs)
        print(num)
        # name7 = Code_Checker()
        # name7.check_guess(self)

class Player_Guess():
    def __init__ (self):
        super().__init__()
        # self.guess = guess

    def Attempts (self):
        print("Welcome Supermind. You can now start to play by guessing the code.")
        print("Enter a guess by providing four characters and press Enter.")
        print ('Attempt #1:')
        guess = input("")

        att = mastermind(Player_Guess, Code_Checker)
        # while guess != input:
        #     guess = input("")
        if guess == input:
            att.__init__(Player_Guess, Code_Checker)


        test3 = Code_Checker(Peg, Player_Guess, Key_Peg, Computer)
        """Return Guess"""

class Code(Computer):
    def __init__ (self):
        pass

    def Actual_Code(self, code):
        pass

class Code2(Player_Guess, Computer, Peg, Key_Peg):
    def __init__ (self, colours, guess, key, random_code):
        self.colours = colours
        self.guess = ""
        self.key = key
        self.random_code = ""
    def guesses (self, colours):
        length = 4
        colours=['R', 'G', 'L', 'Y', 'W', 'B']
        num = None

        print("Welcome Tom Turbo, you need to create a code that consists of four pegs.")
        print("Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,")
        print("or (B)lack. Specify the code by specifying four characters where each")
        print("character indicates a colour as above. For example, WWRG represents the")
        print("code White-White-Red-Green. You need to enter the code twice. No character")
        print("is shown on the screen so Supermind cannot see it.")
        print("")
        while num == None:
            print("Enter the code now:")
            code1 = input("")

            print("")
            print ('Enter the same code again:')
            code2 = input("")
            if code1 == code2:
                num = code2
                print("")
                print ("The code was stored.")
                print (num)

            else:
                print('code did not match')

        print("Welcome Supermind. You can now start to play by guessing the code.")
        print("Enter a guess by providing four characters and press Enter.")
        print ('Attempy #1:')
        guess = input("")

        """if player guesses it first try"""
        if (guess == num):   
            print("Great! You guessed the number in just 1 try! You're a Mastermind!") 
        else: 
            """records the number of turns you are on""" 
            turns = 1 

            

            """while players guess does not equal the code""" 
            while (guess != num):   
                """add 1 to the turn"""
                turns += 1  
                

                """ammount of the code correct"""
                count = 0

                """explicit type conversion of an integer to 
                a string in order to ease extraction of digits
                """ 
                guess = str(guess)   

                """explicit type conversion of a string to an integer """
                num = str(num)   

                """correct[] list stores letters which are correct"""
                correct = ['']*4

                """for loop runs 4 times since the number has 4 letters""" 
                for i in range(0, 4):  

                    """checking for equality of digits"""
                    if (guess[i] == num[i]):   
                        """number of digits guessed correctly increments"""
                        count += 1  
                        """the digit is stored in correct[]""" 
                        correct[i] = guess[i]   
                    else: 
                        continue

                # if turns >=5:
                #     print('Game over')
                #     return

                """when not all the digits are guessed correctly"""
                if (count < 4) and (count != 0): 

                    print("Feedback on Attempt",  "#" + format(turns -1) + ':')
                    for k in correct: 
                        print(k, end=' ')

                    print('\n') 

                    print("Attempt", "#" + format(turns, ) + ':')
                    guess = input("")

                    """when none of the digits are guessed correctly. """
                elif (count == 0):   

                    print("Feedback on Attempt", "#" + format(turns -1) + ':')
                    print('\n') 
                    print("Attempt", "#" + format(turns, ) + ':')
                    guess = input("")

            """when code is finally entered correctly""" 
            if guess == num:   
                print("You've become a Mastermind!") 
                print("It took you only", "#" + format(turns, ) + ':', "tries.")

class Code_Checker(Player_Guess, Computer, Peg, Key_Peg):
    def __init__ (self, colours, guess, key, random_code):
        self.colours = colours
        self.guess = ""
        self.key = key
        self.random_code = ""

    def check_guess (self, colours):
        length = 4
        colours=['R', 'G', 'L', 'Y', 'W', 'B']
        pegs = random.choices(colours, k=4)
        num = ''.join(pegs)
        print(num)

        print("Welcome Supermind. You can now start to play by guessing the code.")
        print("Enter a guess by providing four characters and press Enter.")
        print ('Attempy #1:')
        guess = input("")

        """if player guesses it first try"""
        if (guess == num):   
            print("Great! You guessed the number in just 1 try! You're a Mastermind!") 
        else: 
            """records the number of turns you are on""" 
            turns = 1 

            """while players guess does not equal the code""" 
            while (guess != num):   
                """add 1 to the turn"""
                turns += 1  
                

                """ammount of the code correct"""
                count = 0

                """explicit type conversion of an integer to 
                a string in order to ease extraction of digits
                """ 
                guess = str(guess)   

                """explicit type conversion of a string to an integer """
                num = str(num)   

                """correct[] list stores letters which are correct"""
                correct = ['']*4

                """for loop runs 4 times since the number has 4 letters""" 
                for i in range(0, 4):  

                    """checking for equality of digits"""
                    if (guess[i] == num[i]):   
                        """number of digits guessed correctly increments"""
                        count += 1  
                        """the digit is stored in correct[]""" 
                        correct[i] = guess[i]   
                    else: 
                        continue

                # if turns >=5:
                #     print('Game over')
                #     return

                """when not all the digits are guessed correctly"""
                if (count < 4) and (count != 0): 

                    print("Feedback on Attempt",  "#" + format(turns -1) + ':')
                    for k in correct: 
                        print(k, end=' ')

                    print('\n') 

                    print("Attempt", "#" + format(turns, ) + ':')
                    guess = input("")

                    """when none of the digits are guessed correctly. """
                elif (count == 0):   

                    print("Feedback on Attempt", "#" + format(turns -1) + ':')
                    print('\n') 
                    print("Attempt", "#" + format(turns, ) + ':')
                    guess = input("")

            """when code is finally entered correctly""" 
            if guess == num:   
                print("You've become a Mastermind!") 
                print("It took you only", "#" + format(turns, ) + ':', "tries.")

"""display details from top of screen"""
gm_selector = GameMode_Selector()
gm_selector.display_details()

