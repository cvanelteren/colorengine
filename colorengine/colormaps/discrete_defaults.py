import matplotlib as mpl
from matplotlib.colors import ListedColormap

__all__ = ["cmap", "cmap_r"]
__author__ = "Casper van Elteren"
__package__ = "colorengine"
cm_type = "discrete"
name = "ce.default"

cm_data = [
    "#FF4136",
    "#FF851B",
    "#FFDC00",
    "#2ECC40",
    "#3D9970",
    "#39CCCC",
    "#0074D9",
    "#001F3F",
    "#85144B",
    "#F012BE",
    "#B10DC9",
    "#7FDBFF",
    "#01FF70",
    "#FFAB40",
    "#FF4081",
    "#00BCD4",
    "#8BC34A",
    "#FFC107",
    "#607D8B",
    "#795548",
]
cmap = ListedColormap(cm_data, name=name)
cmap_r = cmap.reversed()

mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)

if __name__ != "__main__":
    globals()[name] = cmap
    globals()[name + "_r"] = cmap_r
