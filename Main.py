import time
import Settings
import Apple


def game_loop():
    snake = Settings.Menu.Snake.Snake()
    apple = Apple.Apple()

    while True:
        for event in Settings.pygame.event.get():
            if event.type == Settings.pygame.QUIT:
                Settings.Functions.my_quit()
            elif event.type == Settings.pygame.KEYDOWN:
                if event.key == Settings.pygame.K_UP:
                    snake.point(Settings.UP)
                elif event.key == Settings.pygame.K_DOWN:
                    snake.point(Settings.DOWN)
                elif event.key == Settings.pygame.K_LEFT:
                    snake.point(Settings.LEFT)
                elif event.key == Settings.pygame.K_RIGHT:
                    snake.point(Settings.RIGHT)
                elif event.key == Settings.pygame.K_SPACE:
                    snake.pause()
                    Settings.Menu.pause(snake)

        Settings.surface.fill(Settings.black)
        snake.move()
        Settings.Functions.check_eat(snake, apple)
        snake.draw(Settings.surface)
        apple.draw(Settings.surface)
        Settings.screen.blit(Settings.surface, (0, 0))
        Settings.pygame.display.flip()
        Settings.pygame.display.update()
        Settings.fpsClock.tick(Settings.fps + snake.length / 3)


if __name__ == '__main__':
    Settings.Menu.intro(game_loop, Settings.Functions.my_quit)
