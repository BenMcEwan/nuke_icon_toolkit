import nuke
from pathlib import Path

# Recursively add plugin paths from subdirectories
root_path = Path(__file__).parent

for path in Path(root_path).rglob("*/"):
    nuke.pluginAddPath(str(path))
