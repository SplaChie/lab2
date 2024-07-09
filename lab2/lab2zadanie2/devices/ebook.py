class EBook:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"{self.__class__.__name__} by {self.brand}"

class IProneEBook(EBook):
    def __init__(self):
        super().__init__("IProne")

class XiaomiEBook(EBook):
    def __init__(self):
        super().__init__("Xiaomi")

class GalaxyEBook(EBook):
    def __init__(self):
        super().__init__("Galaxy")
