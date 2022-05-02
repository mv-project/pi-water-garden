#library
import time
import schedule
import RPi.GPIO as GPIO
#from picamera import PiCamera

"""
GPIO setup -- pin 29 = moisture sensor; pin 7 = LED
Sensor: 
LED: GPIO 7,
Sensor: GPIO 29,
Relay 1: GPIO 37, 
Relay 2: GPIO 38.
"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

#photo settings 
#camera = PiCamera()
#camera.resolution = (2592, 1944)
#camera.framerate = 15

#variabili
interval = 120 #time in second to restart the cicle
water = 12 #time in second to leave the pump open
idro = 40 # % of umidity soil
control = 5 #time in second before make the second turn
watertwo = 6 #time in second to leave the pump open at second time
second = 1 #check if the second turn is made
#pic_num = 1

def job():
  			at
    while True:
        #accensione led
        GPIO.output(7,True)
        #start led and sensor and view photo 
        #camera.start_preview()
        GPIO.output(38,True)
        time.sleep(5)
        """
        the first ^if^ check if the soil humidity il less than 40% and give water or richeck after an hour with the second ^if^, the variables /second/ check if the second turn was made
        """
        if (GPIO.input(29))<=idro:
                GPIO.output(37,True)
                time.sleep(water)
                GPIO.output(37,False)
                time.sleep(control)
            if (GPIO.input(29))<=idro:
                    GPIO.output(37,True)
                    time.sleep(watertwo)
                    GPIO.output(37,False)
                    secondo = 2
             else:
        		# set off led and sensor and take the photo
        		GPIO.output(38,False)
        		GPIO.output(7,False)
             return
         else:
           if second == 1:
           		time.sleep(interval)
           		do(job,'its dry')
            else:
              return
              
                 
        """
        camera.capture('/home/pi/Pictures/pic_%03d.jpg' % (pic_num))
        camera.stop_preview()
        pic_num = pic_num + 1
        """
        
        #every day at (21:30) starts 'def job():' 
schedule.every().day.at("21:30").do(job,'sto innafiando')

        #Wait for interval period, flashing LED every 30 seconds
        """
        count_AA = 0
        while count_AA < (interval * 2):
            count_BB = 0
            while count_BB < 5:
                GPIO.output(7,True)
                time.sleep(0.5)
                GPIO.output(7,False)
                time.sleep(0.5)
                count_BB = count_BB + 1
            time.sleep(25)
            count_AA = count_AA + 1
		"""
finally:
    #reset GPIO pin before end
    GPIO.cleanup()