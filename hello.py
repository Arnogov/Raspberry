from flask import Flask, render_template, redirect, url_for
from led import Led
import RPi.GPIO as GPIO
app = Flask(__name__)

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = Led(14)
blueLed = Led(16)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/on/<color>')
def on(color):
    if color == "red":
        redLed.on()
    elif color == "blue":
        blueLed.on()
    return redirect(url_for('home'))

@app.route('/off/<color>')
def off(color):
    if color == "red":
        redLed.off()
    elif color == "blue":
        blueLed.off()
    return redirect(url_for('home'))
