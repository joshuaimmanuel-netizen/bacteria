
import random
import numpy as np

class Bacteria:
    def __init__(self, color, size, satiety=10):
        self.color = color 
        self.size = size
        self.satiety = satiety
        self.life = True
        self.time = 0
    
    def set_coords(self, screen_size: tuple):
        self.x = random.randint(15, screen_size[0] - self.size)
        self.y = random.randint(15, screen_size[1] - self.size)
        
    def get_coords(self):
        return (self.x, self.y, self.size, self.size)

    def get_satiety(self):
        return self.satiety
    
    def set_satiety(self, param):
        self.satiety = param

    def tick_time(self):
        self.time += 1
        if self.time > 500:
            self.life = False
        else:
            self.life = True

        return self.life


    
    


class Ameba(Bacteria):

    def change_coords(self, list_of_food):
        
        closest_food = None
        minimal_dist = float('inf')
        
        for food in list_of_food:
            food_x, food_y, *args = food.get_food_coords()
            distance = ((self.x - food_x) ** 2 + (self.y - food_y) ** 2) ** (1 / 2)

            if distance < minimal_dist:
                minimal_dist = distance
                closest_food = food.get_food_coords()   

            if distance < 2:
                list_of_food.remove(food)
                self.satiety += 1
                break              


        
        if closest_food is not None:

            decisions = (self.x, self.y, *closest_food)  #6 points array

            # self.x += (decisions[2] - decisions[0]) / 50 + np.sign((decisions[2] - decisions[0])) * 2
            # self.y += (decisions[3] - decisions[1]) / 50 + np.sign((decisions[3] - decisions[1])) * 2

            self.x += (decisions[2] - decisions[0]) / 10 
            self.y += (decisions[3] - decisions[1]) / 10 


