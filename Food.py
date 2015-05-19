import pygame
import math, random

class FoodManager():
    def __init__(self):
        self.food_list = [ { "name": "acorn",
                      "img": pygame.image.load("Assets/foods/acorn.png"),
                      "min_angle": 10 },
                     { "name": "apple",
                      "img": pygame.image.load("Assets/foods/apple.png"),
                      "min_angle": 20 },
                    { "name": "appleslice",
                      "img": pygame.image.load("Assets/foods/appleslice.png"),
                      "min_angle": 20 },
                    { "name": "grapes",
                      "img": pygame.image.load("Assets/foods/grapes.png"),
                      "min_angle": 50 },
                    { "name": "lemon",
                      "img": pygame.image.load("Assets/foods/lemon.png"),
                      "min_angle": 30 },
                    { "name": "onion",
                      "img": pygame.image.load("Assets/foods/onion.png"),
                      "min_angle": 40 },
                    { "name": "orange",
                      "img": pygame.image.load("Assets/foods/orange.png"),
                      "min_angle": 40 },
                    { "name": "orangeslice",
                      "img": pygame.image.load("Assets/foods/orangeslice.png"),
                      "min_angle": 20 },
                    { "name": "peach",
                      "img": pygame.image.load("Assets/foods/peach.png"),
                      "min_angle": 30 },
                    { "name": "strawberry",
                      "img": pygame.image.load("Assets/foods/strawberry.png"),
                      "min_angle": 20 },
                    { "name": "tomato",
                      "img": pygame.image.load("Assets/foods/tomato.png"),
                      "min_angle": 30 },
                    { "name": "watermelon",
                      "img": pygame.image.load("Assets/foods/watermelon.png"),
                      "min_angle": 70 },
                    { "name": "yam",
                      "img": pygame.image.load("Assets/foods/yam.png"),
                      "min_angle": 50 },
                    { "name": "zucchini",
                      "img": pygame.image.load("Assets/foods/zucchini.png"),
                      "min_angle": 50 }
                   ]
        self.num_foods = len(self.food_list)
        self.active = []
        self.isStarted = False

    def generate_food(self):
        self.isStarted = True
        index = int(math.floor(random.random() * self.num_foods))
        selected_food = self.food_list[index]
        new_food = Food(selected_food["name"], selected_food["img"],
                        selected_food["min_angle"])
        self.active.append(new_food)
        print(new_food.name)

    def draw(self, screen):
        for food in self.active:
            screen.blit(food.image, [food.pos_x, food.pos_y])
            food.move()
            if(food.pos_x <= 0):
#                food is off screen
                self.active.pop(0)
                self.generate_food()

    def reset(self):
        self.active = []
        self.isStarted = False

class Food(pygame.sprite.Sprite):
    """Food element for game"""
    def __init__(self, name, img, min_angle):
        self.name = name
        self.image = img
        self.min_angle = min_angle
        self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.pos_x = 1200
        self.pos_y = 550
        self.speed = -10

    def set_min_angle(self, angle):
        """Set the minimum angle required to eat this Food"""
        self.min_angle = angle;

    def set_position(self, x, y):
        """Set the position of this Food"""
        self.pos_x = x
        self.pos_y = y

    def move(self):
        self.pos_x += self.speed
