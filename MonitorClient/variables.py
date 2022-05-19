from dataclasses import dataclass, field
import numpy as np

CONNECT_CAMERA = 10001
CONNECT_CONTROLLER = 10002

# BPM
NUMBER_OF_MONITORS = 2
RPI_ADDR = '10.1.30.202'

### PV NAMES
PV_NAME_RANK0 = 'BPM'
PV_NAME_RANK1 = 'MONITOR'

### CAPROTOCOL
ACTUATOR_REQUEST_NOTHING = 0
ACTUATOR_REQUEST_STATUS = 1
ACTUATOR_REQUEST_GO_UP = 2
ACTUATOR_REQUEST_GO_DOWN = 3

### ACTUATOR
ACTUATOR_TIME_LIMIT = 5.0
ACTUATOR_DEFAULT = 0
ACTUATOR_UP = 1
ACTUATOR_DOWN = 2
ACTUATOR_GOES_UP = 3
ACTUATOR_GOES_DOWN = 4
ACTUATOR_ERROR = -1

# CAMERA
### CAMERA STATUS
CAMERA_REQUEST_NOTHING = 20000
CAMERA_REQUEST_STREAM = 20001
CAMERA_REQUEST_CAPTURE = 20002
CAMERA_REQUEST_STOP = 20003
CAMERA_REQUEST_DISCONNECT = 20004

CAMERA_GAIN = 30001
CAMERA_FPS = 30002
CAMERA_EXPOSURE_TIME = 30003
CAMERA_REPEAT = 30004
CAMERA_ROI_X0 = 30005
CAMERA_ROI_Y0 = 30006
CAMERA_ROI_WIDTH = 30007
CAMERA_ROI_HEIGHT = 30008
CAMERA_ROTATION_LEFT = 30009
CAMERA_ROTATION_RIGHT = 30010
CAMERA_FLIP_RIGHT_LEFT = 30011
CAMERA_FLIP_UP_DOWN = 30012

CAMERA_SHOW = 40001
CAMERA_EXIT = 40002

PICTURE_SCREEN = 50001
LIVE_XPROFILE_SCREEN = 50002
LIVE_YPROFILE_SCREEN = 50003
PROFILE_SCREEN = 50004
XSIZE_SCREEN = 50005
YSIZE_SCREEN = 50006

NO_FILTER = 60000
BKG_SUBSTRACTION = 60001
GAUSSIAN_FILTER = 60002
MEDIAN_FILTER = 60003
BILATERAL_FILTER = 60004

# Return Queue
STREAM = 70000
ANALYSIS = 70001

@dataclass
class Parameters:
    # Flags
    cam_conn: bool = False
    ctl_conn: bool = False

    calibrated: bool = False
    
    roi_sel: bool = False
    filtered: bool = False
    fliped: bool = False

    # Controller
    server_ip: str = ''
    monitor_id: str = ''
    act_status: int = ACTUATOR_DEFAULT
    act_request: int = ACTUATOR_REQUEST_NOTHING

    # Camera
    url: str = ''
    sdk: str = ''
    cam_request: int = CAMERA_REQUEST_NOTHING

    gain: int = 0 #%
    exp_time: int = 5000 #us
    fps: int = 20
    repeat: int = 1

    # Image
    stream_size: list = field(default_factory=list)
    intensity_line: list = field(default_factory=list)

    calibration_angle: float = 0.0
    cal_target_points: dict = field(default_factory=dict) # {'PointX':[[xpixel, ypixel],[xreal, yreal]]} 
    cal_dest_points: dict = field(default_factory=dict)
    transform_matrix: np.array = field(default_factory=np.array)

    pixel_per_mm: list = field(default_factory=list)

    roi: list = field(default_factory=list)

    filter_code: int = NO_FILTER
    filter_para: dict = field(default_factory=dict)

    rotation: int = 0
    flip_rl: int = 0
    flip_ud: int = 0
    
    current: float = 0.0

    # Beam
    coordinate_center: list = field(default_factory=list) # [xpixel, ypixel]
    #beam_center: list = field(default_factory=list) # [[xpixel, ypixel], [xreal, yreal]]
    #fit_parameters: list = field(default_factory=list)
    #beam_width: list = field(default_factory=list)

    def __init__(self):
        self.stream_size: list = [0,0]
        self.intensity_line: list = [-1,-1]
        self.cal_target_points = {'Point1':[[0,0],[0,0]], 'Point2':[[0,0],[0,0]], 'Point3':[[0,0],[0,0]], 'Point4':[[0,0],[0,0]]}
        self.cal_dest_points = {'Point1':[[0,0],[0,0]], 'Point2':[[0,0],[0,0]], 'Point3':[[0,0],[0,0]], 'Point4':[[0,0],[0,0]]}
        self.transform_matrix = np.array([])
        self.pixel_per_mm = [1.0,1.0]
        self.roi = [[0,0],[0,0],[0,0],[0,0]]
        self.filter_para = {}
        self.coordinate_center = [0,0]

    def set_parameter(self, idx, value=None):
        if idx == CAMERA_GAIN:
            self.gain = float(value)
        elif idx == CAMERA_EXPOSURE_TIME:
            self.exp_time = round(value)
        elif idx == CAMERA_FPS:
            self.fps = int(value)
        elif idx == CAMERA_REPEAT:
            self.repeat = value
        elif idx == CAMERA_ROTATION_RIGHT:
            self.rotation += 90
            self.rotation = self.rotation % 360
        elif idx == CAMERA_ROTATION_LEFT:
            self.rotation += 270
            self.rotation = self.rotation % 360
        elif idx == CAMERA_FLIP_UP_DOWN:
            self.flip_ud += 1
            self.flip_ud = self.flip_ud % 2
        elif idx == CAMERA_FLIP_RIGHT_LEFT:
            self.flip_rl += 1
            self.flip_rl = self.flip_rl % 2
        elif idx == CAMERA_REQUEST_CAPTURE:
            self.repeat = value
            self.cam_request = CAMERA_REQUEST_CAPTURE
        elif idx in [CAMERA_REQUEST_STOP, CAMERA_REQUEST_STREAM]:
            self.cam_request = idx
    
    def is_default(self, para):
        for key, value in self.__dict__.items():
            if value == para:
                return True
        return False