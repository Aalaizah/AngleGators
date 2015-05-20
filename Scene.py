import pygame

from FontItem import FontItem, FontButton
from Alligator import Alligator
from Food import FoodManager, Food

class Scene(object):
    def __init__(self, screen, bg_image="Assets/mainbackground.png", font=None,
                    font_size=30, font_color=(33, 69, 30)):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_image = pygame.image.load(bg_image)
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

    def draw(self):
        # Redraw the background
        self.screen.blit(self.bg_image, [0, 0])
        pygame.display.flip()

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 fps
            self.clock.tick(50)
            self.draw()

class GameScene(Scene):
    def __init__(self, screen, bg_image="Assets/playbackground.png", font=None,
                    font_size=30, font_color=(33, 69, 30)):
        super(GameScene, self).__init__(screen, bg_image, font, font_size, font_color)
        self.gator = Alligator(0)
        self.food_manager = FoodManager()

    def draw(self):
        # Redraw the background
        self.screen.blit(self.bg_image, [0, 0])
        self.gator.draw(self.screen)
        self.food_manager.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            # Limit frame speed to 50 fps
            self.clock.tick(50)
            if not self.food_manager.is_started:
                self.food_manager.generate_food()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('quitting')
                    return 'Quit'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.gator.change_angle("up")
                    elif event.key == pygame.K_RIGHT:
                        self.gator.change_angle("down")
                    elif event.key == pygame.K_ESCAPE:
                        self.food_manager.reset()
                        return 'Pause'
            self.draw()

class MenuScene(Scene):
    #                           items is a list of FontItem
    def __init__(self, screen, items, title, bg_image="Assets/mainbackground.png", font=None,
                    font_size=30, font_color=(33, 69, 30)):
        super(MenuScene, self).__init__(screen, bg_image, font, font_size, font_color)
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        self.title = FontItem(title, 60)

        #self.title_label = pygame.font.Font.render(self.title, 1, self.font_color)
        self.title_pos_x = (self.scr_width / 2) - (self.title.width / 2)
        self.title_pos_y = (self.scr_width / 8) - (self.title.height / 2)
        self.title.set_position(self.title_pos_x, self.title_pos_y)

        for index, item in enumerate(items):
            #t_h: total height of text block
            t_h = len(items) * item.height
            pos_x = (self.scr_width / 2) - (item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * item.height)

            item.set_position(pos_x, pos_y)

        self.items = items


    def draw(self):
        # Redraw the background
        self.screen.blit(self.bg_image, [0, 0])

        for item in self.items:
            if isinstance(item, FontButton) and item.is_mouse_selection(pygame.mouse.get_pos()):
                item.set_font_color((255, 255, 255))
            else:
                item.set_font_color((33, 69, 30))
            self.screen.blit(item.label, item.position)

	    self.screen.blit(self.title.label, self.title.position)
        pygame.display.flip()

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 fps
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mpos = pygame.mouse.get_pos()
                    for item in self.items:
                        if isinstance(item, FontButton) and item.is_mouse_selection(mpos):
                            return item.text

            self.draw()