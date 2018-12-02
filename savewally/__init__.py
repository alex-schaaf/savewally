import numpy as np
import tqdm
import os
import matplotlib.pyplot as plt

maxX = 46883
maxY = 63512
SizeTile = 256
# coordinate vector full resolution
Xo = np.arange(maxX)
Yo = np.arange(maxY)
# LL coordinate of tiles
Xto = Xo[::SizeTile]
Yto = Yo[::SizeTile]



def GetFilepath(k, row, col):
    """Returns relative filepath from image root folder."""
    return str(k) + "/" + str(row) + "/" + str(col) + ".png"


def LocateTile (X,Y,SizeTile):
   '''Locate the tile index from the pixel coordinate'''
   return X//SizeTile, Y//SizeTile


def axisTile (Coord, depth):
   '''Locate pixel coordinate from coordinate vector at given depth'''
   return Coord[::2*depth]


def find_nearest(array, value):
   return (np.abs(array - value)).argmin()


def RGB2Lum(patch):
    '''Convert a collection of rgb array to grey using standard luminence equation'''
    return patch[:,:,0]*.2126 + patch[:,:,1]*.7152 + patch[:,:,2]*.0722


def non_white(mask_array, level=8):
    """
    Returns list of image file paths containing any non white values
    """
    image_paths = []
    for i in range(256):
        for j in range(256):
            if mask_array[-i, j]:
                image_path = "Stitch_3/{}".format(sw.GetFilepath(col=i, row=j, k=level))
            else:
                continue
            image_paths.append(image_path)
    return image_paths


def overlap_area(seal_box, patch_box, dx, dy):
    """
    takes two tuples that describe the extents of two boxes and returns the percentage overlap
    """
    a = seal_box
    b = patch_box

    if a[0] >= b[0]:
        width = b[2] - a[0]
    else:
        width = a[2] - b[0]

    if a[1] >= b[1]:
        height = b[3] - a[1]
    else:
        height = a[3] - b[1]

    return (width * height)/(dx * dy * 4)


def read_patches(fp, step=1):
    patches = []
    for patch in tqdm.tqdm(os.listdir(fp)[::step]):
        patch = plt.imread(fp + patch)
        if patch.shape == (50,50,3):
            patches.append(patch)
    return np.array(patches)