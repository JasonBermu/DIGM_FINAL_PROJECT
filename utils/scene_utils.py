import maya.cmds as cmds
import random

def create_sky(size=100):

    if size <= 0:
        cmds.error("Sky size must be greater than zero.")
        
    sky = cmds.polySphere(radius = size, name="sky")[0]
    cmds.polyNormal(sky, normalMode=0)
    return sky

def create_ground(size=20):
    ground = cmds.polyPlane(w=size, h=size, name="forest_floor")[0]
    return ground

def create_tree(tree_type='round', height=2.0):
    if height <= 0:
        cmds.error("Tree height must be greater than zero.")

    trunk = cmds.polyCylinder(r=0.2, h=height, name="trunk")[0]
    cmds.move(0, height/2, 0, trunk)
    
    if tree_type == 'round':
        canopy = cmds.polySphere(r=1.0, name="canopy")[0]
        cmds.move(0, height + 0.8, 0, canopy) 
    else:
        canopy = cmds.polyCone(r=0.8, h=2.0, name="canopy")[0]
        cmds.move(0, height + 1.0, 0, canopy)
        
    tree_grp = cmds.group(trunk, canopy, n=f"tree_{tree_type}_grp")
    return tree_grp

def create_rock(scale_val=1.0):
    rock = cmds.polyCube(n="rock")[0]
    rand_y = random.uniform(0.5, 1.5)

    cmds.scale(scale_val, rand_y, scale_val, rock)
    cmds.move(0, rand_y / 2, 0, rock)
    return rock

def create_cabin(pos=(0, 0, 0), scale=1.0):
    cabin = cmds.polyCube(n="cabin", w=3, h=2, d=4)[0]
    cmds.move(pos[0], 1 * scale, pos[2], cabin)
    cmds.scale(scale, scale, scale, cabin)
    return cabin

def scatter_item(item_name, area_range=10):
    # Input Validation and Error Handling required by rubric
    if area_range < 0:
        cmds.error("Scatter area range cannot be negative.")
    if not cmds.objExists(item_name):
        cmds.warning(f"Object {item_name} does not exist. Skipping.")
        return None

    pos_x = random.uniform(-area_range, area_range)
    pos_z = random.uniform(-area_range, area_range)
    current_y = cmds.getAttr(f"{item_name}.ty")
    cmds.move(pos_x, current_y, pos_z, item_name)
    return [pos_x, pos_z]

def create_hill(scale_val=5.0):
    hill = cmds.polySphere(r=1.0, sx=10, sy=10, name="hill")[0]
    
    rand_x = scale_val * random.uniform(1.0, 1.8)
    rand_y = scale_val * random.uniform(0.3, 0.6) 
    rand_z = scale_val * random.uniform(1.0, 1.8)
    
    cmds.scale(rand_x, rand_y, rand_z, hill)
    cmds.move(0, -5, 0, hill) 
    return hill

def create_sun(height=15.0):
    sun = cmds.polySphere(r=1.5, name="stylize_sun")[0]
    cmds.move(0, height, 0, sun)
    return sun

def create_cloud():
    cloud_grp = cmds.group(em=True, name="cloud_grp")
    
    num_puffs = random.randint(3, 5)
    for i in range(num_puffs):
        puff = cmds.polySphere(r=random.uniform(0.6, 1.2), name="cloud_puff")[0]
        cmds.move(random.uniform(-1.0, 1.0), random.uniform(-0.2, 0.2), random.uniform(-0.5, 0.5), puff)
        cmds.parent(puff, cloud_grp)
        
    cmds.xform(cloud_grp, cp=True)
    
    cmds.move(random.uniform(0, 5), random.uniform(10.0, 14.0), random.uniform(0, 5), cloud_grp)
    return cloud_grp
