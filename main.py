#first let's make a ref array

ref_map = [[0.0,0.1,0.2,0.3,0.4,0.5], [1.0,1.1,1.2,1.3,1.4,1.5], [2.0,2.1,2.2,2.3,2.4,2.5], [3.0,3.1,3.2,3.3,3.4,3.5], [4.0,4.1,4.2,4.3,4.4,4.5],[5.0,5.1,5.2,5.3,5.4,5.5], [6.0,6.1,6.2,6.3,6.4,6.5], [7.0,7.1,7.2,7.3,7.4,7.5], [8.0,8.1,8.2,8.3,8.4,8.5], [9.0,9.1,9.2,9.3,9.4,9.5], [10.0,10.1,10.2,10.3,10.4,10.5]]

#print(ref_map)

map = [[0,3,0,0,0,0], [0,1,0,0,0,0], [0,1,0,0,0,0], [1,1,1,0,1,1], [1,1,1,1,4,1], [1,1,1,0,1,4], [0,1,0,0,0,0], [0,1,1,2,0,0], [0,0,0,1,0,0], [0,0,2,1,1,0], [0,5,1,1,2,0]]
print (map[[0],[0]])

#print(map)
positiony = 4
positionx = 1
print("Welcome to Leah's Spooky Haunted House\nDo you think you can find the cursed treasure?\n\n\nUse 'w', 'a', 's', 'd' to play\n\n\n")

play = input("Type 'Start' to play")

if play != "Start" or play !="start":
  print("Ok, goodbye")

play = "start"
#later change this so that the player can exit the game

print("Welcome Adventurer!\nYou find yourself in a dark room, your lantern seems so dim in the vast blackness of the old place that you can barely see even a step in front of you.\n\nChoose a direction to move in\n")

