import pygame as pg
import controller

import node
from node import Node



LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

NORMALNODE = 1
ZONENODE = 2
tether = True
currentType = NORMALNODE

def readMouse(event):
    # game = controller.activeGUI
    mousepos = pg.mouse.get_pos()

    # drawSelection()
    if event.type == pg.MOUSEBUTTONDOWN:
        um = getUnderMouse(mousepos) ##underneath mouse position sprite array
        if event.button == RIGHT:
            print "db right click"
            print controller.activeGUI.size
            if len(um) == 1:
                for sprite in um:
                    if type(sprite) == Node:
                        #sprite is a unit, and inherits methods
                        if controller.selected: controller.selected.connect(sprite,tether)


        elif event.button == LEFT:
            # controller.mleftdownpos = mousepos
            #selecting something
            if len(um) == 1:
                for sprite in um:
                    if type(sprite) == Node:
                        #sprite is a unit, and inherits methods
                        print sprite.name
                        node.updateSelect(sprite)
            else:#nothing under cursor
                newnode = None
                if currentType == NORMALNODE:
                    newnode = Node(mousepos[0],mousepos[1],NORMALNODE)
                elif currentType == ZONENODE:
                    newnode = Node(mousepos[0], mousepos[1],ZONENODE)


                controller.activeGUI.all_sprites.add(newnode)
                if controller.selected == None: controller.selected = newnode


    elif event.type == pg.MOUSEBUTTONUP:

        if event.button == LEFT:
            # selection(mousepos)
            pass


        
def getUnderMouse(mousepos):
    sprites = []

    for sprite in controller.activeGUI.all_sprites:
        if sprite.rect.collidepoint(mousepos):
            sprites.append(sprite)

    return sprites



