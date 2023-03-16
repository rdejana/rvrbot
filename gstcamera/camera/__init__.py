
import os

DEFAULT_CAMERA = os.environ.get('JETBOT_DEFAULT_CAMERA', 'zmq_camera')
from .zmq_camera import ZmqCamera
from .opencv_gst_pi_camera import OpenCvGstPiCamera
if DEFAULT_CAMERA == 'zmq_camera':
    from .zmq_camera import ZmqCamera
    Camera = ZmqCamera
else:
    from .opencv_gst_pi_camera import OpenCvGstPiCamera