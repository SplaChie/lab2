class Smartphone:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"{self.__class__.__name__} by {self.brand}"

class IProneSmartphone(Smartphone):
    def __init__(self):
        super().__init__("IProne")

class XiaomiSmartphone(Smartphone):
    def __init__(self):
        super().__init__("Xiaomi")

class GalaxySmartphone(Smartphone):
    def __init__(self):
        super().__init__("Galaxy")
