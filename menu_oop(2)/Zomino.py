from Restaurants import *


class Zominoes(Restaurants):


    def __init__(self):

        menu_dict = {1: ['Burger', 10],
                     2: ['Pizza', 30],
                     3: ['ColdDrink', 10],
                     4: ['Thali', 50],
                     5: ['Ham', 100]}

        super().__init__('Zomino', menu_dict, {})
        """self.__order = {}

        self.__menu_dict = {1: ['Burger', 10],
                     2: ['Pizza', 30],
                     3: ['ColdDrink', 10],
                     4: ['Thali', 50],
                     5: ['Ham', 100]}"""

    """def __init__(self):
        super().__init__('Zomino', self.__menu_dict, self.__order)

        self.__order = {}

        self.__menu_dict = {1: ['Burger', 10],
                            2: ['Pizza', 30],
                            3: ['ColdDrink', 10],
                            4: ['Thali', 50],
                            5: ['Ham', 100]}"""
