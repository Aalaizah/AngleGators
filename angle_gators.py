#!/usr/bin/python
import pygame
from gi.repository import Gtk
import sys

from Food import FoodManager, Food
from FontItem import FontItem, FontButton
from Scene import MenuScene, GameScene
from Alligator import Alligator

class GameState():
	Menu = 0
	Playing = 1
	Paused = 2
	HowTo = 3
	Credits = 4

class AngleGators:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False
        self.currentState = GameState.Menu

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

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
        background_imgs = { "main": pygame.image.load("Assets/mainbackground.png"),
                            "play": pygame.image.load("Assets/playbackground.png")}

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            if self.currentState == GameState.Menu:
                menu_items = (FontButton('Start'), FontButton('How to Play'),
                              FontButton('Credits'), FontButton('Quit'))
                gm = MenuScene(screen, menu_items, 'AngleGators', 'Assets/mainbackground.png')
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
                game_scene = GameScene(screen)
                response = game_scene.run()
                if response == 'Quit':
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    return
                elif response == 'Pause':
                    self.currentState = GameState.Paused
            elif self.currentState == GameState.Paused:
                text_items = (FontButton('Resume'),FontButton('Return to Main Menu'), FontButton('Quit'))
                ps = MenuScene(screen, text_items, 'Game is Paused', 'Assets/playbackground.png')
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
                ht = MenuScene(screen, text_items, 'How To Play', 'Assets/mainbackground.png')
                response = ht.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
            elif self.currentState == GameState.Credits:
                #print('Credits')
                text_items = (FontItem('Programmers: Melody Kelly, Alex Mack, William Russell'),
                              FontItem('Artwork: Jackie Wiley'),
                              FontButton('Back'))
                cm = MenuScene(screen, text_items, 'Credits', 'Assets/mainbackground.png')
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
#            screen.blit(cur_background, [0, 0])

            #all_sprites_list.clear(background, [255, 108, 0])

            #all_sprites_list.draw(screen)

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
        screenSize = (1200, 900)
    pygame.display.set_mode(screenSize)
    pygame.display.set_caption('AngleGators')
    game = AngleGators()
    game.run()

if __name__ == '__main__':
    main()
