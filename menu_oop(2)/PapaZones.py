class PapaZones:
    def __init__(self):

        self.__order = {}

        self.__menu_dict = {1: ['Burger', 10],
                            2: ['Pizza', 30],
                            3: ['ColdDrink', 10]}

    def ask_for_menu(self):

        print("!!! Welcome to Zominoes !!!")
        yes_no = True
        while yes_no:
            print("Todays Menu:- ")
            for i in self.__menu_dict:
                print(str(i) + ' ' + self.__menu_dict[i][0])

            item_selector = int(input("Enter the item which you want by using serial number: \n"))

            quantity = 0

            for key in self.__menu_dict:
                if item_selector == key:
                    print("You selected " + self.__menu_dict[key][0] + '.')

                    quantity = quantity + int(input("Enter Quantity: "))

                    print("You selected ", quantity, ' ', self.__menu_dict[key][0], '.')
                    val2 = {self.__menu_dict[key][0]: quantity}
                    self.__order.update(val2)

            yes_no = input("Do you want to select more(Y/N): ")

            if yes_no == 'Y':
                yes_no = True

            if yes_no == 'N':
                """print(1, '  ', self.__menu_dict[1][0], '  ', self.__order[self.__menu_dict[1][0]], '  ',
                      self.__order[self.__menu_dict[1][0]] * self.__menu_dict[1][1])"""
                self.__total()
                # print(self.__order)
                yes_no = False

    def __total(self):

        keys = []
        price = []
        total_quantity = []
        total_price = []
        total_quantity_answer = 0
        total_price_answer = 0

        print("Your total: ")

        for i in self.__order:
            keys.append(i)

        for i in range(len(keys)):
            for j in self.__menu_dict:
                if keys[i] == self.__menu_dict[j][0]:
                    price.append(self.__menu_dict[j][1])

        for i in range(len(self.__order)):
            print(i + 1, '  ', keys[i], '  ', self.__order[keys[i]], '  ', self.__order[keys[i]] * price[i])

        for i in range(len(self.__order)):
            total_quantity.append(self.__order[keys[i]])

        for i in total_quantity:
            total_quantity_answer = total_quantity_answer + i

        for i in range(len(self.__order)):
            total_price.append(self.__order[keys[i]] * price[i])

        for i in total_price:
            total_price_answer = total_price_answer + i

        print('TOTAL: ', total_quantity_answer, total_price_answer)
