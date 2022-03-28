'''
Skill yang saya bangun ini untuk mengontrol Smart Water Dispenser dengan Alexa Echo Dot Gen 3
 - Menggunakan pemanggil Flask-Ask

Menggunakan perintah :
Alexa, tell polines **** water dispenser .....
Echo, tell polines **** water dispenser .....
Amazone, tell polines **** water dispenser .....
Computer, tell polines **** water dispenser .....

Created Idetor by: Chandra Septianoor
https://dispenserchandraseptianoor.pagekite.me/ 
Dimodifikasi pada tanggal: 2019-12-29
'''

from flask import Flask, render_template
from flask_ask import Ask, statement, question
from multiprocessing import Process

import RPi.GPIO as GPIO #Penggunaan penamaan pin GPIO
import logging
import time, datetime
import sys
import subprocess
import os
import multiprocessing
import calendar
import requests
import yaml
now = datetime.datetime.now()

#Inisiaisasi PIN Raspberry Pi 3 B
GPIO.setwarnings(False)
coolPin = 19 #terkoneksi pada Raspberry pin GPIO 10
freshPin = 21 #GPIO 9
hotPin = 22 #GPIO 25
coffeePin = 26 #GPIO 7
teaPin = 24 #GPIO 8

GPIO.setmode(GPIO.BOARD)
#Set.Mode GPIO berdasarkan lokasi fisik
GPIO.setup(freshPin, GPIO.OUT)   
GPIO.setup(coolPin, GPIO.OUT)
GPIO.setup(hotPin, GPIO.OUT)
GPIO.setup(coffeePin, GPIO.OUT)
GPIO.setup(teaPin, GPIO.OUT)
#Mengatur pin outputnya relay menyala
GPIO.output(freshPin, GPIO.LOW)
GPIO.output(coolPin, GPIO.LOW)
GPIO.output(hotPin, GPIO.LOW)
GPIO.output(coffeePin, GPIO.LOW)
GPIO.output(teaPin, GPIO.LOW)
#Mengatur pin outputnya relay berhenti
GPIO.output(freshPin, GPIO.HIGH)
GPIO.output(coolPin, GPIO.HIGH)
GPIO.output(hotPin, GPIO.HIGH)
GPIO.output(coffeePin, GPIO.HIGH)
GPIO.output(teaPin, GPIO.HIGH)


#inisialiasi flask ask
app = Flask(__name__)
ask = Ask(app, '/')
#logging.getLogger('flask_ask').setLevel(logging.DEBUG)

#STATUSON = ['on','LOW']
#STATUSOFF = ['off','HIGH']

@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)
  
@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('fallback_message')
    return question(reprompt_text)

@ask.session_ended
def session_ended():
    return "{}", 2


@ask.intent('FreshIntent')
def on(dispenser):
    command = dispenser
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command =='dispenser':
        GPIO.output(freshPin, GPIO.LOW)
        x=os.fork()
        if x:
            subprocess.call(["python3","/home/pi/Chandra_Septianoor/Smart-Dispenser-Bismillah/fresh.py"])
        else:
            response_text = render_template('command1', freshCommand=command)
            return statement(response_text).simple_card('command1', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt1')
        return question(reprompt_text)

@ask.intent('CoolIntent')
def on(dispenser):
    command = dispenser
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command =='dispenser':
        GPIO.output(coolPin, GPIO.LOW)
        x=os.fork()
        if x:
            subprocess.call(["python3","/home/pi/Chandra_Septianoor/Smart-Dispenser-Bismillah/cool.py"])
        else:
            response_text = render_template('command2', coolCommand=command)
            return statement(response_text).simple_card('command2', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt2')
        return question(reprompt_text)

@ask.intent('HotIntent')
def on(dispenser):
    command = dispenser
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command =='dispenser':
        GPIO.output(hotPin, GPIO.LOW)
        x=os.fork()
        if x:
            subprocess.call(["python3","/home/pi/Chandra_Septianoor/Smart-Dispenser-Bismillah/hot.py"])
        else:
            response_text = render_template('command3', hotCommand=command)
            return statement(response_text).simple_card('command3', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt3')
        return question(reprompt_text)

@ask.intent('CoffeeIntent')
def on(dispenser):
    command = dispenser
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command =='dispenser':
        GPIO.output(coffeePin, GPIO.LOW)
        x=os.fork()
        if x:
            subprocess.call(["python3","/home/pi/Chandra_Septianoor/Smart-Dispenser-Bismillah/coffee.py"])
        else:
            response_text = render_template('command4', coffeeCommand=command)
            return statement(response_text).simple_card('command4', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt4')
        return question(reprompt_text)

@ask.intent('TeaIntent')
def on(dispenser):
    command = dispenser
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command =='dispenser':
        GPIO.output(teaPin, GPIO.LOW)
        x=os.fork()
        if x:
            subprocess.call(["python3","/home/pi/Chandra_Septianoor/Smart-Dispenser-Bismillah/tea.py"])
        else:
            response_text = render_template('command5', teaCommand=command)
            return statement(response_text).simple_card('command5', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt5')
        return question(reprompt_text)

if __name__ == '__main__':
    app.run(debug=True)
