import matplotlib as mpl
from matplotlib.colors import ListedColormap

__all__ = ["cmap", "cmap_r"]
__author__ = "Casper van Elteren"
__package__ = "colorengine"
cm_type = "discrete"
name = "ce.vivid"
cm_data = [
    [0.0, 0.18, 0.29],
    [0.84, 0.16, 0.16],
    [0.97, 0.50, 0.0],
    [0.99, 0.75, 0.29],
    [0.918, 0.886, 0.718],
]

cmap = ListedColormap(cm_data, name=name)
cmap_r = cmap.reversed()
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)

if __name__ != "__main__":
    globals()[name] = cmap
    globals()[name + "_r"] = cmap_r
