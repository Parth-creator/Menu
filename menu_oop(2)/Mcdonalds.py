from Restaurants import *

class Mcdonalds(Restaurants):
    def __init__(self):
        menu_dict = {1: ['Burger', 10],
                            2: ['Chicken Burger', 30],
                            3: ['ColdDrink', 10]}

        super().__init__('McDonalds', menu_dict, {})

