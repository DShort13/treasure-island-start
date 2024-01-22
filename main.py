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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

crossroad = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
crossroad = crossroad.lower()
if crossroad == "left":
  lake = input("You reach a lake and see two doors on the other side. Do you want to swim across or wait for help? Type 'swim' or 'wait'\n")
  lake = lake.lower()
  if lake == "wait":
    door = input("You see a red door, a blue door, and a yellow door. Which door do you want to go through? Type 'red', 'blue', or 'yellow'\n")
    door = door.lower()
    if door == 'red':
      print("Burned by fire. Game Over.")
    elif door == 'blue':
      print("Eaten by beasts. Game Over.")
    else:
      print("You Win!")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
