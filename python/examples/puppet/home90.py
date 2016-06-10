from servosix import ServoSix
import time

ss = ServoSix()

ss.set_servo(1, 90)
ss.set_servo(2, 90)
ss.set_servo(3, 90)
ss.set_servo(4, 90)

time.sleep(1)

print("Servos in 90 degree position")

ss.cleanup()