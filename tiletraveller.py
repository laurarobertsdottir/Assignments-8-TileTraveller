# Player starts in tile 1,1
# Depending on where the player is located they can either move north, south, east or west.
# Ask for which direction the player wants to proceed to.
# If invalid direction is entered print invalid 
# Once the player is in the victory tile 3.1, print victory msg and stop loop. 

start = (1,1)
átt = "(N)orth."
print("You can travel: ", átt)

while start != (3,1):
    if start == (1,1):    
        direction = input("Direction: ")
        if direction == "N" or direction == "n":
            start = (1,2)
            átt = "(N)orth or (E)ast or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else: 
            print("Not a valid direction!")
            print("You can travel:", átt)
            start = start
    if start == (1,2):
        if direction == "N" or direction == "n":
            start = (1,3)
            átt = "(E)ast or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        elif direction == "E" or direction == "e":
            start = (2,2)
            átt = "(W)est or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        elif direction == "S" or direction == "s":
            start = (1,1)
            átt = "(N)orth."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else:
            print("Not a valid direction!")
            start = start
            direction = input("Direction: ")
    if start == (1,3):
        if direction == "E" or direction == "e":
            start = (2,3)
            átt = "(E)ast or (W)est"
            print("You can travel: ", átt)
            direction = input("Direction: ")
        elif direction == "S" or direction == "s":
            start = (1,2)
            átt = "(N)orth or (E)ast or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else:
            print("Not a valid direction!")
            start = start 
            direction = input("Direction: ")
    if start == (2,3):
        if direction == "E" or direction == "e":
            start = (3,3)
            átt = "(S)outh or (W)est."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        elif direction == "W" or direction =="w":
            start = (1,3)  
            átt = "(E)ast or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else:
            print("Not a valid direction!")
            start = start 
            direction = input("Direction: ")
    if start == (2,2):
        if direction == "S" or direction == "s":
            start = (2,1)
            átt = "(N)orth."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        elif direction == "W" or direction == "w":
            start = (1,2)
            átt = "(N)orth or (E)ast or (S)outh."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else:
            print("Not a valid direction!")
            start = start 
            direction = input("Direction: ")
    if start == (2,1):
       if direction == "n" or direction =="N":
           start = (2,2)
           átt = "(S)outh or (W)est."    
           print("You can travel: ",átt)  
           direction = input("Direction: ") 
       else:
           print("Not a valid direction!")
           start = start
           direction = input("Direction: ")
    if start == (3,3):
        if direction == "W" or direction == "w":
            start = (2,3)
            átt = "(E)ast or (W)est."    
            print("You can travel: ",átt)
            direction = input("Direction: ")
        elif direction == "S" or direction == "s":
            start = (3,2)
            átt = "(N)orth or (S)outh."
            print("You can travel: ",átt)
            direction = input("Direction: ")
        else: 
            print("Not a valid direction!")
            start = start
            direction = input("Direction: ")
    if start == (3,2):
        if direction == "S" or direction =="s":
            start = (3,1)
        elif direction == "N" or direction == "n":
            start = (3,3)
            átt = "(S)outh or (W)est."
            print("You can travel: ", átt)
            direction = input("Direction: ")
        else:
            print("Not a valid direction!")
            start = start
            direction = input("Direction: ")
    if start == (3,1):
        print("Victory!")



    
