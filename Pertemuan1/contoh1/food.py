class Bakso:
    def __init__(self, topping1, topping2):
        self.topping1 = topping1
        self.topping2 = topping2

    def serveFood(self):
        print(f"Bakso dengan topping {self.topping1} dan {self.topping2}")

food = Bakso("Mie", "Pangsit")
food.serveFood()