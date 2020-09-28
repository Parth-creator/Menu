from Zomino import *
from Mcdonalds import *
from PapaZones import *

zomino = Zominoes()
papa_zones = PapaZones()
mcdonalds = Mcdonalds()

print("!!! Welcome to Zomino !!!")

print("Available restraurant: \n 1 Mcdonalds \n 2 Zomino \n 3 PapaZones")
res_input = input("Enter the restraurant by using the serial number: \n")

if res_input == '1':
    mcdonalds.ask_for_menu()

if res_input == '2':
    zomino.ask_for_menu()

if res_input == '3':
    papa_zones.ask_for_menu()



