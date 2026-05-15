import maya.cmds as cmds
import random

def create_ground(size=20):
  ground = cmds.polyPlane(w=size, h=size, name="forest_floor")[0]
    return ground

def create_tree(tree_type='round', height=2.0):
    trunk = cmds.polyCylinder(r=0.2, h=height, name="trunk")[0]
    cmds.move(0, height/2, 0, trunk)
    
    if tree_type == 'round':
        canopy = cmds.polySphere(r=1.0, name="canopy")[0]
    else:
        canopy = cmds.polyCone(r=0.8, h=2.0, name="canopy")[0]
        
    cmds.move(0, height, 0, canopy)
    tree_grp = cmds.group(trunk, canopy, n=f"tree_{tree_type}_grp")
    return tree_grp

def create_rock(scale_val=1.0):
  rock = cmds.polyCube(n="rock")[0]
    cmds.setAttr(f"{rock}.scale", scale_val, random.uniform(0.5, 1.5), scale_val)
    return rock

def create_cabin(pos=(0, 0, 0), scale=1.0):
    cabin = cmds.polyCube(n="cabin", w=3, h=2, d=4)[0]
    cmds.move(pos[0], 1, pos[2], cabin)
    cmds.scale(scale, scale, scale, cabin)
    return cabin

def scatter_item(item_name, area_range=10):
  pos_x = random.uniform(-area_range, area_range)
    pos_z = random.uniform(-area_range, area_range)
    cmds.move(pos_x, 0, pos_z, item_name)
    return [pos_x, pos_z]
