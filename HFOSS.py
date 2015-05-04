#!/usr/bin/python
import pygame
from gi.repository import Gtk
from enum import Enum

# TODO: move to a separate file?
class GameState(Enum):
	Menu = 0
	Playing = 1
	Paused = 2
	HowTo = 3
	Credits = 4

class HFOSS:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1
        self.currentState = GameState.Menu

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    def getNextScreen(e, curScreen):
        if curScreen == GameState.Menu:
            return GameState.Playing
        elif curScreen == GameState.Playing:
            return GameState.Menu

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()
        font = pygame.font.SysFont('Calibri', 25, True, False)

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            if 1 in pygame.mouse.get_pressed():
                print(pygame.mouse.get_pos())
                self.currentState = self.getNextScreen(self.currentState)
            if self.currentState == GameState.Menu:
                # TODO: game menu init here
                print('menu screen')
                text = font.render("AngleGators", True, (0, 0, 0))
            elif self.currentState == GameState.Playing:
                text = font.render("This will be the main game screen", True, (0, 0, 0))
                print('playing')
            elif self.currentState == GameState.Paused:
                print('paused')
                text = font.render("The game is paused", True, (0, 0, 0,))
                self.paused = True
            elif self.currentState == GameState.HowTo:
                print('HowTo')
                text = font.render("How To Play", True, (0, 0, 0))
            elif self.currentState == GameState.Credits:
                print('Credits')
                text = font.render('Mellolikejello, Mackster, Red-Two', True, (0,0,0))
            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1
                    elif event.key == pygame.K_ESCAPE:
                        return

            # Move the ball
            if not self.paused:
                self.x += self.vx * self.direction
                if self.direction == 1 and self.x > screen.get_width() + 100:
                    self.x = -100
                elif self.direction == -1 and self.x < -100:
                    self.x = screen.get_width() + 100

                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy

                self.vy += 5

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            screen.blit(text, [250,250])

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = HFOSS()
    game.run()

if __name__ == '__main__':
    main()
