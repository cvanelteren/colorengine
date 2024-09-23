import matplotlib as mpl
from matplotlib.colors import ListedColormap

__all__ = ["cmap", "cmap_r"]
__author__ = "Casper van Elteren"
__package__ = "colorengine"
cm_type = "discrete"
name = "ce.dream"

cm_data = [
    "#f94144",
    "#f3722c",
    "#f8961e",
    "#f9844a",
    "#f9c74f",
    "#90be6d",
    "#43aa8b",
    "#4d908e",
    "#577590",
    "#277da1",
]
cmap = ListedColormap(cm_data, name=name)
cmap_r = cmap.reversed()

mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)

if __name__ != "__main__":
    globals()[name] = cmap
    globals()[name + "_r"] = cmap_r
