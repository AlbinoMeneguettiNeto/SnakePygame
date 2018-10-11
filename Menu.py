import Settings
import Snake


def lose(start, highscore):
    menu = True
    while menu:
        for event in Settings.pygame.event.get():
            if event.type == Settings.pygame.QUIT:
                Settings.pygame.quit()
                Settings.sys.exit()

            Settings.screen.fill((0, 0, 0))
            large_text = Settings.pygame.font.Font('freesansbold.ttf', 25)
            text_surface, text_rect = Settings.Functions.text_objects('Score: ' + str(Settings.points), large_text, Settings.white)
            text_rect.center = ((Settings.SWidth/2), (Settings.SHeight/3))
            Settings.screen.blit(text_surface, text_rect)

            Settings.Functions.button('Start', 150, (Settings.SHeight / 2), 100, 30, Settings.lightgray, Settings.white, Settings.black, start)
            Settings.Functions.button('Highscore', 380, (Settings.SHeight / 2), 100, 30, Settings.lightgray, Settings.white, Settings.black, highscore)

            Settings.pygame.display.update()
            Settings.clock.tick(30)


def intro(start, myquit):
    menu = True
    while menu:
        for event in Settings.pygame.event.get():
            if event.type == Settings.pygame.QUIT:
                Settings.pygame.quit()
                Settings.sys.exit()

        Settings.screen.fill((0, 0, 0))
        large_text = Settings.pygame.font.Font('freesansbold.ttf', 25)
        text_surface, text_rect = Settings.Functions.text_objects("Snake Game", large_text, Settings.white)
        text_rect.center = ((Settings.SWidth/2), (Settings.SHeight/3))
        Settings.screen.blit(text_surface, text_rect)

        Settings.Functions.button('Start', 150, (Settings.SHeight / 2), 100, 30, Settings.lightgray, Settings.white, Settings.black, start)
        Settings.Functions.button('Quit', 380, (Settings.SHeight / 2), 100, 30, Settings.lightgray, Settings.white, Settings.black, myquit)

        Settings.pygame.display.update()
        Settings.clock.tick(30)


def show_highscores():
    while True:
        for event in Settings.pygame.event.get():
            if event.type == Settings.pygame.QUIT:
                Settings.pygame.quit()
                Settings.sys.exit()
        Settings.screen.fill((0, 0, 0))
        normal_text = Settings.pygame.font.Font('freesansbold.ttf', 20)
        large_text = Settings.pygame.font.Font('freesansbold.ttf', 25)
        title_surface, title_rect = Settings.Functions.text_objects("Highscores:", large_text, Settings.white)
        title_rect.center = ((Settings.SWidth/2), (Settings.SHeight/3))
        Settings.screen.blit(title_surface, title_rect)
        scores = 0
        for score in Settings.highscore:
            scores += 1
            if scores < 6:
                text_surface, text_rect = Settings.Functions.text_objects(str(score), normal_text, Settings.white)
                text_rect = ((Settings.SWidth/2) - 70, (Settings.SHeight/3+(scores*20)))
                Settings.screen.blit(text_surface, text_rect)
        Settings.Functions.button('Start', (Settings.SWidth/2-50), (text_rect[1]+100), 100, 30, Settings.lightgray, Settings.white, Settings.black, Settings.Main.game_loop)


        Settings.pygame.display.update()
        Settings.clock.tick(30)



if __name__ == '__main__':
    show_highscores()
