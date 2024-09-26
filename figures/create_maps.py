import proplot as plt

import numpy as np
from colorengine.colormaps import *  # Import all your colormaps
import colorengine as ce

fig, ax = ce.show_colormaps()
fig.savefig("./colormaps.png")
plt.show(block = 1)
