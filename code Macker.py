code = None
print("Welcome Tom Turbo, you need to create a code that consists of four pegs.")
print("Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite,")
print("or (B)lack. Specify the code by specifying four characters where each")
print("character indicates a colour as above. For example, WWRG represents the")
print("code White-White-Red-Green. You need to enter the code twice. No character")
print("is shown on the screen so Supermind cannot see it.")
print("")
while code == None:
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
