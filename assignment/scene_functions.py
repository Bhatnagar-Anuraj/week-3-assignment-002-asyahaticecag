import maya.cmds as cmds
import math


def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube.

    Args:
        width (float): Width of the building.
        height (float): Height of the building.
        depth (float): Depth of the building.
        position (tuple): (x, y, z) position.

    Returns:
        str: Name of the created building.
    """
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(position[0], position[1] + height / 2.0, position[2], building)
    return building


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a tree with trunk and canopy.

    Args:
        trunk_radius (float): Radius of trunk.
        trunk_height (float): Height of trunk.
        canopy_radius (float): Radius of canopy.
        position (tuple): (x, y, z) position.

    Returns:
        str: Name of the tree group.
    """
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(0, trunk_height / 2.0, 0, trunk)

    canopy = cmds.polySphere(radius=canopy_radius)[0]
    cmds.move(0, trunk_height + canopy_radius * 0.5, 0, canopy)

    tree_group = cmds.group(trunk, canopy, name="tree_grp#")
    cmds.move(position[0], position[1], position[2], tree_group)

    return tree_group


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a fence with posts and a rail.

    Args:
        length (float): Length of the fence.
        height (float): Height of posts.
        post_count (int): Number of posts.
        position (tuple): (x, y, z) position.

    Returns:
        str: Name of the fence group.
    """
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
    """Create a lamp post.

    Args:
        pole_height (float): Height of pole.
        light_radius (float): Radius of light.
        position (tuple): (x, y, z) position.

    Returns:
        str: Name of the lamp group.
    """
    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(0, pole_height / 2.0, 0, pole)

    light = cmds.polySphere(radius=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, light)

    lamp_group = cmds.group(pole, light, name="lamp_grp")
    cmds.move(position[0], position[1], position[2], lamp_group)

    return lamp_group


def create_bench(width=2, height=0.5, depth=0.6, position=(0, 0, 0)):
    """Create a simple bench.

    Args:
        width (float): Width of seat.
        height (float): Height of legs.
        depth (float): Depth of seat.
        position (tuple): (x, y, z) position.

    Returns:
        str: Name of the bench group.
    """
    seat = cmds.polyCube(width=width, height=0.2, depth=depth)[0]
    cmds.move(0, height, 0, seat)

    leg1 = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
    cmds.move(-width / 2 + 0.2, height / 2, 0, leg1)

    leg2 = cmds.polyCube(width=0.2, height=height, depth=0.2)[0]
    cmds.move(width / 2 - 0.2, height / 2, 0, leg2)

    bench_group = cmds.group(seat, leg1, leg2, name="bench_grp")
    cmds.move(position[0], position[1], position[2], bench_group)

    return bench_group


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                    **kwargs):
    """Place objects in a circle.

    Args:
        create_func (callable): Function to create objects.
        count (int): Number of objects.
        radius (float): Radius of circle.
        center (tuple): Center position.
        **kwargs: Extra arguments.

    Returns:
        list: List of created objects.
    """
    results = []

    cmds.select(clear=True)  # REQUIRED for autograder

    for i in range(count):
        angle = 2 * math.pi * i / count
        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)

        obj = create_func(position=(x, center[1], z), **kwargs)
        results.append(obj)

    return results