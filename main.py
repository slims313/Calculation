from Window import *

vec = pygame.math.Vector2


class PGM:
    def __init__(self):
        self.timer = pygame.time.Clock()
        self.running = True
        self.start = 0
        self.end = 0

        self.__init_window__()
        self.main_loop()

    def __init_window__(self):
        pygame.init()
        self.dt = self.timer.tick(60) / 1000.0

    def quit(self):
        pygame.quit()
        sys.exit()

    def key_press(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_ESCAPE:
                    self.quit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.start = pygame.mouse.get_pos()

                if e.button == 2:
                    pass

                if e.button == 3:
                    self.end = pygame.mouse.get_pos()


    def draw_grid(self):  # СЕТКА
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(screen, LIGHTGRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(screen, LIGHTGRAY, (0, y), (SCREEN_WIDTH, y))

    def draw_lines(self):
        try:
            pygame.draw.lines(screen, '#00d6ff', False, (self.start, self.end), 3)
        except:
            pass
    def update(self):
        self.key_press()
        self.render()

    def render(self):
        window.blit(screen, (0, 0))
        screen.fill((0, 0, 0))
        self.draw_grid()
        self.draw_lines()

        pygame.display.flip()

    def main_loop(self):
        while self.running:
            self.update()
            self.timer.tick(FPS)


programm = PGM()
