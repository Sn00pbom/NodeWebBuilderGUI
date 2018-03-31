
import pygame as pg
import mouse
import controller
def readKeyboard(event):


    if event.type == pg.KEYDOWN:
        if controller.selected:
            if event.key == pg.K_a:
                print "db a normal nodes"
                mouse.currentType = mouse.NORMALNODE
            elif event.key == pg.K_s:
                print "db s zone nodes"
                mouse.currentType = mouse.ZONENODE
            elif event.key == pg.K_d:
                print "db d delete node"
                controller.selected.delete()
            elif event.key == pg.K_f:
                print "db f 1-way link: tether = False"
                mouse.tether = False
            elif event.key == pg.K_g:
                print "db g 2-way link: tether = True"
                mouse.tether = True
            elif event.key == pg.K_o:
                print "db o save output file...."
            elif event.key == pg.K_z:
                print "db z Debug"
                for node in controller.activeGUI.all_sprites:
                    node.printall()
            elif event.key == pg.K_n:
                print "db n rename node"
                controller.selected.name = raw_input("Enter new rawname for selected node...")
                print "Done!"
