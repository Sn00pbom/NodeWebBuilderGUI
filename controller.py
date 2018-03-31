import pygame as pg
from gui import GUI
#mostly a bunch of global variables in here

print "db init"
activeGUI = GUI()
selected = None


# def __init__(self):
#     self.activeGUI = GUI()
#     self.selected = None  # selected node


def clearSelected():
    selected = None

