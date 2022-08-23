"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import Optional

from magicgui import magic_factory

import napari
from napari.utils.notifications import show_info
import tempfile

from quoll.io import reader as quollreader
from quoll.frc import oneimg
import os
import numpy as np

@magic_factory
def quoll_oneimgfrc(
    filename: str,
    pixel_size: float,
    unit: Optional[str] = "nm",
    tile_size: Optional[int] = 256,
):
    QuollImg = quollreader.Image(
        filename,
        pixel_size,
        unit,
    )
    
    show_info(f"Working with image: {os.path.basename(filename)}")

    viewer = napari.current_viewer()
    viewer.add_image(QuollImg.img_data)

    tempdir = tempfile.TemporaryDirectory()

    results_df = oneimg.calc_local_frc(
        QuollImg,
        tile_size=tile_size,
        tiles_dir=tempdir.name
    )

    show_info(f"Tiles directory is {tempdir}")

    show_info(f"Resolution is {np.mean(results_df.Resolution)}")

    resolution_heatmap = oneimg.plot_resolution_heatmap(
        QuollImg,
        results_df,
    )

    viewer.add_image(resolution_heatmap, colormap="viridis", opacity=0.3)

    tempdir.cleanup()
