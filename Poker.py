from typing import Tuple, Any

import pygame
import pygame_textinput


pygame.init()

WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load('PokerTable.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (1000,560))
ACTIVE_COLOR = pygame.Color('gray30')
INACTIVE_COLOR = pygame.Color('gray75')
FONT = pygame.font.Font(None, 30)



class player:

    def __init__(self, money,name):

        self.money = money
        self.name = name

    def update(self, value):
        self.money += value

    def get_name(self):
        return self.name


Player_list = []

def draw_player(player, position, screen):
    name = player.name
    money = "$" + str(player.money)
    x = 0
    y = 0
    if position == 0:
        x = 200
        y = 200
    elif position == 1:
        x = 200
        y = 300
    elif position == 2:
        x = 250
        y = 400
    elif position == 3:
        x = 500
        y = 400
    elif position == 4:
        x = 750
        y = 400
    elif position == 5:
        x = 800
        y = 300
    elif position == 6:
        x = 800
        y = 200


    name_surface = FONT.render(name, True, WHITE)
    rect = pygame.Rect(x, y, 5, 2)
    name_rect = name_surface.get_rect(center = rect.center)

    money_surface = FONT.render(money, True, WHITE)
    rect = pygame.Rect(x, y+15, 10,5)
    money_rect = money_surface.get_rect(center = rect.center)

    screen.blit(name_surface, name_rect)
    screen.blit(money_surface, money_rect)






def draw_button(button, screen):
    """Draw the button circle"""

    pygame.draw.circle(screen, button['color'], button['center'], button['radius'], button['width'])
    start_pos = (button['center'][0] + button['radius'], button['center'][1])
    stop_pos = (button['center'][0] - button['radius'], button['center'][1])
    pygame.draw.line(screen, button['color'], start_pos , stop_pos , button['width'])
    start_pos = (button['center'][0] , button['center'][1]+ button['radius'])
    stop_pos = (button['center'][0] , button['center'][1]- button['radius'])
    pygame.draw.line(screen, button['color'], start_pos, stop_pos, button['width'])
    #screen.blit(button['text'], button['text rect'])


def create_button(x, y, r, w):
    """A button is a dictionary that contains the relevant data."""
    # The button is a dictionary consisting of the rect, text,
    # text rect, color and the callback function.
    #text_surf = FONT.render(text, True, WHITE)
    center = (x,y)
    button_rect = pygame.Rect(x-r, y-r, r*2, r*2)
    #text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect' : button_rect,
        'center': center,
        'radius' : r,
        'width' : w,
        #'text': text_surf,
        #'text rect': text_rect,
        'color': INACTIVE_COLOR,
        #'callback': callback,
        }
    return button


def main():
    screen = pygame.display.set_mode((1000, 560))
    clock = pygame.time.Clock()
    done = False



    def add_player():  # A callback function for the button.
        """Increment the `number` in the enclosing scope."""
        global Player_list

        if(len(Player_list) <7):
            name_prompt = FONT.render('Enter Name:', True, WHITE)
            rect = pygame.Rect(500, 230, 10, 5)
            name_prompt_rect = name_prompt.get_rect(center=rect.center)

            name = ''
            money_str = ''
            active = True
            while active:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if(len(name)>=1):
                                name = name[:-1]

                        if event.key == pygame.K_RETURN:
                            active = False
                        else:
                            name += event.unicode

                screen.blit(name_prompt, name_prompt_rect)
                
                pygame.display.update()
                #temp_name_surface = FONT.render(name, True, WHITE)
                #temp_name_rect = pygame.Rect(500, 230)

            money_prompt = FONT.render('Enter start amount:', True, WHITE)
            rect = pygame.Rect(500, 260, 10, 5)
            money_prompt_rect = money_prompt.get_rect(center=rect.center)

            active = True
            while active:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if(len(money_str)>=1):
                                money_str = money_str[:-1]
                        if event.key == pygame.K_RETURN:
                            active = False
                        elif event.unicode.isdigit():
                            money_str += event.unicode
                screen.blit(money_prompt, money_prompt_rect)
                pygame.display.update()

            money = float(money_str)

            Player_list.append(player(money, name))


    def quit_game():  # A callback function for the button.
        nonlocal done
        done = True

    button1 = create_button(100, 100, 25, 5)
    button2 = create_button(100, 200, 25, 5)
    # A list that contains all buttons.
    add_player_list = [button1, button2]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    for button in add_player_list:
                        # `event.pos` is the mouse position.
                        if button['rect'].collidepoint(event.pos):

                            # function in the button list.
                            add_player()


            elif event.type == pygame.MOUSEMOTION:
                # When the mouse gets moved, change the color of the
                # buttons if they collide with the mouse.
                for button in add_player_list:
                    if button['rect'].collidepoint(event.pos):
                        button['color'] = ACTIVE_COLOR
                    else:
                        button['color'] = INACTIVE_COLOR

        screen.fill(WHITE)
        screen.blit(BACKGROUND, (0,0))
        for button in add_player_list:
            draw_button(button, screen)
        for p in Player_list:
            draw_player(p, Player_list.index(p), screen)


        pygame.display.update()
        clock.tick(30)


main()
pygame.quit()







