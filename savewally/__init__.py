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