import time
from servosix import ServoSix

ss = ServoSix()

recording = []

def playback():
    print(recording)
    for x in range(0, len(recording)-1):
        ss.set_servo(1, recording[x][0])
        ss.set_servo(2, recording[x][1])
        ss.set_servo(3, recording[x][2])
        ss.set_servo(4, recording[x][3])
        time.sleep(0.05)

try:
    while True:
        playback()

except:
    ss.cleanup()
