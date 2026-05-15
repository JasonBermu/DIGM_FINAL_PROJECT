import maya.cmds as cmds
import sys
import os

package_path = os.path.dirname(__file__)
if package_path not in sys.path:
    sys.path.append(package_path)

import utils.scene_utils as utils
import importlib
importlib.reload(utils)

FOREST_CONFIG = [
    {"type": "tree", "tree_type": "round", "height": 3.5},
    {"type": "rock", "scale_val": 2.0},
    {"type": "ground", "size": 50},
    {"type": "cabin", "pos": (0, 0, 0)},
]

def build_from_config():
    """
    Iterates through FOREST_CONFIG and calls the 
    matching builder functions from scene_utils.
    """
    cmds.file(new=True, force=True)
    
    for item in FOREST_CONFIG:
        #Checks the type of object and calls the correct function fpr the scene
        if item["type"] == "tree":
            t = utils.create_tree(tree_type=item["tree_type"], height=item["height"])
            utils.scatter_item(t)
            
        elif item["type"] == "rock":
            r = utils.create_rock(scale_val=item["scale_val"])
            utils.scatter_item(r)
            
        elif item["type"] == "ground":
            utils.create_ground(size=item["size"])
            
        elif item["type"] == "cabin":
            utils.create_cabin(pos=item["pos"])

if __name__ == "__main__":
    build_from_config()
