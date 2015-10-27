import time
from servosix import ServoSix

ss = ServoSix(18, 23)

while True:
    servo = input("servo:")
    angle = input("angle:")
    ss.set_servo(servo, angle)

