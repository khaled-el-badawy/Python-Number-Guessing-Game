print("guess number between 0 to 100")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
low = 0
high = 101
medium = (low + high)//2
state = True

guess  =input('Is Your number is ' + str(medium) + " perss Y or N: ")
if guess == "y" or guess == "Y" :
    print("game over")
    print("your Number is: " + str(medium))
    state = False
elif guess == "n" or guess == "N":
    while state :
        guess  = input("Higher(H), Lower(L) than " + str(medium) + ", or True(T)? ")
        if guess == "t" or guess == "T" :
            print("game over")
            print("your Number is: " + str(medium))
            state = False
        elif guess == "h" or guess == "H" :
            low = medium +1
            medium = (low + high)//2
            
        elif guess == "l" or guess == "L" :
            high = medium
            medium = (low + high)//2
            
        if low == high and guess == "l" :
            print("Error: Your Number out of range")
            state = False 
        else:
            medium = (low + high)//2 
else:
    print("Error")