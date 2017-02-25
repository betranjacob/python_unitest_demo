''' Mock Camera Module '''
from enum import Enum
import time
class FPS(Enum):
    F15 = 1
    F30 = 2
    F60 = 3

class FORMAT(Enum):
    YUV444 = 1
    YUV422 = 2
    YUV411 = 3

class SIZE(Enum):
    CIF = 1
    VGA = 2
    SVGA = 3
    HD = 4

#default parameters
cameraHandle = 0
cameraFps = FPS.F15
imageFormat = FORMAT.YUV411
imageSize = SIZE.VGA

def activateCamera () :
    pass;

def setFormat (s):
    imageFormat = s

def setImageSize (s):
     imageSize = s

def setFrameRate (f) :
    cameraFps = f
    
'''Grabs, decodes and returns the next video frame. '''
def captureFrame () :
    time.sleep(0.032) # Mocking capture
    return  True

def release () :
    pass








