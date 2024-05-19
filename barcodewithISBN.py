from time import sleep
import serial
from serial.tools.hexlify_codec import hex_decode
import io
import RPi.GPIO as GPIO
import urllib.request
import json
import textwrap

###############################
# SET the GPIO Pins for LED
###############################
LED_PIN_ROT = 16
LED_PIN_GELB = 20
LED_PIN_GRUEN = 21

################################
# SETTINGS for bar code scanner
# Use lsusb and dmesg | grep tty
# to find the right USB port
################################
BAUDRATE= 19200
DEVICE = '/dev/ttyACM0'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN_ROT, GPIO.OUT)
GPIO.setup(LED_PIN_GELB, GPIO.OUT)
GPIO.setup(LED_PIN_GRUEN, GPIO.OUT)

def readISBN(isbn):
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    with urllib.request.urlopen(base_api_link + isbn) as f:
        text = f.read()

    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object

    if not obj:
        print("ungueltig")
        return False
    try:
        volume_info = obj["items"][0]
        authors = obj["items"][0]["volumeInfo"]["authors"]

        # displays title, summary, author, domain, page count and language
        print("Title:", volume_info["volumeInfo"]["title"])
        #print("\nSubtitle:", volume_info["volumeInfo"]["subtitle"])
        #print("\nAutor:", volume_info["volumeInfo"]["authors"][0])
    
        #print("\nSummary:\n")
        #print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
        print("Author(s):", ",".join(authors))
        print("Public Domain:", volume_info["accessInfo"]["publicDomain"])
        print("Page count:", volume_info["volumeInfo"]["pageCount"])
        print("Language:", volume_info["volumeInfo"]["language"])
        print("**********************\n")
        return True
    except:
        print("ungültig")
        return False

while True:
    print("Starte lesen")
    print("************")
    with serial.Serial(DEVICE, BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE) as connection:
        byte = connection.read(13)
        #print(byte)
        isbn = byte.decode('utf-8')
        if (readISBN(isbn) == True):
            GPIO.output(LED_PIN_GRUEN, GPIO.HIGH)
        else:     
            GPIO.output(LED_PIN_ROT, GPIO.HIGH)
        sleep(2)
        GPIO.output(LED_PIN_GRUEN, GPIO.LOW)
        GPIO.output(LED_PIN_ROT, GPIO.LOW)
