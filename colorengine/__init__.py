"""
ColorEngine
===========
Generate curated pretty discrete colormaps for use in scientific papers and beyond
"""

__author__ = "Casper van Elteren"
__package__ = "colorengine"
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:  # for Python versions < 3.8
    from importlib_metadata import version, PackageNotFoundError
try:
    __version__ = version("colorengine")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

from .colormaps import *


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def show_colormaps():
    # Collect all colormaps from the package
    cmaps = [
        attr
        for attr in globals()
        if isinstance(globals()[attr], mpl.colors.ListedColormap)
        and attr not in ["key", "value"]
    ]

    n = len(cmaps)
    fig, axes = plt.subplots(nrows=n, figsize=(8, 0.8 * n))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, hspace=0.35)

    if n == 1:
        axes = [axes]  # Ensure axes is always iterable

    for ax, name in zip(axes, cmaps):
        cmap = globals()[name]
        n_colors = len(cmap.colors) if hasattr(cmap, "colors") else 256
        ax.imshow(np.linspace(0, 1, n_colors).reshape(1, -1), aspect="auto", cmap=cmap)
        ax.set_title(name, fontsize=10, loc="left")
        ax.set_xticks([])
        ax.set_yticks([])
    return fig, ax
