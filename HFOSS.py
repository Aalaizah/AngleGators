#!/usr/bin/python
import pygame
from gi.repository import Gtk
import sys

# TODO: move to a separate file?
class GameState():
	Menu = 0
	Playing = 1
	Paused = 2
	HowTo = 3
	Credits = 4

class FontItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x=0, pos_y=0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def is_mouse_selection(self, posx_posy):
        posx, posy = posx_posy
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class GameMenu():
    def __init__(self, screen, items, title, bg_color=(255, 108, 0), font=None,
                    font_size=30, font_color=(0,0,0)):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.title = FontItem(title).set_font_color((0, 0, 0))
        #self.title_label = pygame.font.Font.render(self.title, 1, self.font_color)

        self.items = []
        for index, item in enumerate(items):
            menu_item = FontItem(item)

            #t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 fps
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            return item.text

            # Redraw the background
            self.screen.fill(self.bg_color)

            for item in self.items:
                if item.is_mouse_selection(pygame.mouse.get_pos()):
                    item.set_font_color((255, 255, 255))
                else:
                    item.set_font_color((0, 0, 0))
                self.screen.blit(item.label, item.position)

            pygame.display.flip()

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
        self.angle = 0

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


    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()
        font = pygame.font.SysFont(None, 25, True, False)
        gator = None
        text = None

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            #if 1 in pygame.mouse.get_pressed():
                #print(pygame.mouse.get_pos())
                #self.currentState = self.getNextScreen(self.currentState)
            if self.currentState == GameState.Menu:
                # TODO: game menu init here
                menu_items = ('Start', 'Credits', 'Quit')
                gm = GameMenu(screen, menu_items, 'AngleGators')
                response = gm.run()
                if response == 'Start':
                    self.currentState = GameState.Playing
                elif response == 'Credits':
                    self.currentState = GameState.Credits
                elif response == 'Quit':
                    return
                #print('menu screen')
                #text = font.render("AngleGators", True, (0, 0, 0))
            elif self.currentState == GameState.Playing:
                text = font.render(str(self.angle), True, (0, 0, 0))
                gator = Alligator(self.alligator())
            elif self.currentState == GameState.Paused:
                print('paused')
                text_items = ('Resume','Return to Main Menu', 'Quit')
                ps = GameMenu(screen, text_items, 'Game is Paused')
                response = ps.run()
                if response == 'Resume':
                    self.currentState = GameState.Playing
                elif response == 'Return to Main Menu':
                    self.currentState = GameState.Menu
                elif response == 'Quit':
                    return
                #text = font.render("The game is paused", True, (0, 0, 0,))
                self.paused = True
            elif self.currentState == GameState.HowTo:
                print('HowTo')
                text = font.render("How To Play", True, (0, 0, 0))
            elif self.currentState == GameState.Credits:
                #print('Credits')
                text_items = ('Programmers: Melody Kelly, Alex Mack, William Russel', 
                                'Artwork: Jackie Wiley', 'Back')
                cm = GameMenu(screen, text_items, 'Credits')
                response = cm.run()
                if response == 'Back':
                    self.currentState = GameState.Menu
                #text = font.render('Mellolikejello, Mackster, Red-Two', True, (0,0,0))
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
                            self.angle += 1
                        else:
                            self.angle = 90
                    elif event.key == pygame.K_RIGHT:
                        if self.angle > 0:
                            self.angle -= 1
                        else:
                            self.angle = 0
                    elif event.key == pygame.K_ESCAPE:
                        self.currentState = GameState.Paused

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
            screen.fill((255, 108, 0))  # 255 for white

            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            #all_sprites_list.clear(background, [255, 108, 0])

            #all_sprites_list.draw(screen)
            if(gator != None):
                screen.blit(gator.image, [0, (screen.get_height() - gator.rect.height)])
            if(text != None):
                screen.blit(text, [250,(screen.get_height() - gator.rect.height)])
            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.display.set_caption('AngleGators')
    game = HFOSS()
    game.run()

if __name__ == '__main__':
    main()
