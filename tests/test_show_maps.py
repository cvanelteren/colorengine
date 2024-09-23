import unittest
import matplotlib.pyplot as plt
import colorengine as ce


class TestColorEngine(unittest.TestCase):

    def test_colormap_registration(self):
        """Test if colormaps are properly registered."""
        self.assertIn("ce.vivid", plt.colormaps())
        self.assertIn("ce.vivid_r", plt.colormaps())
        # Add more assertions for other colormaps

    def test_colormap_length(self):
        """Test if colormaps have the correct number of colors."""
        self.assertEqual(len(ce.vivid.colors), 5)
        self.assertEqual(len(ce.vivid_r.colors), 5)
        self.assertEqual(len(ce.default.colors), 20)
        self.assertEqual(len(ce.default_r.colors), 20)

    def test_show_colormaps_function(self):
        """Test if show_colormaps function runs without errors."""
        try:
            ce.show_colormaps()
        except Exception as e:
            self.fail(f"show_colormaps() raised {type(e).__name__} unexpectedly!")

    def test_colormap_type(self):
        """Test if colormaps are of the correct type."""
        self.assertIsInstance(ce.vivid, plt.cm.colors.ListedColormap)
        # Add more assertions for other colormaps

    def test_reversed_colormap(self):
        """Test if reversed colormaps are correctly created."""
        self.assertEqual(ce.vivid.colors[::-1], ce.vivid_r.colors)
        # Add more assertions for other reversed colormaps


if __name__ == "__main__":
    unittest.main()
