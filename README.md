# Procedural Forest Generator

A Python-based tool for Maya that automatically generates a customizable 3D forest. You can instantly build and scatter natural layouts with trees, rocks, clouds, a ground plane, and a sun.

# Features
* Modular Code: Split into separate files for the UI, main setup, and asset tools to keep the code clean and organized.
*  UI Window: Easy-to-use sliders to control object counts, sizes, and layout spacing.
* Error Prevention: Built-in checks to prevent bad settings (like invalid tree heights) from crashing Maya.
* Save/Load Presets: Save your favorite slider setups to a `.json` file and load them back up later.

# Project Files

Save these three files together in your Maya scripts folder:

1.  **`scene_utils.py`** – Contains the building blocks. It makes the 3D shapes (trees, rocks, clouds) and handles the math to scatter them randomly.
2.  **`main.py`** – The coordinator. It takes settings from the UI and tells `scene_utils.py` exactly what to build.
3.  **`ui.py`** – Creates the custom window, sliders, buttons, and the file menus for saving/loading.

#How to run it

# 1. Where to Save the Files
Put `scene_utils.py`, `main.py`, and `ui.py` into your local Maya scripts directory:

# 2. Launching the Tool
1. Open Autodesk Maya.
2. Open the Script Editor
3. Open a new Python tab
4. Paste the following code

```python
import ui
import importlib

# Reload ensures any new code changes update immediately,
importlib.reload(ui)

# Open the UI itself
ui.show()
