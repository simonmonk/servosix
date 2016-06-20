import time
from servosix import ServoSix
import RPi.GPIO as GPIO

PIR_PIN = 7

ss = ServoSix()
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

recording = [[150, 85, 85, 10], [145, 85, 85, 10], [140, 85, 85, 10], [135, 85, 85, 10], [130, 85, 85, 10], [125, 85, 85, 10], [120, 85, 85, 10], [115, 85, 85, 10], [110, 85, 85, 10], [105, 85, 85, 10], [100, 85, 85, 10], [95, 85, 85, 10], [90, 85, 85, 10], [85, 85, 85, 10], [80, 85, 85, 10], [75, 85, 85, 10], [70, 85, 85, 10], [70, 85, 85, 10], [75, 85, 85, 10], [80, 85, 85, 10], [85, 85, 85, 10], [90, 85, 85, 10], [85, 85, 85, 10], [80, 85, 85, 10], [75, 85, 85, 10], [70, 85, 85, 10], [75, 85, 85, 10], [80, 85, 85, 10], [85, 85, 85, 10], [90, 85, 85, 10], [95, 85, 85, 10], [100, 85, 85, 10], [105, 85, 85, 10], [110, 85, 85, 10], [115, 85, 85, 10], [120, 85, 85, 10], [125, 85, 85, 10]]

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
        if GPIO.input(PIR_PIN):
            print("Triggered")
            playback()
            time.sleep(1)

except:
    ss.cleanup()
