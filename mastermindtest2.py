import random 
num = None

# the .randrange() function generates a 
# random number within the specified range.

# num = random.randrange(1000, 10000)  

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

