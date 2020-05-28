#import des utilistaires python
import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self, numGPIO):
        self.shouldCancel = False
        # constructeur pour instancier notre objet Buzzer
        # création d'une variable d'instance "Numéro de GPIO"
        self.numGPIO = numGPIO
        # On dit au raspberry qu'on utilise la broche pour "écrire" dessus en mode "sortie"
        GPIO.setup(self.numGPIO, GPIO.OUT)
    
    # méthod "on" pour allumer la Buzzer
    def on(self):
        print('Buzzer '+str(self.numGPIO)+' on')
        # On dit à la broche d'envoyer du courant
        GPIO.output(self.numGPIO, GPIO.HIGH)

    # méthod "off" pour éteindre la Buzzer
    def off(self):
        print('Buzzer '+str(self.numGPIO)+' off')
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

    def beep(self, beepTime):
        self.on()
        time.sleep(beepTime)
        self.off()

    # beep selon un code morse de type '.-'
    # Bonjour = -... --- -. .--- --- ..- .-.
    def morse(self, code): 
        pulse = 0.3
        for character in code:
            if character == '.':
                self.beep(pulse)
            elif character == '-':
                self.beep(pulse * 3)
            else:
                time.sleep(pulse * 2)
            time.sleep(pulse)