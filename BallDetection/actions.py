from __future__ import division
import math
import time
import Adafruit_PCA9685
#for handeling ctrl+C
import signal
import sys

class Actions:

    pwm = Adafruit_PCA9685.PCA9685()

    servo_min = 150
    servo_max = 600
    servo_mid = (int)((servo_min + servo_max)/2)
    servo_range = servo_max - servo_min
    speed=0.1

    head = 7
    front_left  = 1
    front_right = 2
    back_left   = 3
    back_right  = 4

    def rotateRight(self):
        x=0
        i = 0
        while True:
            back_right_value  = (int)(((math.sin(x)*0.1+0.5)*self.servo_range) +self.servo_min)
            back_left_value  = (int)(((math.cos(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            self.pwm.set_pwm(self.back_right, 0, back_right_value)
            self.pwm.set_pwm(self.back_left, 0, back_left_value)

            #larger addition = more speed!
            x += self.speed

            if(x > math.pi*2):
              x -= math.pi*2

            i += 1

        self.reset()


    def rotateLeft(self):
        x=0
        i = 0
        while i < 100:
            back_right_value  = (int)(((math.cos(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            back_left_value  = (int) (((math.sin(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            self.pwm.set_pwm(self.back_right, 0, back_right_value)
            self.pwm.set_pwm(self.back_left, 0, back_left_value)

            #larger addition = more speed!
            x += self.speed

            if(x > math.pi*2):
              x -= math.pi*2
            i += 1
        self.reset()



    def walkStraight(self):
        x=0
        i = 0
        while i < 100:
            front_right_value = (int)(((math.sin(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            front_left_value = (int)(((math.sin(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            back_right_value  = (int)(((math.cos(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            back_left_value  = (int)(((math.cos(x)*0.1+0.5)*self.servo_range)+self.servo_min)
            self.pwm.set_pwm(self.front_right, 0, front_right_value)
            self.pwm.set_pwm(self.front_left, 0, front_left_value)
            self.pwm.set_pwm(self.back_right, 0, back_right_value)
            self.pwm.set_pwm(self.back_left, 0, back_left_value)

            #larger addition = more speed!
            x += self.speed

            if(x > math.pi*2):
              x -= math.pi*2
            i += 1
        self.reset()

    def reset(self):
        self.pwm.set_pwm(self.head, 0, self.servo_mid)
        self.pwm.set_pwm(self.front_left, 0, self.servo_mid)
        self.pwm.set_pwm(self.front_right, 0, self.servo_mid)
        self.pwm.set_pwm(self.back_left, 0, self.servo_mid)
        self.pwm.set_pwm(self.back_right, 0, self.servo_mid)


