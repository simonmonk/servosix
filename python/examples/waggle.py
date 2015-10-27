from servosix import ServoSix
import time

ss = ServoSix(18, 23)

period = 0.5

while (True):  
    ss.set_servo(1, 0)
    time.sleep(period)
    ss.set_servo(1, 180)
    time.sleep(period)