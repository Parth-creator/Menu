from zomino import *

burger_quantity = 0
pizza_quantity = 0
colddrink_quantity = 0

menu_dict = {1: ['Burger', burger_quantity, 10],
             2: ['Pizza', pizza_quantity, 20],
             3: ['ColdDrink', colddrink_quantity, 10]}

print("!!!Welcome to Zomino!!!")
z = Zomino(menu_dict, burger_quantity, pizza_quantity, colddrink_quantity)
