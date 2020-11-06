import random
class Code_Peg():
    colours = ['R', 'G', 'L', 'Y', 'W', 'B']
    pegs = random.choices(colours, k=4)
    num = ''.join(pegs)
    print(num)
