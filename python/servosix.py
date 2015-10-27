import time
import RPi.GPIO as GPIO

class ServoSix:
    
    CLK_PIN = 0
    DATA_PIN = 0
    
    t1 = 0.000005      #  uS
    # t1 = 0.00002      #  uS
    t2 = t1 / 2
    t3 = t1 / 4      #  uS
    t4 = t1 - (t2 + t3)
    t5 = t1 * 10
    clk_start_len = 0.003
    repeats = 3
    
    def __init__(self, clk_pin, data_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.CLK_PIN, self.DATA_PIN = clk_pin, data_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CLK_PIN, GPIO.OUT)
        GPIO.setup(self.DATA_PIN, GPIO.OUT)
    
    def send_message(self, x):
        GPIO.output(self.CLK_PIN, 1)
        time.sleep(self.clk_start_len)
        GPIO.output(self.CLK_PIN, 0)
        time.sleep(self.t4)
        for i in range(0, 16):
            bit = x & 1
            x = x >> 1
            GPIO.output(self.DATA_PIN, bit)
            time.sleep(self.t2) # let data stabilize
	        GPIO.output(self.CLK_PIN, 1)
            time.sleep(self.t3)
            GPIO.output(self.CLK_PIN, 0)
	        time.sleep(self.t4)
    
    def set_servo(self, servo, angle):
        if servo < 1 or servo > 6:
            print("Servo 1 to 6")
        elif angle < 0 or angle > 180:
            print("Angle 0 to 180")
        else:
            for i in range(1, self.repeats):
                send_message((6-servo) * 256 + angle)
                time.sleep(0.001)



