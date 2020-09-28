class PapaZones:
    def __init__(self):

        self.__burger_quantity = 0
        self.__pizza_quantity = 0
        self.__colddrink_quantity = 0
        self.__menu_dict = {1: ['Burger', self.__burger_quantity, 10],
                            2: ['Pizza', self.__pizza_quantity, 30],
                            3: ['ColdDrink', self.__colddrink_quantity, 10]}


    def ask_for_menu(self):
        print("!!! Welcome to PapaZones !!!")
        yes_no = True
        while yes_no:
            print("Todays Menu:- ")
            for i in self.__menu_dict:
                print(str(i) + ' ' + self.__menu_dict[i][0])
            item_selector = input("Enter the item which you want by using serial number: \n")

            if item_selector == '1':
                print("You selected " + self.__menu_dict[1][0] + '.')
                self.__menu_dict[1][1] = input("Enter Quantity: ")
                print("You selected " + str(self.__burger_quantity) + ' ' + self.__menu_dict[1][0] + '.')
                yes_no = input("Do you want to select more(Y/N): ")

            if item_selector == '2':
                print("You selected " + self.__menu_dict[2][0] + '.')
                self.__menu_dict[2][1] = input("Enter Quantity: ")
                print("You selected " + str(self.__burger_quantity) + ' ' + self.__menu_dict[2][0] + '.')
                yes_no = input("Do you want to select more(Y/N): ")

            if item_selector == '3':
                print("You selected " + self.__menu_dict[3][0] + '.')
                self.__menu_dict[3][1] = input("Enter Quantity: ")
                print("You selected " + str(self.__burger_quantity) + ' ' + self.__menu_dict[3][0] + '.')
                yes_no = input("Do you want to select more(Y/N): ")

            if yes_no == 'Y':
                yes_no = True

            if yes_no == 'N':
                self.total()
                yes_no = False

    def __total(self):
        print("Your total:- ")
        print('1. ' + self.__menu_dict[1][0] + "      " + str(self.__menu_dict[1][1]) + "    " + str(
            self.__menu_dict[1][2] * int(self.__menu_dict[1][1])))
        print('2. ' + self.__menu_dict[2][0] + "       " + str(self.__menu_dict[2][1]) + "    " + str(
            self.__menu_dict[2][2] * int(self.__menu_dict[2][1])))
        print(
            '3. ' + self.__menu_dict[3][0] + "   " + str(self.__menu_dict[3][1]) + "    " + str(
                self.__menu_dict[3][2] * int(self.__menu_dict[3][1])))
        print("TOTAL:-        " + str(
            int(self.__menu_dict[1][1]) + int(self.__menu_dict[2][1]) + int(
                self.__menu_dict[3][1])) + "    " + str(
            self.__menu_dict[1][2] * int(self.__menu_dict[1][1]) + self.__menu_dict[2][2] * int(self.__menu_dict[2][1]) + self.__menu_dict[3][2] * int(
                self.__menu_dict[3][1])))
