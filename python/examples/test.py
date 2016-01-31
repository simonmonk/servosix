import time
from servosix import ServoSix

ss = ServoSix()

while True:
    servo = input("servo:")
    angle = input("angle:")
    ss.set_servo(servo, angle)

