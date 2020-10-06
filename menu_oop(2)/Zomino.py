class Zominoes:
    def __init__(self):

        self.__order = {}

        self.__menu_dict = {1: ['Burger', 10],
                            2: ['Pizza', 30],
                            3: ['ColdDrink', 10],
                            4: ['Thali', 50],
                            5: ['Ham', 100]}

    def ask_for_menu(self):

        print("!!! Welcome to Zominoes !!!")
        yes_no = True
        while yes_no:
            print("Todays Menu:- ")
            for i in self.__menu_dict:
                print(str(i) + ' ' + self.__menu_dict[i][0])

            item_selector = int(input("Enter the item which you want by using serial number: \n"))

            quantity = 0
            q1 = 0
            for key in self.__menu_dict:
                if item_selector == key:
                    print("You selected " + self.__menu_dict[key][0] + '.')

                    quantity = quantity + int(input("Enter Quantity: "))

                    print("You selected ", quantity, ' ', self.__menu_dict[key][0], '.')
                    val2 = {self.__menu_dict[key][0]: quantity}
                    self.__order.update(val2)
                    # q1 = self.__order[self.__menu_dict[key][0]] + quantity

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

        """for i in range(len(self.__order)):
            print(i + 1, '  ', keys[i], '  ', self.__order[keys[i]], '  ', self.__order[keys[i]] * price[i])

        for i in range(len(self.__order)):
            total_quantity.append(self.__order[keys[i]])

        for i in total_quantity:
            total_quantity_answer = total_quantity_answer + i

        for i in range(len(self.__order)):
            total_price.append(self.__order[keys[i]] * price[i])

        for i in total_price:
            total_price_answer = total_price_answer + i

        print('TOTAL: ', total_quantity_answer, total_price_answer)"""

        """val = []
        for i in self.__order.values():
            val.append(i)

        print("Your total:- ")
        for i in range(len(self.__order)):
            print(i + 1, '  ', self.__menu_dict[i + 1][0], '  ',
                  val[i], '  ',
                  val[i] * self.__menu_dict[i + 1][1])

        answer = 0

        # print("TOTAL: ")
        t_quantity = self.__order.values()
        for i in self.__order.values():
            val.append(i)

        for i in self.__order.values():
            total_quantity.append(i)

        for i in range(len(total_quantity)):
            answer = answer + total_quantity[i]

        total_price = []
        answer2 = 0

        for i in range(len(self.__order)):
            total_price.append(total_quantity[i] * self.__menu_dict[i + 1][1])

        for i in range(len(total_price)):
            answer2 = answer2 + total_price[i]

        print('TOTAL:       ', answer, '   ', answer2)"""

        """print("TOTAL: ", self.__order[self.__menu_dict[1][0]] + self.__order[self.__menu_dict[2][0]] + self.__order[
            self.__menu_dict[3][0]], '   ',
              self.__order[self.__menu_dict[1][0]] * self.__menu_dict[1][1] + self.__order[self.__menu_dict[2][0]] *
              self.__menu_dict[2][1] + self.__order[self.__menu_dict[3][0]] * self.__menu_dict[3][1])"""

        """print('1. ' + self.__menu_dict[1][0] + "      " + str(self.__menu_dict[1][1]) + "    " + str(
            self.__menu_dict[1][2] * int(self.__menu_dict[1][1])))
        print('2. ' + self.__menu_dict[2][0] + "       " + str(self.__menu_dict[2][1]) + "    " + str(
            self.__menu_dict[2][2] * int(self.__menu_dict[2][1])))
        print(
            '3. ' + self.__menu_dict[3][0] + "   " + str(self.__menu_dict[3][1]) + "    " + str(
                self.__menu_dict[3][2] * int(self.__menu_dict[3][1])))
        print("TOTAL:-        " + str(
            int(self.__menu_dict[1][1]) + int(self.__menu_dict[2][1]) + int(
                self.__menu_dict[3][1])) + "    " + str(
            self.__menu_dict[1][2] * int(self.__menu_dict[1][1]) + self.__menu_dict[2][2] * int(
                self.__menu_dict[2][1]) + self.__menu_dict[3][2] * int(
                self.__menu_dict[3][1])))"""
