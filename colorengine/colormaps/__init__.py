import importlib


def auto_import_colormaps():
    bindings = {}
    modules_to_import = [
        "discrete_defaults",
        "dream",
        "vivid",
        "icecream",
        "distinct",
    ]

    for module_name in modules_to_import:
        module = importlib.import_module(f"colorengine.colormaps.{module_name}")

        if module_name == "discrete_defaults":
            bindings["default"] = module.cmap
            bindings["default_r"] = module.cmap_r
        else:
            bindings[module_name] = module.cmap
            bindings[f"{module_name}_r"] = module.cmap_r

    return bindings


colormaps = auto_import_colormaps()
for key, value in colormaps.items():
    globals()[key] = value
