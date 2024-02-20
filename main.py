import pygame
import sys
import random
from food import Food
from bacteria import Ameba


FPS = 60
 
pygame.init()

screen_sizes = (1000, 900)
screen = pygame.display.set_mode(screen_sizes)
clock = pygame.time.Clock()
pygame.display.update()




num_food = 200
main_food_list = []


# генерация еды
def generate_food(food_list):
    color_food = (0, 111, 111)
    
    for i in range(num_food):
        new_food = Food(color_food)
        new_food.set_food_coords(screen_sizes)
        food_list.append(new_food)

    return food_list


main_food_list = generate_food(main_food_list)


# amebs
color_ameba = (222, 222, 0)
ameba1 = Ameba(color_ameba, 15, 10)
ameba1.set_coords(screen_sizes)

amebs = []
amebs.append(ameba1)


while True:
 
    clock.tick(FPS)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255)) 
    
    for food_instance in main_food_list:
        if len(main_food_list) <= 3/5 * num_food:
            main_food_list = generate_food(main_food_list)
        pygame.draw.rect(screen, food_instance.color, pygame.Rect(food_instance.get_food_coords()))


    for ameb in amebs:
        print(ameb.get_satiety())

        
        pygame.draw.rect(screen, ameb.color, pygame.Rect(ameb.get_coords()))
        ameb.change_coords(main_food_list)

        if ameb.tick_time():
            print('time is on: ', ameb.time)
            print('общее кол-во амебусов ============', len(amebs))

        else:
            amebs.remove(ameb)
            print('time is off: ', ameb.time)
            continue

        if ameb.get_satiety() > 5:
            ameba_reproduction = Ameba(ameb.color, ameb.size, 10)
            ameba_reproduction.x = ameb.x + random.randint(-110, 110)
            ameba_reproduction.y = ameb.y + random.randint(-110, 110)
            ameba_reproduction.color = ameb.color # идея с изменением цвета
            ameba_reproduction.set_satiety(0) 
            ameb.set_satiety(0) 


            amebs.append(ameba_reproduction)    

    pygame.display.flip()

pygame.quit()