"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import napari
import numpy as np
from magicgui import magic_factory
from magicgui.widgets import Table
from matplotlib.backends.backend_qt5agg import FigureCanvas
from napari.utils.notifications import show_info
from quoll.frc import oneimg
from quoll.io import reader as quollreader


@magic_factory(
    pixel_size={"min": 1e-6}, tile_size={"min": 128.0}, results_csv={"mode": "w"}
)
def quoll_oneimgfrc(
    data: napari.types.ImageData,
    pixel_size: float,
    unit: str = "nm",
    tile_size: float = 256.0,  # temp fix as can't type in the GUI if it's a float
    save_csv: bool = True,
    results_csv: Path = Path("results.csv"),
):
    # Load image
    QuollImg = quollreader.Image(
        img_data=data,
        pixel_size=pixel_size,
        unit=unit,
    )

    # Display image
    viewer = napari.current_viewer()
    viewer.layers.selection.scale = [1 / pixel_size, 1 / pixel_size]
    viewer.scale_bar.visible = True
    viewer.scale_bar.unit = unit

    # Create temporary dir to hold tiles
    tempdir = tempfile.TemporaryDirectory()

    # Calculate resolution of tiles
    results_df = oneimg.calc_local_frc(
        QuollImg, tile_size=int(tile_size), tiles_dir=tempdir.name
    )

    show_info(f"Mean resolution is {np.mean(results_df.Resolution)} {unit}")

    # Display resolution results
    table = Table(value=results_df.describe().to_dict())
    viewer.window.add_dock_widget(table, name="Resolution", area="right")
    if save_csv is True:
        results_df.to_csv(results_csv)

    # Display histogram of results
    fig = plt.figure()
    results_df.Resolution.hist()
    plt.xlabel(f"Resolution ({unit})")
    plt.ylabel("Number of tiles")
    viewer.window.add_dock_widget(
        FigureCanvas(fig), name="Histogram of resolution", area="right"
    )

    # Display heatmap of resolutions as layer
    resolution_heatmap = oneimg.plot_resolution_heatmap(
        QuollImg,
        results_df,
    )
    viewer.add_image(
        resolution_heatmap,
        colormap="viridis",
        opacity=0.3,
        # scale=(1 / pixel_size, 1 / pixel_size),
    )

    # Remove tiles directory
    tempdir.cleanup()
