# running this script will open napari with the stack loaded

import napari
from skimage.io import imread

fname = '/Users/guillermo/Downloads/10x_1.0x_pLPT20&41_single_TiTweez_1_MMStack_Pos0.ome.tif'
im = imread(fname)[:,:,:,1:]
viewer = napari.view_image(
	im, 
	channel_axis=3,
	name=['Phase', 'YFP', 'CFP'],
	colormap=['gray','green','blue']
	)

