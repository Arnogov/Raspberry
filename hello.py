from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, send, emit
from led import Led
from temperature import TemperatureSensor
from light import LightSensor
import RPi.GPIO as GPIO
from threading import Thread
app = Flask(__name__)
socketio = SocketIO(app)
#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = Led(18)
blueLed = Led(24)

tempSensor = TemperatureSensor('28-01131a4f0da1')

lightSensor = LightSensor(27)

@app.route('/')
def home():
    temp = tempSensor.read_temp()
    return render_template('home.html', temp=temp)

@app.route('/temp')
def temp():
    temp = tempSensor.read_temp()
    return str(temp)

@app.route('/light')
def light():
    light = lightSensor.read_light()
    if light < 300:
        return 'Il fait jour'
    else:
        return 'Il fait nuit'

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
        redLed.cancel()
    elif color == "blue":
        blueLed.off()
        blueLed.cancel()
    return redirect(url_for('home'))

@app.route('/blink', methods=['POST'])
def blink():
    color = request.form['color']
    numBlink = int(request.form['numBlink'])
    sleepTime = float(request.form['sleepTime'])
    led = None
    if color == "red":
        led = redLed
    elif color == "blue":
        led = blueLed
    thread = Thread(target=led.blink, args=(numBlink, sleepTime, ))
    thread.start()
    return redirect(url_for('home'))

def message_loop():
    while True:
        message = input('Votre message ?')
        socketio.emit('alert', message, Broadcast=True)

# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer 
# en parallèle du serveur.
read_messages = Thread(target=message_loop)
read_messages.start()