#!/usr/bin/python
import pygame
from gi.repository import Gtk
import sys

from Food import FoodManager, Food
from FontItem import FontItem, FontButton
from GameMenu import GameMenu

class GameState():
	Menu = 0
	Playing = 1
	Paused = 2
	HowTo = 3
	Credits = 4

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

class Conveyor(pygame.sprite.Sprite):
    def __init__(self):
        #load conveyor image
        self.image = pygame.image.load("Assets/environment/conveyorbelt.png")
        self.image.convert()
        self.rect = self.image.get_rect()

class AngleGators:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False
        self.currentState = GameState.Menu
        self.angle = 0 
        self.angles = [0, 10, 20, 25, 50, 70, 75, 80, 90]

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    def alligator(self):
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
            print(Angles[1])
        elif direction == "down":
            print("hi")
    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()
        font = pygame.font.SysFont(None, 25, True, False)
        gator = None
        text = None
        conveyor = None
        food_manager = FoodManager()
        food_manager.generate_food()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            if self.currentState == GameState.Menu:
                menu_items = (FontButton('Start'), FontButton('How to Play'),
                              FontButton('Credits'), FontButton('Quit'))
                gm = GameMenu(screen, menu_items, 'AngleGators')
                response = gm.run()
                if response == 'Start':
                    self.currentState = GameState.Playing
                elif response == 'How to Play':
                    self.currentState = GameState.HowTo
                elif response == 'Credits':
                    self.currentState = GameState.Credits
                elif response == 'Quit':
                    return
                #print('menu screen')
            elif self.currentState == GameState.Playing:
                text = font.render(str(self.angle), True, (33, 69, 30))
                gator = Alligator(self.alligator())
                conveyor = Conveyor()
            elif self.currentState == GameState.Paused:
                text_items = (FontButton('Resume'),FontButton('Return to Main Menu'), FontButton('Quit'))
                ps = GameMenu(screen, text_items, 'Game is Paused')
                response = ps.run()
                if response == 'Resume':
                    self.currentState = GameState.Playing
                elif response == 'Return to Main Menu':
                    self.currentState = GameState.Menu
                elif response == 'Quit':
                    return
                self.paused = True
            elif self.currentState == GameState.HowTo:
                text_items = (FontItem('Open the Alligators mouth to eat the object'),
                              FontItem('Use the left arrow to open it\'s mouth more'),
                              FontItem('Use the right arrow to close it\'s mouth'),
                              FontButton('Back'))
                ht = GameMenu(screen, text_items, 'How To Play')
                response = ht.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
            elif self.currentState == GameState.Credits:
                #print('Credits')
                text_items = (FontItem('Programmers: Melody Kelly, Alex Mack, William Russell'),
                              FontItem('Artwork: Jackie Wiley'),
                              FontButton('Back'))
                cm = GameMenu(screen, text_items, 'Credits')
                response = cm.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.angle < 90:
                         self.angle = self.angles[self.angles.index(self.angle) + 1]
                        else:
                            self.angle = 90
                    elif event.key == pygame.K_RIGHT:
                        if self.angle > 0:
                            self.angle = self.angles[self.angles.index(self.angle) - 1]
                        else:
                            self.angle = 0
                    elif event.key == pygame.K_ESCAPE:
                        self.currentState = GameState.Paused

            # Clear Display
            #screen.fill((255, 108, 0))  # 255 for white
            background = pygame.image.load("Assets/mainbackground.png")
            screen.blit(background, [0, 0])

            #all_sprites_list.clear(background, [255, 108, 0])

            #all_sprites_list.draw(screen)
            if(gator != None):
                screen.blit(gator.image, [0, (screen.get_height() - gator.rect.height)])
            if(text != None):
                screen.blit(text, [250,(screen.get_height() - gator.rect.height)])
            if(conveyor != None):
                screen.blit(conveyor.image, [(screen.get_width() - gator.rect.width - 100), screen.get_height() - (gator.rect.height/1.8)])
#                foodCount = 10
#                for food in foods:
#                    screen.blit(food.image, [300, foodCount])
#                    foodCount += 50
                food_manager.draw(screen)
            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./angle_gators.py
def main():
    pygame.init()
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    if(float(screen_width)/float(screen_height) == float(4)/float(3)):
        screenSize = (screen_width,screen_height)
    else:
        screenSize = (800,600)
    pygame.display.set_mode(screenSize)
    pygame.display.set_caption('AngleGators')
    game = AngleGators()
    game.run()

if __name__ == '__main__':
    main()
