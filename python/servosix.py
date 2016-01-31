import time
import os


class ServoSix:
    
    servo_min = 500
    servo_max = 2500
    
    def __init__(self, servo_min=500, servo_max=2500):
        self.servo_min = servo_min
        self.servo_max = servo_max
        # start the service
        os.system("sudo /etc/init.d/servoblaster start")
        
    
    def set_servo(self, servo, angle):
        if servo < 1 or servo > 6:
            print("Servo 1 to 6")
        elif angle < 0 or angle > 180:
            print("Angle 0 to 180")
        else:
            range = self.servo_max - self.servo_min
            scaler = range / 180
            pulse = self.servo_min + angle * scaler
            command = "echo {}={}us > /dev/servoblaster".format(servo, pulse)
            os.system(command)

    def cleanup(self):
        # stop the service
        os.system("sudo killall servoblaster")
        # disable it so it doesn't start after reboot'
        os.system("sudo update-rc.d servoblaster disable")		

