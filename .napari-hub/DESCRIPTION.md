<!-- This file is a placeholder for customizing description of your plugin 
on the napari hub if you wish. The readme file will be used by default if
you wish not to do any customization for the napari hub listing.

If you need some help writing a good description, check out our 
[guide](https://github.com/chanzuckerberg/napari-hub/wiki/Writing-the-Perfect-Description-for-your-Plugin)
-->

# Description

This Napari plugin allows you to estimate the local resolution of images using the Fourier Ring Correlation (FRC). 

## How it works

Quoll splits the input image into square tiles of a user specified size. This tile is then split into two sets of sub-image pairs, and the average FRC resolution of these sets is calculated. A calibration factor is applied to match this one-image FRC measurement to the standard two-image FRC resolution.

## What was Quoll developed for?

Quoll was developed for cryo-electron microscopy images. 

# Who is this for?

Anyone who might want to measure spatial variations in image resolution. See [Quoll](https://github.com/rosalindfranklininstitute/quoll) if you would like to access the command-line interface option for batch-scripting, or if you would like to customise the tool for your needs.

# Getting started

## Installation

In a terminal, create a new conda environment and install the latest version of `napari-quoll`. 

```
conda create -n napari-quoll pip
conda activate napari-quoll
pip install git+https://github.com/rosalindfranklininstitute/napari-quoll.git
```

Launch Napari
```
python -m napari
```

(If that does not work, run `pip install napari[all]` and try again)

## Napari-quoll plugin

Napari-quoll should be under the plugins menu at the top.

The menu should pop up on the right. 

1. Open the image you would like to try this with and choose it from the dropdown menu (a test image is included [here](https://github.com/rosalindfranklininstitute/napari-quoll/tree/main/test_data)). 
2. Specify the pixel size in physical units. The test image pixel size is 3 nm.
3. Specify the tile-size in pixel units (how fine the resolution map should be)
4. Specify if you would like to save the results as .csv and the filepath for this.
5. Click run! 

Once complete, the resolution map should be shown in the main window, and summary statistics and a histogram of resolutions should pop up on the bottom right, though these windows might need resizing.

# FAQ

### 1. What tile size should I use?

The minimum tile size is 128 x 128 pixels, the smaller the tile the finer the resolution map, though if the tile is too small, there might not be any features to calculate resolution on.

### 2. How was the one-image FRC calibrated to match the two-image FRC?

The original implementation by [Koho et al](https://github.com/sakoho81/miplib) obtained a calibration function based on a set of pairs of optical microscopy images taken at different pixel sizes. We have repeated this with cryo-electron microscopy images to ensure that our calibration is correct for EM images.

# Getting help

Submit an [issue](https://github.com/rosalindfranklininstitute/napari-quoll/issues) :)

# Citations/Links

### 1. Original implementation of single-image FRC resolution measurement

Koho, S. et al. Fourier ring correlation simplifies image restoration in fluorescence microscopy. [Nat. Commun. 10 3103 (2019).](https://www.nature.com/articles/s41467-019-11024-z)

### 2. Quoll - adapted implementation for local resolution measurement of cryo-EM images
Elaine Ho. (2022). rosalindfranklininstitute/quoll: v0.0.1 (v0.0.1). Zenodo. https://doi.org/10.5281/zenodo.6958768
