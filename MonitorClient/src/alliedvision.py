from PySide6.QtCore import *

is_imported = False
try:
    from vimba import *
    is_imported = True
except ImportError:
    print("ERROR: Vimba module importing is failed.")

class Camera():
    def __init__(self):
        self.camera = None

        self.connected = False

        self.url = None

        self.idx = None
        self.gain = None
        self.frame = None
        self.exposure_time = None

    # Camera controling
    def set_parameter(self, idx, value):
        if not self.connected: return
        with Vimba.get_instance() as vimba:
            with self.camera as cam:
                if idx == CAMERA_GAIN:
                    minimum, maximum = cam.GainRaw.get_range()
                    self.gain = minimum + round((maximum - minimum) * value / 200.0)
                elif idx == CAMERA_EXPOSURE_TIME:
                    self.exposure_time = value * 1000.0 # [us]

    def connect_camera(self, url):
        if not is_imported:
            return 'ERROR please install vimba api', False
        self.url = url

        try:
            with Vimba.get_instance() as vimba:
                cams = vimba.get_all_cameras()
                if len(cams) < 1:
                    msg = f'There is no connected GigE camera.'
                    self.connected = False
                    return msg, self.connected
                self.camera = cams[0]
                msg = f'Using device at '
                self.connected = True
        except:
            msg = f'connection is failed.'
            self.connected = False

        return msg, self.connected

    def take_a_picture(self):
        if not self.connected: return
        with Vimba.get_instance() as vimba:
            cams = vimba.get_all_cameras()
            with cams[0] as cam:
                try:
                    minimum, maximum = cam.ExposureTimeAbs.get_range()
                    if minimum <= self.exposure_time <= maximum:
                        cam.ExposureAuto.set('Off')
                        cam.ExposureTimeAbs.set(self.exposure_time)
                except(AttributeError, VimbaFeatureError):
                    pass

                try:
                    cam.GainAuto.set('Off')
                    cam.GainRaw.set(self.gain)
                except(AttributeError, VimbaFeatureError):
                    pass

                try:
                    frame = cam.get_frame()
                    frame.convert_pixel_format(PixelFormat.Mono8)
                    image = frame.as_opencv_image()
                except:
                    image = f'ERROR!'
        return image