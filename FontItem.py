import pygame

class FontItem(pygame.font.Font):
    """Displayable Text Item"""
    def __init__(self, text, font_size=30, font=None,
                 font_color=(33, 69, 30), pos_x=0, pos_y=0,):
        """Initialize FontItem

        Keyword arguments:
        text -- text to be displayed
        font_size -- size of font (default 30)
        font -- typeface (default None)
        font_color -- color of font (default black)
        pos_x -- x position of text (default 0)
        pos_y -- y position of text (default 0)
        """
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
        """Update position of FontItem"""
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
        self.label = self.render(self.text, 1, self.font_color)

    def set_text(self, value):
        """Update text value, re-renders with updated text value"""
        self.text = value
        self.label = self.render(self.text, 1, self.font_color)

    def set_font_color(self, rgb_tuple):
        """Update colof of FontItem"""
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class FontButton(FontItem):
    """Extends FontItem, adds mouse check for interaction"""
    def __init__(self, text, font_size=30, font=None,
                 font_color=(33, 69, 30), pos_x=0, pos_y=0):
        super(FontButton, self).__init__(text, font_size, font, font_color,
                        pos_x, pos_y)
    def is_mouse_selection(self, posx_posy):
        """Check if mouse position collides with FontButton

        Keyword arguments:
        posx_posy -- tuple of x and y position
        """
        posx, posy = posx_posy
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False