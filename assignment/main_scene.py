"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# Create a row of buildings to represent a small city block

# Buildings 
sf.create_building(width=5, height=12, depth=5, position=(-10, 0, 10))
sf.create_building(width=6, height=10, depth=4, position=(-5, 0, 12))
sf.create_building(width=4, height=8, depth=4, position=(0, 0, 10))
sf.create_building(width=7, height=14, depth=5, position=(5,0,12))

# Fence to define the park boundary
sf.create_fence(length=15, post_count=8, position=(-8, 0, -5))

# Lamp posts
sf.create_lamp_post(position=(8, 0, 0))
sf.create_lamp_post(position=(10, 0, 3))
sf.create_lamp_post(position=(12, 0, -2))

#Bench
sf.create_bench(position=(0, 0, -8))
sf.create_bench(position=(3, 0, -8))

# Trees in a circular park layout
sf.place_in_circle(sf.create_tree, count=8, radius=12)

# Extra trees
sf.create_tree(position=(-12, 0, -10))
sf.create_tree(position=(12, 0, -10))

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
