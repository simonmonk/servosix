# servosix
Python library for controlling servo motors accurately, without any jitter.

This library is of general use for anyone connecting servomotors to their Raspberry Pi, but is designed specifically for the MonkMakes Servo Six board http://monkmakes.com/servo-six.


## Installation

```
$ git clone https://github.com/simonmonk/servosix.git
$ cd servosix/python
$ sudo python setup.py install
```

Many thanks to Richard Hurst for giving me permission to use his rather wonderful ServoBlaster code as part of this project. You can find Richard's original Github repository here: https://github.com/richardghirst/PiBits/tree/master/ServoBlaster

## Getting Started

To get started, attach a servo or several servos using the control pins listed in the next section. If you are using a Servo Six Board from MonkMakes, then attach as many servos as you want as shown below. You need to connect the GND on the Servo Six to the GND on Raspberry Pi and as many control pins on the Servo Six as servo channels that you want to use. Next to each servo channel connector on the top of the Servo Six the GPIO pin to connect to is labeled. For example, channel 1 is connected to GPIO 17, 2 to GPIO 18 etc.:


![ServoSix](http://i1.wp.com/www.monkmakes.com/wp-content/uploads/2016/06/servo_six_pi-web.jpg)

You will also need to attach a 5 or 6V power supply or battery box to the screw terminals.

Now run the test program in the examples folder using:


```
$ cd examples
$ sudo python test.py
servo: 1
angle: 90
```

You will be prompted to enter the servo number (0 to 7) and the angle that you want to set the servo's arm to (0 to 180). When you've had enough press CTRL-C.

There are some other programs that you can use as examples for your own code, including programs for the Monk Makes Puppet Kit for Raspberry Pi (http://monkmakes.com/puppet-kit).


## Pin Allocations

The code defaults to driving 8 servos, the control signals of which should be
connected to P1 header pins as follows:

     Servo number    GPIO number   Pin in P1 header
          0               4             P1-7
          1              17             P1-11
          2              18             P1-12
          3             21/27           P1-13
          4              22             P1-15
          5              23             P1-16
          6              24             P1-18
          7              25             P1-22

P1-13 is connected to either GPIO-21 or GPIO-27, depending on board revision. If you have a very old original Raspberry Pi B revision 1, then use 21. Also keep your Pi safe its a valuable rarity.
