class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"{self.__class__.__name__} by {self.brand}"

class IProneLaptop(Laptop):
    def __init__(self):
        super().__init__("IProne")

class XiaomiLaptop(Laptop):
    def __init__(self):
        super().__init__("Xiaomi")

class GalaxyLaptop(Laptop):
    def __init__(self):
        super().__init__("Galaxy")
