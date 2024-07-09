class Hero:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = None
        self.inventory = []

    def __str__(self):
        return f"Hero: {self.height}, {self.build}, {self.hair_color}, {self.eye_color}, {self.clothing}, {self.inventory}"

class HeroBuilder:
    def __init__(self):
        self.hero = Hero()

    def set_height(self, height):
        self.hero.height = height
        return self

    def set_build(self, build):
        self.hero.build = build
        return self

    def set_hair_color(self, hair_color):
        self.hero.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.hero.eye_color = eye_color
        return self

    def set_clothing(self, clothing):
        self.hero.clothing = clothing
        return self

    def add_inventory(self, item):
        self.hero.inventory.append(item)
        return self

    def build(self):
        return self.hero
