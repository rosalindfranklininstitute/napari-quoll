# make_napari_viewer is a pytest fixture that returns a napari viewer object
# capsys is a pytest fixture that captures stdout and stderr output streams

from pathlib import Path
from unittest.mock import patch

import numpy as np
import tifffile

from napari_quoll._widget import quoll_oneimgfrc


def test_quoll_widget(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((256, 256)))

    # this time, our widget will be a MagicFactory or FunctionGui instance
    quoll_widget = quoll_oneimgfrc()

    # if we "call" this object, it'll execute our function
    quoll_widget(
        data=layer.data,
        pixel_size=3,
        tile_size=128,
        save_csv=False,
    )

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out is not None


def test_save_results_csv(make_napari_viewer):
    # get test data
    data = tifffile.imread("./test_data/SerialFIB57_2048x2048.tif")

    viewer = make_napari_viewer()
    layer = viewer.add_image(data)

    # run quoll and save csv
    quoll_widget = quoll_oneimgfrc()

    with patch("pandas.DataFrame.to_csv") as to_csv_mock:
        quoll_widget(
            data=layer.data,
            pixel_size=3,
            tile_size=512,
            save_csv=True,
        )
        to_csv_mock.assert_called_with(Path("results.csv"))
