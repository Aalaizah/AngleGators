import pygame

class Alligator(pygame.sprite.Sprite):
    def __init__(self, currentImage):
        #super().__init__()
        # Create an image
        self.images = [pygame.image.load("Assets/gator0.png"),
            pygame.image.load("Assets/gator20.png"),
            pygame.image.load("Assets/gator45.png"),
            pygame.image.load("Assets/gator70.png"),
            pygame.image.load("Assets/gator90.png")]
        self.image = self.images[currentImage]
        self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.angle = 0
        self.angles = [0, 10, 20, 25, 50, 70, 75, 80, 90]

    def angle_index(self):
        if self.angle == 0:
            # image is mouth shut
            return 0
        elif self.angle > 0 and self.angle < 30:
            # image is mouth slightly open
            return 1
        elif self.angle > 29 and self.angle < 60:
            # image is mouth halfway open
            return 2
        elif self.angle > 59 and self.angle < 90:
            # Mouth is mostly open
            return 3
        elif self.angle == 90:
            # Mouth is all the way open
            return 4

    def change_angle(self, direction):
        if direction == "up":
            if self.angle < 90:
                self.angle = self.angles[self.angles.index(self.angle) + 1]
            else:
                self.angle = 90
        elif direction == "down":
            if self.angle > 0:
                self.angle = self.angles[self.angles.index(self.angle) - 1]
            else:
                self.angle = 0

    def draw(self, screen):
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render(str(self.angle), True, (33, 69, 30))
        screen.blit(text, [250, 350])
        screen.blit(self.images[self.angle_index()], [0, 400])