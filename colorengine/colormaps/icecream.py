import matplotlib as mpl
from matplotlib.colors import ListedColormap

__all__ = ["cmap", "cmap_r"]
__author__ = "Casper van Elteren"
__package__ = "colorengine"
cm_type = "discrete"
name = "ce.icecream"

cm_data = [
    "#C9CBA3",
    "#FFE1A8",
    "#E26D5C",
    "#723D46",
    "#472D30",
]
cmap = ListedColormap(cm_data, name=name)
cmap_r = cmap.reversed()

mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)

if __name__ != "__main__":
    globals()[name] = cmap
    globals()[name + "_r"] = cmap_r
