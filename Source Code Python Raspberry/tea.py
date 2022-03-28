import time, datetime
#import telepot
#from telepot.loop import MessageLoop
now = datetime.datetime.now()
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
hotPin = 22 #GPIO 25 terkoneksi pada Raspberry pin 21
freshPin = 21 #GPIO 9
coolPin = 19#GPIO 10
coffeePin = 26 #GPIO 7
teaPin = 24 #GPIO 8

GPIO_TRIGGER1 = 35
GPIO_ECHO1 = 15
#GPIO.setup(RELAY, GPIO.OUT) 
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.output(GPIO_TRIGGER1, GPIO.LOW)
# Penomoran GPIO berdasarkan lokasi fisik # mengatur pin outputnya relay menyala
GPIO.setup(hotPin, GPIO.OUT)
GPIO.setup(freshPin, GPIO.OUT)   
GPIO.setup(coolPin, GPIO.OUT)
GPIO.setup(coffeePin, GPIO.OUT)
GPIO.setup(teaPin, GPIO.OUT)
# mengatur pin outputnya relay berhenti
GPIO.output(hotPin, GPIO.HIGH)
GPIO.output(freshPin, GPIO.HIGH)
GPIO.output(coolPin, GPIO.HIGH)
GPIO.output(coffeePin, GPIO.HIGH)
GPIO.output(teaPin, GPIO.HIGH)

def distance1():
    
    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    
    GPIO.output(GPIO_TRIGGER1, False)
    
    StartTime1 = time.time()
    StopTime1 = time.time()
    
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime1 = time.time()
        
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime1 = time.time()
        
        
    #perhitungan jarak
    elapsed1 = StopTime1 - StartTime1
    distance1 = elapsed1 * 17160
   
    print (distance1)
    return distance1

while True:
           
        if distance1() >= 3.5:
              jarak1 = distance1()
              GPIO.output(teaPin, GPIO.LOW)
              print ("Jarak TEH pada gelas = %.1f cm" % jarak1)
              print("\n")
              time.sleep(0.5)
            
        else :
            distance1() == 3.0
            jarak1 = distance1()
            print ("STOP! TEH sudah penuh = %.1f cm" % jarak1)
            print("\n")
            GPIO.output(teaPin, GPIO.HIGH)
            os._exit(0)
            time.sleep(3)
        time.sleep(0.5)