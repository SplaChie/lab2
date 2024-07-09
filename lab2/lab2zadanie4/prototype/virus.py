import copy

class Virus:
    def __init__(self, name, weight, age, species, children=None):
        self.name = name
        self.weight = weight
        self.age = age
        self.species = species
        self.children = children if children else []

    def clone(self):
        # Глибоке копіювання всіх властивостей
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} ({self.species}), {self.weight}kg, {self.age} years old, {len(self.children)} children"

# Створення вірусів і клонування
parent_virus = Virus("Parent", 10, 2, "Type A")
child_virus1 = Virus("Child1", 1, 0.5, "Type A")
child_virus2 = Virus("Child2", 1.2, 0.6, "Type A")

parent_virus.children.extend([child_virus1, child_virus2])

cloned_virus = parent_virus.clone()
