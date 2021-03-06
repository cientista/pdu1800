__author__ = 'Florian'
from util import get_lan_ip
#################
# CONFIGURATION #
#################


# CHANGE FROM HERE
#

UDP_PORT = 18877
IP = get_lan_ip()
BUFFER_SIZE = 8192
TIMEOUT_IN_SECONDS = 0.1

#
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
SCREEN_DEEP = 32

#
LABEL_RIGHT = 0
LABEL_LEFT = 1

ALIGN_CENTER = 0
ALIGN_RIGHT = 1
ALIGN_LEFT = 2
VALIGN_CENTER = 0
VALIGN_TOP = 1
VALIGN_BOTTOM = 2
#
#
#
BORDER_TOP = 't'
BORDER_BOTTOM = 'b'
BORDER_LEFT = 'l'
BORDER_RIGHT = 'r'
BORDER_TLR = [BORDER_TOP, BORDER_LEFT, BORDER_RIGHT]
BORDER_BLR = [BORDER_BOTTOM, BORDER_LEFT, BORDER_RIGHT]
BORDER_ALL = [BORDER_BOTTOM, BORDER_LEFT, BORDER_RIGHT, BORDER_TOP]

TIME_LABEL_WIDTH=40
TIME_WIDGET_WIDTH=105
#
# Stop changing. Of course - you can do, but it should not be necessary
#
FONT = 'assets/DroidSansMono.ttf'
# set up the colors
BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
RED   =  (255,   0,   0)
GREEN =  (  0, 255,   0)
BLUE  =  (  0,   0, 255)
CYAN  =  (  0, 255, 255)
MAGENTA= (255,   0, 255)
YELLOW = (255, 255,   0)
RPM_YELLOW = (230, 230,   40)
GREY   = (214, 214, 214)
DARK_GREY = (160, 160, 160)

BACKGROUND_COLOR = BLACK
FOREGROUND_COLOR = WHITE
#
#
#

import os, sys, platform
if sys.platform == 'darwin':
    # Display on Laptop Screen on the left
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-400,100)

elif platform.machine() == 'armv7l' and platform.dist()[0] == 'debian':
    if os.path.isfile('/etc/pointercal'):
        os.environ["TSLIB_CALIBFILE"] = '/etc/pointercal'
    os.putenv('SDL_VIDEODRIVER', 'fbcon')
    os.putenv('SDL_FBDEV'      , '/dev/fb1')
    os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
    os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')
    from evdev import InputDevice, list_devices

    devices = map(InputDevice, list_devices())
    eventX=""
    for dev in devices:
        if dev.name == "ADS7846 Touchscreen":
            eventX = dev.fn
    os.environ["SDL_MOUSEDEV"] = eventX
else:
    # Display on Laptop Screen on the left
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (80,80)
