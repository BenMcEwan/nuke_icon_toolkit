# ======================================================================================================================
# :::::  INFO  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ======================================================================================================================
#  high_res_menu_icons.py
#  Version: 2.0.0
#  Author: Ben McEwan
#  Website: https://benmcewan.com/
#  Last Updated: August 30th, 2025

# ======================================================================================================================
# :::::  USAGE  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ======================================================================================================================
#  From Nuke Icon Design Toolkit: https://github.com/BenMcEwan/nuke_icon_toolkit
#  Replace Nuke's default low-res icons with high-resolution versions.
# ======================================================================================================================


import nuke
import nukescripts


def replace_menu_icons():
    """
    Replace Nuke's default low-res menu icons with high-resolution versions.
        • Remove all existing menus.
        • Re-add menus with high-resolution icons.
        • Run Nuke's default menu setup to populate menus, and add anything this script missed.
    """

    # Once menus are loaded, it's tough to change their icons.
    # Instead, we will clear all the menu items, add our own, then run Foundry's setup_toolbars to re-populate the menus.
    nodes_toolbar = nuke.menu("Nodes")

    # Remove all menu items
    for menu in nodes_toolbar.items():
        nodes_toolbar.removeItem(menu.name())

    # Add new menus with high-res icons
    menu_icons_to_update = {
        "Image": "icon_toolbar_image_HighRes.png",
        "Draw": "icon_toolbar_draw_HighRes.png",
        "Time": "icon_toolbar_time_HighRes.png",
        "Channel": "icon_toolbar_channel_HighRes.png",
        "Color": "icon_toolbar_color_HighRes.png",
        "Filter": "icon_toolbar_filter_HighRes.png",
        "Keyer": "icon_toolbar_keyer_HighRes.png",
        "Merge": "icon_toolbar_merge_HighRes.png",
        "Transform": "icon_toolbar_transform_HighRes.png",
        "3D": "icon_toolbar_3d_HighRes.png",
        "Particles": "icon_toolbar_particles_HighRes.png",
        "Deep": "icon_toolbar_deep_HighRes.png",
        "Views": "icon_toolbar_views_HighRes.png",
        "MetaData": "icon_toolbar_metadata_HighRes.png",
        "ToolSets": "icon_toolbar_toolsets_HighRes.png",
        "Other": "icon_toolbar_other_HighRes.png",
        "FurnaceCore": "icon_toolbar_furnace_HighRes.png",
        "AIR": "icon_toolbar_AIR_HighRes.png",
        "CaraVR": "icon_toolbar_CaraVR_HighRes.png",
    }
    # Note: Cattery not in this list, as it will cause errors if Cattery wouldn't otherwise load in.
    #       Instead, the icon is named the same as it is in Nuke's install directory, and Nuke picks that
    #       up instead.

    for menu, icon in menu_icons_to_update.items():
        nodes_toolbar.addMenu(menu, icon=icon)

    # Re-populate menus with items
    nukescripts.toolbars.setup_toolbars()


# Ensure this runs after the GUI is initialized
nuke.executeInMainThread(replace_menu_icons)
