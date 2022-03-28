import time, datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO_TRIGGER1  = 40
GPIO_ECHO1 = 16
GPIO_TRIGGER2  = 37
GPIO_ECHO2 = 18
#GPIO.setup(RELAY, GPIO.OUT) 
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.output(GPIO_TRIGGER1, GPIO.LOW)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.output(GPIO_TRIGGER2, GPIO.LOW)


bot = telepot.Bot(token="980188162:AAHghlGhQh982M3c6UUOY5mN5C1PUhKVqnY")
chat_id=1015196226

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

def distance2():
    
    GPIO.output(GPIO_TRIGGER2, True)
    time.sleep(0.00001)
    
    GPIO.output(GPIO_TRIGGER2, False)
    
    StartTime2 = time.time()
    StopTime2 = time.time()
    
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime2 = time.time()
        
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime2 = time.time()
        
        
    #perhitungan jarak
    elapsed2 = StopTime2 - StartTime2
    distance2 = elapsed2 * 17160
   
    print (distance2)
    return distance2

while True:
        
           
        if distance1() >= 18.0 :
              jarak1 = distance1()
             # GPIO.output(teaPin, GPIO.LOW)
              print (str(datetime.datetime.now()))
              print ("Jarak Teh pada tangki = %.1f cm" % jarak1)
              print("\n")
              #bot.sendMessage(chat_id, str(datetime.datetime.now()))
              #bot.sendMessage(chat_id=chat_id, text="Air Teh telah habis")
              #os.close(fd)
              time.sleep(0.5)
              
        elif distance1() >= 9.5 :
            jarak1 = distance1()
            print (str(datetime.datetime.now()))
            print ("Jarak Teh pada tangki = %.1f cm" % jarak1)
            print ("\n")
            #bot.sendMessage(chat_id, str(datetime.datetime.now()))
            #bot.sendMessage(chat_id=chat_id, text=" Air Teh hampir habis")
            time.sleep(0.5)      
            
        else :
            distance1() == 17.0 
            jarak1 = distance1()
            print ("Jarak Teh pada tangki = %.1f cm" % jarak1)
            print("\n")
            #GPIO.output(teaPin, GPIO.HIGH)
           # os.close(fd)
            time.sleep(0.5)
            
            
        time.sleep(0.5)
        
        if distance2() >= 18.0 :
              jarak2 = distance2()
             # GPIO.output(teaPin, GPIO.LOW)
              print (str(datetime.datetime.now()))
              print ("Jarak Kopi pada tangki = %.1f cm" % jarak2)
              print("\n")
              bot.sendMessage(chat_id, str(datetime.datetime.now()))
              bot.sendMessage(chat_id=chat_id, text="Air Kopi telah habis")
              #os.close(fd)
              time.sleep(0.5)
              
        elif distance2() >= 11.0 :
            jarak2 = distance2()
            print (str(datetime.datetime.now()))
            print ("Jarak Kopi pada tangki = %.1f cm" % jarak2)
            print ("\n")
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            bot.sendMessage(chat_id=chat_id, text="Air Kopi hampir habis")
            time.sleep(0.5)
            
        else :
            distance2() == 17.0 
            jarak2 = distance2()
            print ("Jarak Kopi pada tangki = %.1f cm" % jarak2)
            print("\n")
            #GPIO.output(teaPin, GPIO.HIGH)
           # os.close(fd)
            time.sleep(0.5)            
            
        time.sleep(0.5)
