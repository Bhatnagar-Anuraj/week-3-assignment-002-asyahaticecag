
import maya.cmds as cmds
import math

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube, placed on the ground plane."""
    building = cmds.polyCube(width=width, height=height, depth=depth,)[0]
    cmds.move(position[0],position[1]+height / 2.0, position[2], building)
    return building


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy."""

    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(0, trunk_height / 2.0, 0, trunk)

    canopy = cmds.polySphere(radius=canopy_radius)[0]
    cmds.move(0, trunk_height + canopy_radius * 0.5, 0, canopy)

    tree_group = cmds.group(trunk,canopy,name="tree_grp#")
    cmds.move(position[0], position[1], position[2], tree_group)

    return tree_group


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails."""

    posts = []
    spacing = length / (post_count - 1)

    for i in range(post_count):
        post = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
        cmds.move(i * spacing, height / 2.0, 0, post)
        posts.append(post)

    rail = cmds.polyCube(width=length, height=0.2, depth=0.2)[0]
    cmds.move(length / 2.0, height * 0.6, 0, rail)
    
    fence_group = cmds.group(posts + [rail], name="fence_grp")
    cmds.move(position[0], position[1], position[2], fence_group)

    return fence_group

def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light."""

    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(0, pole_height / 2.0, 0, pole)

    light = cmds.polySphere(radius=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, light)

    lamp_group = cmds.group(pole, light, name="lamp_grp")
    cmds.move(position[0], position[1], position[2], lamp_group)

    return lamp_group

def create_bench(width=2, height=0.5,depth=0.6, position=(0,0,0)):
    """Create a simple bench."""
    
    seat = cmds.polyCube(width=width, height=0.2, depth=depth)[0]
    cmds.move(0,height, 0, seat)

    leg1 = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
    cmds.move(-width/ 2 + 0.2, height/2, 0, leg1)

    leg2 = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
    cmds.move(width/ 2 - 0.2, height/2, 0, leg2)

    bench_group = cmds.group(seat, leg1, leg2, name="bench_grp")
    cmds.move(position[0], position[1], position[2], bench_group)

    return bench_group

def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    """Place objects created by 'create_func' in a circular arrangement. """

    results = []

    for i in range(count):
        angle = 2 * math.pi * i / count
        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)

        obj = create_func(position=(x, center[1], z), **kwargs)
        results.append(obj)

    return results
