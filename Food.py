import pygame

class Food(pygame.sprite.Sprite):
    """Food element for game"""
    def __init__(self, index):
        # Create an image
        self.images = [pygame.image.load("Assets/foods/acorn.png"),
            pygame.image.load("Assets/foods/apple.png"),
            pygame.image.load("Assets/foods/appleslice.png"),
            pygame.image.load("Assets/foods/grapes.png"),
            pygame.image.load("Assets/foods/lemon.png"),
            pygame.image.load("Assets/foods/onion.png"),
            pygame.image.load("Assets/foods/orange.png"),
            pygame.image.load("Assets/foods/orangeslice.png"),
            pygame.image.load("Assets/foods/peach.png"),
            pygame.image.load("Assets/foods/strawberry.png"),
            pygame.image.load("Assets/foods/tomato.png"),
            pygame.image.load("Assets/foods/watermelon.png"),
            pygame.image.load("Assets/foods/yam.png"),
            pygame.image.load("Assets/foods/zucchini.png")]
        self.image = self.images[index]
        self.min_angle = 10
        self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def set_min_angle(self, angle):
        """Set the minimum angle required to eat this Food"""
        self.min_angle = angle;

    def set_position(self, x, y):
        """Set the position of this Food"""
        self.pos_x = x
        self.pos_y = y
