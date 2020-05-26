from flask import Flask, render_template, redirect, url_for
from led import Led
import RPi.GPIO as GPIO
app = Flask(__name__)

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = Led(14)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/on')
def on():
    redLed.on()
    return redirect(url_for('home'))

@app.route('/off')
def off():
    redLed.off()
    return redirect(url_for('home'))
