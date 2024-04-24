class Bakso:
    def __init__(self):
        self.topping1 = None
        self.topping2 = None

    def getData(self, topping1, topping2):
        self.topping1 = topping1
        self.topping2 = topping2

    def serveFood(self):
        print(f"Bakso dengan topping {self.topping1} dan {self.topping2}")

food = Bakso()
topping1 = input("Masukan Topping 1 : ")
topping2 = input("Masukan Topping 2 : ")

food.getData(topping1, topping2)
food.serveFood()