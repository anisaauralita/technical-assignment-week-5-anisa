import Adafruit_DHT
import time


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

a="Sistem Informasi Suhu"
b="======================="
c="by : Innovator 6"

print(a.center(23))
print(b.center(23))
print(c.center(21))
print("")
    
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if temperature <=15 :
        print("Aktifitas ditunda,")
        print("Karena suhu dingin = {0:0.1f}*C".format(temperature))
        print("Siapkan kehangatan di samping anda.")
        print("")
    elif temperature <=25:
        print("Tetap semangat hari ini,")
        print("Suhu sudah stabil = {0:0.1f}*C".format(temperature))
        print("Selamat beraktifitas.")
        print("")
    elif temperature >25 :
        print("Suhu saat ini = {0:0.1f}*C".format(temperature))
        print("Tetap berada di dalam ruangan supaya kulitmu tidak kering.")
        print("")
    else:
        print("Suhu tidak terdeteksi")

    time.sleep(2.0)
    
