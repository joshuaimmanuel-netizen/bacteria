import random

class Food:

    def __init__(self, color, size=5):
        self.color = color
        self.size = size

    
    def set_food_coords(self, screen_size: tuple):
        self.x = random.randint(self.size, screen_size[0] - self.size)
        self.y = random.randint(self.size, screen_size[1] - self.size)
        
    def get_food_coords(self):
        return (self.x, self.y, self.size, self.size)


