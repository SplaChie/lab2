class Enemy:
    def __init__(self):
        self.height = None
        self.build = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = None
        self.inventory = []

    def __str__(self):
        return f"Enemy: {self.height}, {self.build}, {self.hair_color}, {self.eye_color}, {self.clothing}, {self.inventory}"

class EnemyBuilder:
    def __init__(self):
        self.enemy = Enemy()

    def set_height(self, height):
        self.enemy.height = height
        return self

    def set_build(self, build):
        self.enemy.build = build
        return self

    def set_hair_color(self, hair_color):
        self.enemy.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color):
        self.enemy.eye_color = eye_color
        return self

    def set_clothing(self, clothing):
        self.enemy.clothing = clothing
        return self

    def add_inventory(self, item):
        self.enemy.inventory.append(item)
        return self

    def build(self):
        return self.enemy
