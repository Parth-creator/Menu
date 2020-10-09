class Parent:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

        print("Parent, ")

    def sum(self):
        global answer
        answer = self.num1 + self.num2 + self.num3
        print(answer)

        self.faltu()

    def faltu(self):
        print(answer*6)

class Child(Parent):
    def __init__(self):
        self.num1 = 1
        self.num2 = 2
        self.num3 = 3

        print("Child, ")
        super().__init__(self.num1, self.num2, self.num3)


child = Child()
child.sum()
