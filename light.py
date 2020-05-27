import RPi.GPIO as GPIO
import time

class LightSensor: 
    def __init__(self, broche):
        # Numéro de la broche que nous allons utiliser pour lire 
        # les données
        self.broche = broche

    def read_light(self):
        lightCount = 0 #intitialisation de la variable de lumière
        GPIO.setup(self.broche, GPIO.OUT)
        GPIO.output(self.broche, GPIO.LOW)
        time.sleep(0.1) # on draine la charge du condensateur
        GPIO.setup(self.broche, GPIO.IN)
        #Tant que la broche lit ‘off’ on incrémente notre variable
        while (GPIO.input(self.broche) == GPIO.LOW):
            lightCount += 1
        return lightCount