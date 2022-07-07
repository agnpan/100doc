# TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.")

left_or_right = input("""\nYou are at a crossroad.
Would you like to go left or right? Type 'left' or 'right'. """).lower()

if left_or_right[0] == "l":
    swim_or_wait = input("""\nYou have reached a river passage by a cave.
Would you like to swim or enter the cave? Type 'swim' or 'enter'. """).lower()
    
    if swim_or_wait[0] == "e":
        door = input("""\nYou entered a cave and found 3 doors: one red, one yellow and one blue.
Which door would you like to enter? Type 'red', 'yellow' or 'blue'. """).lower()
        
        if door[0] == "r":
            print("\nYou got burned in a fire. Game Over.")
        elif door[0] == "b":
            print("\nYou were eaten by beasts. Game Over.")
        elif door[0] == "y":
            print("\nCongratulations! You found the treasure!")
        else:
            print("\nGame Over.")
    else:
        print("You were attacked by a trout. Game Over.")

elif left_or_right[0] == "r":
    print("You fell into a hole. Game Over.")
else:
    print("You chose an incorrect option. Game Over.")