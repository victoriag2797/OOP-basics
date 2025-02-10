import random

class Character:
    hair_colors = ["Blonde", "Brown", "Black", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Telepathy", "Metal bending", "Fire control", "Super Strength"]
    style = ["Alternative", "Goth", "Basic", "Indie", "Vintage", "Artsy", "Preppy"]

    #Constructor
    def __init__(self):
        self.generate_character()

    def generate_character():
        self.hair_colors = random.choice(Character.hair_colors)
        self.sizes = random.choice(Character.sizes)
        self.special_powers = random.choice(Character.special_powers)
        self.style = random.choice(Character.style)
        self.description = (
            f"Your Character has {self.hair_colors} hair,"
            f"is {self.sizes} in size, and has the power of {self.special_powers} and a {self.style} style."
        )

    def __str__(self):
        return self.description

char1 = Character()
char2 = Character()

print(char1)
print(char2)