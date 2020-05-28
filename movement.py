import RPi.GPIO as GPIO
from led import Led
import time
from threading import Thread

# Initialisation de notre GPIO 17 pour recevoir un signal
# Contrairement à nos LEDs avec lesquelles on envoyait un signal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class MovementSensor:
    def __init__(self, broche, detectFunction = None, readyFunction = None):
        self.broche = broche
        GPIO.setup(self.broche, GPIO.IN)        
        self.detectFunction = detectFunction
        self.readyFunction = readyFunction
        self.running = False

    def detect(self):
        currentstate = 0
        previousstate = 0
        # Boucle infini jusqu'à CTRL-C
        while self.running:
            # Lecture du capteur
            currentstate = GPIO.input(self.broche)
                # Si le capteur est déclenché
            if currentstate == 1 and previousstate == 0:
                if not (self.detectFunction is None):
                    self.detectFunction()
                # En enregistrer l'état
                previousstate = 1
            # Si le capteur est s'est stabilisé
            elif currentstate == 0 and previousstate == 1:
                if not (self.readyFunction is None):
                    self.readyFunction()
                previousstate = 0
            # On attends 10ms
            time.sleep(0.01)

    def startDetection(self):
        self.running = True
        thread = Thread(target=self.detect)
        thread.start()
        return thread

    def stopDetection(self):
        self.running = False