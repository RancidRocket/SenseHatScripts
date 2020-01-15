#defining libraries
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

#defining humidity measurement function to print
def humidity():
	humid = sense.get_humidity()
	strhumid = (str(int(humid)))
	print("~~~~~~~~~")
	print(strhumid + "\% H \n")
	

#defining barometric pressure measurement function to print
def barometric():
	pressure = sense.get_pressure()
	strpressure = (str(int(pressure)))
	print(strpressure + "mbar \n")
	
#defining thermometer function to print
def thermometer():
	temp = sense.get_temperature()
	prtemp = (int(float(str(temp))))
	print(str(prtemp - 10) + "degC \n")
	print("~~~~~~~~~")

#do it again
while True:	
	sleep(1)
	humidity()
	barometric()
	thermometer()