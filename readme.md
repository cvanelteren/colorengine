![GitHub Actions](https://github.com/cvanelteren/colorengine/actions/workflows/build.yml/badge.svg)

<div align="center">
  <img src="./figures/colorengine.png" width="100%" alt="Color Engine Logo">
</div>

# Color Engine

ColorEngine is a Python package that provides a collection of custom colormaps for use with Matplotlib. It offers an easy-to-use interface for accessing and visualizing a variety of color schemes, enhancing your data visualization capabilities.

Is your favorite colormap missing? Feel free to open an issue or submit a pull request!

![colormaps](./figures/colormaps.png)


## Installation

You can install ColorEngine using pip:

```bash
pip install colorengine
```

## Usage

### Importing the package

```python
import colorengine as ce
```

### Using a colormap

You can use ColorEngine's colormaps in your Matplotlib plots:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
data = np.random.rand(10, 10)

# Plot using a ColorEngine colormap
plt.imshow(data, cmap=ce.vivid)
plt.colorbar()
plt.show()
```

### Displaying all available colormaps

ColorEngine provides a convenient function to display all available colormaps:

```python
ce.show_colormaps()
```

This will create a visual representation of all colormaps included in the package.


## Customization
Each colormap in ColorEngine is designed to be used as-is, but you can also create variations
