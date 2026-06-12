import maya.cmds as cmds
import json
import main as forest_main
import importlib

# Ensures main logic is reloaded for testing
importlib.reload(forest_main)

class ForestGeneratorUI():
    def __init__(self):
        """ Initialize UI constants and window naming."""
        self.window_id = "forestGenWindow"
        self.title = "Procedural Forest Generator"
        self.size = (400, 450)

    def create(self):
        # Cleans up existing UI to prevent duplicates (Standard safety check)
        if cmds.window(self.window_id, exists=True):
            cmds.deleteUI(self.window_id)

        # Define the Window
        self.window = cmds.window(
            self.window_id, 
            title=self.title, 
            widthHeight=self.size,
            menuBar=True
        )

        # Presets Menu (Extra Credit JSON)
        cmds.menu(label="File")
        cmds.menuItem(label="Export Settings to JSON", command=self.save_json)
        cmds.menuItem(label="Import Settings from JSON", command=self.load_json)

        # Main Master Layout
        self.main_layout = cmds.columnLayout(adjustableColumn=True)

        # Environment part
        cmds.frameLayout(label="Environment Base Setup", collapsable=True, marginHeight=5)
        cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
        
        self.ground_size = cmds.floatSliderGrp(label="Ground Size", field=True, minValue=10.0, maxValue=200.0, value=30.0)
        self.sky_size = cmds.floatSliderGrp(label="Sky Size", field=True, minValue=50.0, maxValue=500.0, value=100.0)
        self.sun_height = cmds.floatSliderGrp(label="Sun Height", field=True, minValue=10.0, maxValue=100.0, value=18.0)
        
        cmds.setParent('..') # Close Column
        cmds.setParent('..') # Close Frame

        # Forest scattering
        cmds.frameLayout(label="Tree Scattering Settings", collapsable=True, marginHeight=5)
        cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
        
        self.tree_count = cmds.intSliderGrp(label="Tree Count", field=True, minValue=0, maxValue=200, value=35)
        self.tree_radius = cmds.floatSliderGrp(label="Scatter Radius", field=True, minValue=1.0, maxValue=100.0, value=14.0)
        self.tree_min_h = cmds.floatSliderGrp(label="Min Tree Height", field=True, minValue=0.5, maxValue=10.0, value=1.8)
        self.tree_max_h = cmds.floatSliderGrp(label="Max Tree Height", field=True, minValue=1.0, maxValue=20.0, value=3.2)
        
        cmds.setParent('..')
        cmds.setParent('..') 

        # --- PROPS & ASSETS SECTION ---
        cmds.frameLayout(label="Props & Atmosphere", collapsable=True, marginHeight=5)
        cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
        
        self.rock_count = cmds.intSliderGrp(label="Rock Count", field=True, minValue=0, maxValue=100, value=15)
        self.rock_radius = cmds.floatSliderGrp(label="Rock Radius", field=True, minValue=1.0, maxValue=100.0, value=13.0)
        self.cloud_count = cmds.intSliderGrp(label="Cloud Count", field=True, minValue=0, maxValue=50, value=6)
        
        cmds.setParent('..') 
        cmds.setParent('..') 

        # Action buttons that make things generate or close the window
        cmds.separator(height=15, style="none")
        cmds.button(label="Generate Scene", height=40, backgroundColor=(0.2, 0.4, 0.2), command=self.on_build_clicked)
        cmds.button(label="Close Window", command=lambda x: cmds.deleteUI(self.window_id))

        # Show Window
        cmds.showWindow(self.window)

    def get_config_dict(self):
        # Input Validation Check (Safety logic)
        min_h = cmds.floatSliderGrp(self.tree_min_h, query=True, value=True)
        max_h = cmds.floatSliderGrp(self.tree_max_h, query=True, value=True)
        
        if min_h >= max_h:
            cmds.warning("UI Logic: Min height adjusted to be less than Max height.")
            min_h = max_h * 0.5
            cmds.floatSliderGrp(self.tree_min_h, edit=True, value=min_h)

        return {
            "sky": {"size": cmds.floatSliderGrp(self.sky_size, query=True, value=True)},
            "ground": {"size": cmds.floatSliderGrp(self.ground_size, query=True, value=True)},
            "trees": {
                "count": cmds.intSliderGrp(self.tree_count, query=True, value=True),
                "types": ["round", "cone"],
                "height_range": (min_h, max_h),
                "scatter_radius": cmds.floatSliderGrp(self.tree_radius, query=True, value=True)
            },
            "rocks": {
                "count": cmds.intSliderGrp(self.rock_count, query=True, value=True),
                "scale_range": (0.6, 1.4),
                "scatter_radius": cmds.floatSliderGrp(self.rock_radius, query=True, value=True)
            },
            "clouds": {
                "count": cmds.intSliderGrp(self.cloud_count, query=True, value=True),
                "scatter_radius": 15.0
            },
            "sun": {"height": cmds.floatSliderGrp(self.sun_height, query=True, value=True)}
        }

    def on_build_clicked(self, *args):
        #Callback to execute the build from configuration
        config = self.get_config_dict()
        forest_main.build_from_config(FOREST_CONFIG=config)

    # Extra Credit: JSON Save/Load
    def save_json(self, *args):
        path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=0)
        if path:
            data = self.get_config_dict()
            with open(path[0], 'w') as f:
                json.dump(data, f, indent=4)
            cmds.confirmDialog(title="Done", message="Settings Exported.")

    def load_json(self, *args):
        path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=1)
        if path:
            with open(path[0], 'r') as f:
                data = json.load(f)
            # Update UI from file
            cmds.floatSliderGrp(self.ground_size, edit=True, value=data["ground"]["size"])
            cmds.intSliderGrp(self.tree_count, edit=True, value=data["trees"]["count"])
            # (Add more update calls here as needed)
            cmds.confirmDialog(title="Done", message="Settings Imported.")

def show():
    ui = ForestGeneratorUI()
    ui.create()
