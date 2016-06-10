import time
from servosix import ServoSix

ss = ServoSix()

recording = [[155, 85, 80, 30], [155, 90, 80, 40], [155, 95, 80, 55], [155, 100, 80, 65], [155, 105, 80, 75], [155, 100, 80, 65], [155, 95, 80, 50], [155, 90, 80, 40], [155, 85, 80, 30], [145, 85, 75, 30], [135, 85, 70, 30], [120, 85, 65, 30], [110, 85, 60, 30], [100, 85, 55, 30], [110, 85, 60, 30], [125, 85, 65, 30], [135, 85, 70, 30], [145, 85, 75, 30], [155, 85, 80, 30]]

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
