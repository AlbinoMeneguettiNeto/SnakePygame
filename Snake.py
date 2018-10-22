import Settings
import Singleton


class Snake(Singleton.Singleton):
    def init(self):
        self.lose()
        self.color = (255, 255, 255)

    def get_head_position(self):
        return self.position[0]

    def lose(self):
        self.length = 1
        self.position = [((Settings.SWidth / 2), (Settings.SHeight / 2))]
        self.direction = Settings.random.choice([Settings.UP, Settings.DOWN, Settings.LEFT, Settings.RIGHT])
        self.points = 0

    def point(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.position[0]
        x, y = self.direction
        new = (((cur[0] + (x * Settings.GRIDSIZE)) % Settings.SWidth), (cur[1] + (y*Settings.GRIDSIZE)) % Settings.SHeight)
        if len(self.position) > 2 and new in self.position[2:]:
            Settings.points = self.points
            Settings.highscore.append(Settings.points)
            Settings.highscore = sorted(Settings.highscore, reverse=True)
            self.lose()
            Settings.Menu.lose(Settings.Main.game_loop, Settings.Menu.show_highscores)
        else:
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()

    def draw(self, surface):
        for p in self.position:
            Settings.Functions.draw_box(surface, self.color, p)

    def pause(self):
        self.las_dir = self.direction
        self.direction = Settings.PAUSE

    def resume(self):
        self.direction = self.las_dir
