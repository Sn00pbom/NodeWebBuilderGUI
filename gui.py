import pygame as pg
import settings
from inputs import keyboard
from inputs import mouse
import drawings
import textrect

class GUI():
    def __init__(self):

        pg.init()
        self.size = [settings.GAME_WIDTH, settings.GAME_HEIGHT]
        self.clock = pg.time.Clock()

        self.DISPLAY = pg.display.set_mode(self.size)
        self.running = True
        self.all_sprites = None


    def new(self):
        self.all_sprites = pg.sprite.Group()

        # self.player = Player(settings.GAME_WIDTH, settings.GAME_HEIGHT)
        # self.unit = Unit(settings.GAME_WIDTH,settings.GAME_HEIGHT,3)
        # self.enemy = Enemy(settings.GAME_WIDTH,settings.GAME_HEIGHT,2)





    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            drawings.updateSprites()
            self.draw()
            self.clock.tick(settings.FPS)


    def update(self):
        self.all_sprites.update()

    def events(self):
        events = pg.event.get()
        for event in events:
            keyboard.readKeyboard(event)
            mouse.readMouse(event)
            # self.sticks.listenJoystick(self.player, event)
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                # sys.exit()

    def draw(self):
        self.DISPLAY.fill(settings.WHITE)
        textrect.printInfo()
        drawings.drawLines()
        # drawings.updateSprites()
        self.all_sprites.draw(self.DISPLAY)
        # textsurf = self.font.render("A: normal node mode\n"
        #                             "S: zone node mode\n"
        #                             "D: delete selected node\n"
        #                             "F: 1 way link (no tether)\n"
        #                             "G: 2 way link (tether)\n"
        #                             "Z: debug command\n"
        #                             "N: change node name",True,(0,0,0),justification = 0)

        pg.display.flip()
