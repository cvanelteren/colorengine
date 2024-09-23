import proplot as plt
import numpy as np
from colorengine.colormaps import *  # Import all your colormaps

def show_colormaps():
    # Collect all colormaps from the package
    cmaps =  []
    for attr in globals():
        attr = globals()[attr]
        if isinstance(attr, plt.colors.mcm.colors.ListedColormap):
            cmaps.append(attr)
    n = len(cmaps)
    fig, axes = plt.subplots(nrows=n, figsize=(8, 0.8 * n))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, hspace=0.35)
    if n == 1:
        axes = [axes]  # Ensure axes is always iterable

    for ax, cmap in zip(axes, cmaps):
        n_colors = len(cmap.colors) if hasattr(cmap, 'colors') else 256
        img = np.linspace(0, 1, n_colors, 1)[None]
        ax.imshow(img, aspect='auto', cmap=cmap)
        ax.set_title(cmap.name, fontsize=10, loc='left')
        ax.set_xticks([])
        ax.set_yticks([])

    fig.savefig("./colormaps.png")
    plt.show()

show_colormaps()
