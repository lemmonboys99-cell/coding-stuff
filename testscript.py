import pygame,sys,random
from pygame.math import Vector2
import os



if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')


inventoryp = ['Ice Cream', 'Sandwich', 'Soda', "Salad", "Water"]
inventory = ['ice cream', 'sandwich', 'soda', "salad", "water"]


print("you has: ", end = "")
for i in inventoryp:
    if i == inventoryp[len(inventoryp)-1]:
        print(i, end = ". \n")
        break
    print(i, end = ", ")
    
choice = input('What would you like to eat? You can eat multiple items up to 3. ').lower()

selection = None
for item in inventory:
    print(item)
    if item in choice:
        selection = item
        print('yay worked')
        break
    else:
        print('didnt work sad')
        
