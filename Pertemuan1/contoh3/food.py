class Food:
    def __init__(self):
        self._topping1 = None
        self._topping2 = None

    @property
    def topping1(self):
        return self._topping1
    
    @topping1.setter
    def topping1(self, value):
        self._topping1 = value

    @property
    def topping2(self):
        return self._topping2
    
    @topping2.setter
    def topping2(self, value):
        self._topping2 = value

    def serveFood(self):
        print(f"Bakso dengan topping {self.topping1} dan {self.topping2}")

food = Food()
topping1 = input("Masukan Topping 1 : ")
topping2 = input("Masukan Topping 2 : ")

food.topping1 = topping1
food.topping2 = topping2
food.serveFood()