import random
code = []

class Computer():
    def __init__ (self):
        pass

    def random_code (self):
        computer_random = random.randint(1, 6) 
        code = computer_random
        while len(code) != 4:
            code.append (computer_random)
            print(code)
            return

test = Computer()
test.random_code()