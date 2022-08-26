from napari_quoll._widget import quoll_oneimgfrc


# make_napari_viewer is a pytest fixture that returns a napari viewer object
# capsys is a pytest fixture that captures stdout and stderr output streams

# def test_quoll_widget(make_napari_viewer, capsys):
#     viewer = make_napari_viewer()
#     # layer = viewer.add_image(np.random.random((100, 100)))

#     # this time, our widget will be a MagicFactory or FunctionGui instance
#     my_widget = quoll_oneimgfrc()

#     # if we "call" this object, it'll execute our function
#     my_widget(
#         filename="test_data/SerialFIB57_2048x2048.tif",
#         pixel_size=3,
#         tile_size=512,
#     )

#     # read captured output and check that it's as we expected
#     captured = capsys.readouterr()
#     assert captured.out is not None
