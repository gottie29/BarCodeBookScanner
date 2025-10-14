# BarCodeBookScanner
This is a development project of an Bar Code Scanner with Google Book API based an Raspberry Pi 4 with button, switch toggle and scanner

Hardware:
- Raspberry Pi 4 (4GB)
- Barcode Scanner (Yanzeo USB-Barcode-Scanner, CCD-Barcode-Scanner für Computer – Plug-and-Play, schnelles und genaues Scannen, für Bücher, Büro, Lager, Geschäft)
- Button
- Switch toggle
- LED Light

![image](https://github.com/gottie29/BarCodeBookScanner/assets/67120052/96589bf4-8a36-4747-9c58-302b8a19605f)
![image](https://github.com/gottie29/BarCodeBookScanner/assets/67120052/825d9162-d65c-4c04-8ca0-bdce371cf33f)

![image](https://github.com/gottie29/BarCodeBookScanner/assets/67120052/be2b2e3f-1e52-4c40-a0ec-adcc1a04ebc6)


![image](https://github.com/gottie29/BarCodeBookScanner/assets/67120052/e3982a49-8994-4a55-a85a-8240e08d6be3)

# Für OLED i2c-Interface in raspi-config aktivieren:
---------
## I2C aktivieren
sudo raspi-config   # Interface Options → I2C → Enable

<code>
sudo apt-get update
sudo apt-get install -y python3-pip python3-pil i2c-tools
pip3 install --upgrade luma.oled --break-system-packages
</code>

## Test: sollte ein Device zeigen (typisch 0x3C)
sudo i2cdetect -y 1
