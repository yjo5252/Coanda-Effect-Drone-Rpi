import sys
import smbus
import math
import time
from time import sleep  # time module
import RPi.GPIO as GPIO
from Servo import Servo
from Gyro import Gyro

# ---------------------------------------
#  servo_1 은 gyro x 축에 의해 움직이도록
#  servo_2 는 gyro y 축에 의해 움직이도록
#  작성된 코드입니다. (오차는 있을 수 있음)
# ---------------------------------------

GPIO.setmode(GPIO.BCM)

servo_1 = Servo(18, GPIO)
servo_2 = Servo(17, GPIO)
gyro = Gyro()

try:
    while(1):
        accel_x,accel_y,accel_z = gyro.get_accel_data_g()
        x_angle = gyro.get_x_rotation(accel_x, accel_y, accel_z)
        y_angle = gyro.get_y_rotation(accel_x, accel_y, accel_z)
        
        servo_1.motor_ctrl(x_angle)
        servo_2.motor_ctrl(y_angle)
        
except KeyboardInterrupt:
    print("     == stop ==")

servo_1.stop()
servo_2.stop()
GPIO.cleanup()
