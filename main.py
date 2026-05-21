import maya.cmds as cmds
import sys
import random

import scene_utils as utils
import importlib
importlib.reload(utils)

FOREST_CONFIG = {
    "ground": {
        "size": 30 },
    
    "hills": {
        "count": 1,
        "scale_range": (15.0, 7.0),
        "scatter_radius": 0 },
    
    "trees": {
        "count": 35,
        "types": ["round", "cone"],
        "height_range": (1.8, 3.2),
        "scatter_radius": 14 },

    "rocks": {
        "count": 15,
        "scale_range": (0.6, 1.4),
        "scatter_radius": 13},

    "clouds": {
        "count": 6,
        "scatter_radius": 15},

    "sun": {
        "height": 18.0}
}

# This is for exact placement for "Hero Objects" (basically anything that I want to put in an exact place because there is only one)
HERO_ASSET_PLACEMENTS = {
    "cabin": {
        "position": (0, 0, 0),
        "scale": 1.2
    },
    "chopping_block": {
        "position": (3.5, 0, 2.0)
    },
    "stump_with_axe": {
        "position": (4.5, 0, 1.5)
    }
}

def build_from_config():
    """
    Iterates through FOREST_CONFIG and calls the 
    matching builder functions from scene_utils.
    """
    cmds.file(new=True, force=True)
    
    # These are for foundational pieces from the world that don't really change unless you want them to be bigger
    if "ground" in FOREST_CONFIG:
        ground_size = FOREST_CONFIG["ground"]["size"]
        utils.create_ground(size=ground_size)
        
    if "sun" in FOREST_CONFIG:
        sun_height = FOREST_CONFIG["sun"]["height"]
        utils.create_sun(height=sun_height)

    # Build and Scatter the procedural generate models, trees, rocks, hills, stuff like that
    if "hills" in FOREST_CONFIG:
        hill_cfg = FOREST_CONFIG["hills"]
        for _ in range(hill_cfg["count"]):
            min_s, max_s = hill_cfg["scale_range"]
            rand_scale = random.uniform(min_s, max_s)
            h = utils.create_hill(scale_val=rand_scale)
            utils.scatter_item(h, area_range=hill_cfg["scatter_radius"])

    if "trees" in FOREST_CONFIG:
        tree_cfg = FOREST_CONFIG["trees"]
        for _ in range(tree_cfg["count"]):
            rand_type = random.choice(tree_cfg["types"])
            min_h, max_h = tree_cfg["height_range"]
            rand_height = random.uniform(min_h, max_h)
            
            t = utils.create_tree(tree_type=rand_type, height=rand_height)
            utils.scatter_item(t, area_range=tree_cfg["scatter_radius"])

    if "rocks" in FOREST_CONFIG:
        rock_cfg = FOREST_CONFIG["rocks"]
        for _ in range(rock_cfg["count"]):
            min_s, max_s = rock_cfg["scale_range"]
            rand_scale = random.uniform(min_s, max_s)
            
            r = utils.create_rock(scale_val=rand_scale)
            utils.scatter_item(r, area_range=rock_cfg["scatter_radius"])

    if "clouds" in FOREST_CONFIG:
        cloud_cfg = FOREST_CONFIG["clouds"]
        for _ in range(cloud_cfg["count"]):
            c = utils.create_cloud()
            utils.scatter_item(c, area_range=cloud_cfg["scatter_radius"])

    # This puts all the specific objects where you want them to go
    if "cabin" in HERO_ASSET_PLACEMENTS:
        cabin_cfg = HERO_ASSET_PLACEMENTS["cabin"]
        utils.create_cabin(pos=cabin_cfg["position"], scale=cabin_cfg["scale"])

if __name__ == "__main__":
    build_from_config()
