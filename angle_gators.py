#!/usr/bin/python
import pygame
from gi.repository import Gtk
import sys

from FontItem import FontItem, FontButton
from Scene import MenuScene, GameScene

class GameState():
    Menu = 0
    Playing = 1
    Paused = 2
    HowTo = 3
    Credits = 4
    Gameover = 5


class AngleGators:
    def __init__(self):
        pygame.init()
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        if(float(screen_width)/float(screen_height) == float(4)/float(3)):
            screenSize = (screen_width,screen_height)
        else:
            screenSize = (1200, 900)
        pygame.display.set_mode(screenSize)
        pygame.display.set_caption('AngleGators')

        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.paused = False
        self.currentState = GameState.Menu
        self.finalScore = 0

        self.screen = pygame.display.get_surface()
        self.scenes = self.generate_scenes()

    def generate_scenes(self):
        scenes = []

        main_menu_items = (FontButton('Start'), FontButton('How to Play'),
                              FontButton('Credits'), FontButton('Quit'))
        main_menu_scene = MenuScene(self.screen, main_menu_items, 'AngleGators',
                                    'Assets/mainbackground_tail.png')

        game_scene = GameScene(self.screen)

        pause_scene_items = (FontButton('Resume'),
                             FontButton('Return to Main Menu'),
                             FontButton('Quit'))
        pause_scene = MenuScene(self.screen, pause_scene_items, 'Game is Paused',
                                'Assets/playbackground.png')

        howto_scene_items = (FontItem('Open the Alligators mouth to eat the object'),
                              FontItem('Use the left arrow to open its mouth more'),
                              FontItem('Use the right arrow to close its mouth'),
                              FontButton('Back'))
        howto_scene = MenuScene(self.screen, howto_scene_items, 'How To Play',
                                'Assets/mainbackground.png')

        credits_scene_items = (FontItem('Programmers: Melody Kelly, Alex Mack, Alex Russell'),
                              FontItem('Artwork: Jackie Wiley'),
                              FontButton('Back'))
        credits_scene = MenuScene(self.screen, credits_scene_items, 'Credits',
                                  'Assets/mainbackground.png')

        gameover_scene_items = (FontItem('Score: '),
                                FontButton('Restart Game'),
                                FontButton('Return to Main Menu'),
                                FontButton('Quit'))
        gameover_scene = MenuScene(self.screen, gameover_scene_items, 'Game Over',
                                    'Assets/mainbackground.png')

        scenes.insert(GameState.Menu, main_menu_scene)
        scenes.insert(GameState.Playing, game_scene)
        scenes.insert(GameState.Paused, pause_scene)
        scenes.insert(GameState.HowTo, howto_scene)
        scenes.insert(GameState.Credits, credits_scene)
        scenes.insert(GameState.Gameover, gameover_scene)

        return scenes

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            if self.currentState == GameState.Menu:
                gm = self.scenes[GameState.Menu]
                response = gm.run()
                if response == 'Start':
                    self.currentState = GameState.Playing
                elif response == 'How to Play':
                    self.currentState = GameState.HowTo
                elif response == 'Credits':
                    self.currentState = GameState.Credits
                elif response == 'Quit':
                    return
            elif self.currentState == GameState.Playing:
                game_scene = self.scenes[GameState.Playing]
                response = game_scene.run()
                if response == 'Quit':
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    return
                elif response == 'Pause':
                    self.currentState = GameState.Paused
                elif response[0] == 'Game Over':
                    self.finalScore = response[1]
                    self.currentState = GameState.Gameover 
            elif self.currentState == GameState.Paused:
                ps = self.scenes[GameState.Paused]
                response = ps.run()
                if response == 'Resume':
                    self.currentState = GameState.Playing
                elif response == 'Return to Main Menu':
                    self.currentState = GameState.Menu
                    self.scenes[GameState.Playing].reset()
                elif response == 'Quit':
                    return
                self.paused = True
            elif self.currentState == GameState.HowTo:
                ht = self.scenes[GameState.HowTo]
                response = ht.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
            elif self.currentState == GameState.Credits:
                cm = self.scenes[GameState.Credits]
                response = cm.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
            elif self.currentState == GameState.Gameover:
                gameover_scene_items = (FontItem(('Score: ' + str(self.finalScore))),
                                FontButton('Restart Game'),
                                FontButton('Return to Main Menu'),
                                FontButton('Quit'))

                gom = MenuScene(self.screen, gameover_scene_items, 'Game Over',
                                    'Assets/mainbackground.png')
                
                response = gom.run()
                if response == 'Restart Game':
                    self.scenes[GameState.Playing].reset()
                    self.currentState = GameState.Playing
                elif response == 'Return to Main Menu':
                    self.currentState = GameState.Menu
                    self.scenes[GameState.Playing].reset()
                elif response == 'Quit':
                    return

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    return

            #all_sprites_list.clear(background, [255, 108, 0])

            #all_sprites_list.draw(screen)

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./angle_gators.py
def main():
    game = AngleGators()
    game.run()

if __name__ == '__main__':
    main()
