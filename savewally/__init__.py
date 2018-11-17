import numpy as np
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


def non_white(mask_array, level=8):
    """
    Returns list of paths to images with any non white values
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
