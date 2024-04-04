# running this script will open napari with the stack loaded

import napari
from skimage.io import imread

fname = '/Users/guillermo/Downloads/10x_1.0x_pLPT20&41_single_TiTweez_1_MMStack_Pos0.ome.tif'
viewer = napari.view_image(imread(fname'), channel_axis=3)

