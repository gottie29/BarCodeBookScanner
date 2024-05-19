import RPi.GPIO as GPIO
import time
LEFT_PIN = 23
RIGHT_PIN = 18
LED_PIN_ROT = 16
LED_PIN_GELB = 20
LED_PIN_GRUEN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT_PIN, GPIO.IN)
GPIO.setup(RIGHT_PIN, GPIO.IN)
GPIO.setup(LED_PIN_ROT, GPIO.OUT)
GPIO.setup(LED_PIN_GELB, GPIO.OUT)
GPIO.setup(LED_PIN_GRUEN, GPIO.OUT)

while True:
    if GPIO.input(LEFT_PIN) == GPIO.HIGH:
        print("LEFT")
        GPIO.output(LED_PIN_ROT, GPIO.HIGH)
    elif GPIO.input(RIGHT_PIN) == GPIO.HIGH:
        print("Right")
        GPIO.output(LED_PIN_GELB, GPIO.HIGH)
    
    time.sleep(0.5)
    GPIO.output(LED_PIN_ROT, GPIO.LOW)
    GPIO.output(LED_PIN_GELB, GPIO.LOW)
    time.sleep(0.5)