import cameraMock as cam
import time
import unittest 
import math as m

class TestUM(unittest.TestCase):
 
    def setUp(self):
        print("Initialising Camera registers")
        cam.activateCamera();     
        cam.setFormat(cam.FORMAT.YUV422)
        cam.setImageSize(cam.SIZE.SVGA)
        pass

    def test_frameRate(self) :
 
         # Start default camera
        cam.activateCamera();     

        # Set the Framerate.
        cam.setFrameRate(cam.FPS.F30);

        # Number of frames to capture
        num_frames = 120;
        print ("Capturing {0} frames".format(num_frames))
 
        # Start time
        start = time.time()
     
        # Grab few frames
        for i in range(0, num_frames) :
            ret = cam.captureFrame()
      
        # End time
        end = time.time()
 
        # Time elapsed
        seconds = end - start
        print ('Time taken : {0} seconds'.format(seconds))

 
        # Calculate frames per second
        c_fps  = num_frames / seconds;
        print ('Estimated frames per second : {0}'.format(c_fps))
 
        # Release video
        cam.release()

        self.assertEqual( 30, m.floor(c_fps))

if __name__ == '__main__':
    unittest.main()


