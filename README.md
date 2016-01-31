# servosix
Python library for the ServoSix motor controller from Monkmakes

Many thanks to Richard Hurst for giving me permission to use his rather wonderful ServoBlaster code as part of this project. You can find Richard's original Github repository here: https://github.com/richardghirst/PiBits/tree/master/ServoBlaster

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

P1-13 is connected to either GPIO-21 or GPIO-27, depending on board revision.