from Restaurants import *

class PapaZones(Restaurants):
    def __init__(self):
        menu_dict = {1: ['Burger', 10],
                            2: ['Pizza', 30],
                            3: ['ColdDrink', 10]}

        super().__init__('PapaZones', menu_dict, {})


