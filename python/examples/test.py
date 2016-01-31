import time
from servosix import ServoSix

ss = ServoSix()

try:
    while True:
        servo = input("servo:")
        angle = input("angle:")
        ss.set_servo(servo, angle)

finally:
    ss.cleanup()