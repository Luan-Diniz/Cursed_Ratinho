from screeninfo import get_monitors
from App.system import Control

#Get screen size
screen_height, screen_width = 0, 0
for monitor in get_monitors():
    if  monitor.is_primary:
        screen_height = monitor.height
        screen_width = monitor.width
if screen_height == 0 or screen_width == 0:
    raise Exception("No primary monitor set: Unable to get the size.")

program = Control(screen_width,screen_height)
program.start()