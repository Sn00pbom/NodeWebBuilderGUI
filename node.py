import pygame as pg
import math
import controller
vec = pg.math.Vector2
import controller
import random

class Node(pg.sprite.Sprite):
    NORMALNODE = 1
    ZONENODE = 2

    def __init__(self,x,y,ntype):
        self.pos = vec(x,y)

        self.connected = {}
        # self.name = "db"
        self.name = str(random.randint(1111,9999))
        self.ntype = ntype

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("./assets/node_u.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.pos



    def connect(self,node,tether):
        if not self.connected.__contains__(node):
            self.connected[node.name] = node
            if tether:
                node.connect(self,False)

    def delete(self):
        for node in controller.activeGUI.all_sprites:
            for nkey in node.connected:
                if node.connected[nkey].name == node.name:
                    node.connected.pop(nkey,None)
        self.kill()


    def update(self):
        # print self.pos
        # print self.goTo
        # if self.atDest() == True:
        #     self.vel = vec(0,0)
        # if self.checkMove(self.vel):
        #     self.pos = self.pos + self.vel

        self.rect.center = self.pos
    def printall(self):
        print self.name
        for nkey in self.connected:
            print "         " + self.connected[nkey].name

def updateSelect(newSelect):
    # if controller.selected:
        # controller.selected.image = pg.image.load('./assets/node_u.png')

    # if newSelect.ntype == 1: controller.selected = newSelect
    controller.selected = newSelect
    # controller.selected.image = pg.image.load('./assets/node_s.png')

