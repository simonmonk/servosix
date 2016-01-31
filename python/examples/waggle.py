from servosix import ServoSix
import time

ss = ServoSix()

period = 0.5

try:
    while (True):  
        ss.set_servo(1, 0)
        time.sleep(period)
        ss.set_servo(1, 180)
        time.sleep(period)
    
finally:
    ss.cleanup()