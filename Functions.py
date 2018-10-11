import Settings


def draw_box(surface, color, pos):
    r = Settings.pygame.Rect((pos[0], pos[1]), (Settings.GRIDSIZE, Settings.GRIDSIZE))
    Settings.pygame.draw.rect(surface, color, r)


def check_eat(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 1
        Settings.points += 1
        apple.randomize()


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def button(text, x, y, width, height, color, hover_color, text_color, click_function=None):
    mouse = Settings.pygame.mouse.get_pos()
    click = Settings.pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        Settings.pygame.draw.rect(Settings.screen, hover_color, (x, y, width, height))
        if click[0] == 1 and click_function is not None:
            click_function()
    else:
        Settings.pygame.draw.rect(Settings.screen, color, (x, y, width, height))

    small_text = Settings.pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rect = text_objects(text, small_text, text_color)
    text_rect.center = ((x + (width/2)), (y + (height/2)))
    Settings.screen.blit(text_surface, text_rect)
