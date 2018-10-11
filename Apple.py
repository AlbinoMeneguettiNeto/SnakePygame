import Settings


class Apple(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = Settings.red
        self.randomize()

    def randomize(self):
        self.position = (Settings.random.randint(0, Settings.GRID_WIDTH - 1) * Settings.GRIDSIZE, Settings.random.randint(0, Settings.GRID_HEIGHT - 1) * Settings.GRIDSIZE)

    def draw(self, surface):
        Settings.Functions.draw_box(surface, self.color, self.position)
