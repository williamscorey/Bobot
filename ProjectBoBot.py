import explorerhat
import RPi.GPIO
import time
from gpiozero import DistanceSensor
sight = False
def forwards():
    explorerhat.motor.two.forward(100)
    explorerhat.motor.one.backward(100)
def left():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
def right():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
def backwards():
    explorerhat.motor.two.backward(100)
    explorerhat.motor.one.forward(100)
def stop():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def check_for_wall():
    RPi.GPIO.setwarnings(False)
    sensor = DistanceSensor(23,24, max_distance=1, threshold_distance=0.2)
    sensor.when_in_range = sight()
def sight():
    sight == True
def reverse():
    backwards()
    time.sleep(1)
    left()
def sentience():
    sight = False
    if sight == False:
        forwards()
        check_for_wall()
    if sight == True:
        reverse()
        check_for_wall()
        
def test():
    check_for_wall()
    if sight != True:
        check_for_wall()
        
def test2():
    sensor = DistanceSensor(23,24,max_distance=.1,threshold_distance=0)
    sensor.when_in_range = print("Works")