from Zomino import *
from Mcdonalds import *
from PapaZones import *

res = None

print("!!! Welcome to Zomino !!!")

print("Available restraurant: \n 1 Mcdonalds \n 2 Zomino \n 3 PapaZones")
res_input = input("Enter the restraurant by using the serial number: \n")

if res_input == '1':
    res = Mcdonalds()

if res_input == '2':
    res = Zominoes()

if res_input == '3':
    res = PapaZones()

res.ask_for_menu()