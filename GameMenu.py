import pygame

from FontItem import FontItem, FontButton

class GameMenu():
    #                           items is a list of FontItem
    def __init__(self, screen, items, title, bg_image="Assets/mainbackground.png", font=None,
                    font_size=30, font_color=(33, 69, 30)):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_image = pygame.image.load(bg_image)
        self.clock = pygame.time.Clock()

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