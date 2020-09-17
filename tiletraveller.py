# Player starts in tile 1,1
# Depending on where the player is located they can either move north, south, east or west.
# Ask for which direction the player wants to proceed to.
# If invalid direction is entered print invalid 
# Once the player is in the victory tile 3.1, print victory msg and stop loop. 

start = (1,1)
átt = "(N)orth."
print("You can travel:", átt)

while start != (3,1):
    if start == (1,1):
        direction = input("Direction: ")
        if direction == "N":
            start = (1,2)
            átt = "(N)orth or (E)ast or (S)outh."
            print("You can travel:", átt)
            direction = input("Direction: ")
        else: 
            print("Not a valid direction!")
            start = start
    if start == (1,2):
        if direction == "N":
            start = (1,3)
            átt = "(E)ast or (S)outh."
            direction = input("Direction:")
        elif direction == "E":
            start = (2,2)
            átt = "(W)est or (S)outh."
            direction = input("Direction:")
        
    
