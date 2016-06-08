# Use the following keys to move servos 1 to 4
# To make an animation, press the spacebar to record the current frame
# To playback the recoded frames press p. This also dumps the frames for use in another program
#
# Servo 1 2 3 4
# Up    1 2 3 4
# Down  q w e r

import time
import sys
import tty
import termios
from servosix import ServoSix

angles = [90, 90, 90, 90]
recording = []
i = 0
ss = ServoSix()

def inc_angle(servo):
    if angles[servo-1] < 180:
        angles[servo-1] += 5
        print("servo " + str(servo) + " set to " + str(angles[servo-1]))
        ss.set_servo(servo, angles[servo-1])


def dec_angle(servo):
    if angles[servo-1] > 0:
        angles[servo-1] -= 5
        print("servo " + str(servo) + " set to " + str(angles[servo-1]))
        ss.set_servo(servo, angles[servo-1])

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

def playback():
    print(recording)
    for x in range(0, i):
        ss.set_servo(1, recording[x][0])
        ss.set_servo(2, recording[x][1])
        ss.set_servo(3, recording[x][2])
        ss.set_servo(4, recording[x][3])
        time.sleep(0.1)

print("x to exit")
while True:
        k = readkey()
        if k == '1':
            dec_angle(1)
        elif k == 'q':
        	    inc_angle(1)
        elif k == '2':
            inc_angle(2)
        elif k == 'w':
        	    dec_angle(2)
        elif k == '3':
            dec_angle(3)
        elif k == 'e':
        	    inc_angle(3)
        elif k == '4':
            inc_angle(4)
        elif k == 'r':
        	    dec_angle(4)
        elif k == ' ':
        	    recording.append(list(angles))
        elif k == 'p':
        	    playback()
        elif k == 'x':
        	    ss.cleanup()
        	    exit()
        	    