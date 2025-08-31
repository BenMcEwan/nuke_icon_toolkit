# ======================================================================================================================
# :::::  INFO  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ======================================================================================================================
#  relocate_2x_icons.py
#  Version: 1.0.0
#  Author: Ben McEwan
#  Website: https://benmcewan.com/
#  Last Updated: August 30th, 2025

# ======================================================================================================================
# :::::  USAGE  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ======================================================================================================================
#  From Nuke Icon Design Toolkit: https://github.com/BenMcEwan/nuke_icon_toolkit
#  Copy any higher-resolution icon from Nuke's installation directory to this toolkit's icons directory.
# ======================================================================================================================


import os
from pathlib import Path
import shutil


def copy_high_res_icons():
    """
    There are a small handful of double-res icons in Nuke's installation directory.
    This function copies them to this toolkit's icons directory, renaming them to match the original.
    When Nuke opens, it will prioritize icons in your ~/.nuke directory over the install directory.
    """

    nuke_install_path = Path(os.getenv("NUKE_PATH").strip(";"))
    icons_path = nuke_install_path / "plugins" / "icons"

    # Recursively find all .png files with @2x in the name.
    for icon in icons_path.rglob("*.png"):
        if "@2x" in icon.name:

            # Remove @2x or trailing underscores to attempt to recreate the existing icon's name.
            icon_renamed = icon.stem.replace("@2x", "").rstrip("_") + icon.suffix
            destination_file = (
                Path(__file__).parents[1] / "icons" / "nuke_16_2x" / icon_renamed
            )

            # Copy renamed file to new location
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(icon, destination_file)
            print(f"Copied {icon} to {destination_file}")


copy_high_res_icons()
