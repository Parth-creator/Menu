class Zomino:

    def __init__(self, menu_dict, burger_quantity, pizza_quantity, colddrink_quantity):
        self.menu_dict = menu_dict
        self.burger_quantity = burger_quantity
        self.pizza_quantity = pizza_quantity
        self.colddrink_quantity = colddrink_quantity
        self.ask_for_menu()

    def ask_for_menu(self):

        while True:
            print("Today's menu:- ")
            print('1. ' + self.menu_dict[1][0] + "      " + str(self.menu_dict[1][2]))
            print('2. ' + self.menu_dict[2][0] + "       " + str(self.menu_dict[2][2]))
            print('3. ' + self.menu_dict[3][0] + "   " + str(self.menu_dict[3][2]))
            item_selector = input("Enter the item which you want by using serial number: ")
            if item_selector == '1':
                print("you selected " + self.menu_dict[1][0] + ".")
                self.burger_quantity = input("Enter Quantity: ")
                print("You selected " + self.burger_quantity + ' ' + self.menu_dict[1][0] + '.')
                yes_no = input("Do you want to select more(y/n): ")

            if item_selector == '2':
                print("you selected " + self.menu_dict[2][0] + ".")
                self.pizza_quantity = input("Enter Quantity: ")
                print("You selected " + self.pizza_quantity + ' ' + self.menu_dict[2][0] + '.')
                yes_no = input("Do you want to select more(y/n): ")

            if item_selector == '3':
                print("you selected " + self.menu_dict[3][0] + ".")
                self.colddrink_quantity = input("Enter Quantity: ")
                print("You selected " + self.colddrink_quantity + ' ' + self.menu_dict[3][0] + '.')
                yes_no = input("Do you want to select more(y/n): ")

            if yes_no == 'y':
                pass
            if yes_no == 'n':
                self.total()
                exit()

    def total(self):
        print("Your total:- ")
        print('1. ' + self.menu_dict[1][0] + "      " + str(self.burger_quantity) + "    " + str(10 * int(self.burger_quantity)))
        print('2. ' + self.menu_dict[2][0] + "       " + str(self.pizza_quantity) + "    " + str(10 * int(self.pizza_quantity)))
        print(
            '3. ' + self.menu_dict[3][0] + "   " + str(self.colddrink_quantity) + "    " + str(10 * int(self.colddrink_quantity)))
        print("TOTAL:-        " + str(
            int(self.burger_quantity) + int(self.pizza_quantity) + int(self.colddrink_quantity)) + "    " + str(
            10 * int(self.burger_quantity) + 10 * int(self.pizza_quantity) + 10 * int(self.colddrink_quantity)))











