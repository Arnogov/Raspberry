#import des utilistaires python
import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, numGPIO):
        self.shouldCancel = False
        # constructeur pour instancier notre objet Led
        # création d'une variable d'instance "Numéro de GPIO"
        self.numGPIO = numGPIO
        # On dit au raspberry qu'on utilise la broche pour "écrire" dessus en mode "sortie"
        GPIO.setup(self.numGPIO, GPIO.OUT)
    
    # méthod "on" pour allumer la led
    def on(self):
        print('Led '+str(self.numGPIO)+' on')
        # On dit à la broche d'envoyer du courant
        GPIO.output(self.numGPIO, GPIO.HIGH)

    # méthod "off" pour éteindre la led
    def off(self):
        print('Led '+str(self.numGPIO)+' off')
        # on dit à la broche d'arrêter d'envoyer du courant
        GPIO.output(self.numGPIO, GPIO.LOW)

    def cancel(self):
        self.shouldCancel = True

    def blink(self, numBlink, sleepTime):
        i = 0
        self.shouldCancel = False
        while i < numBlink and not self.shouldCancel:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i += 1