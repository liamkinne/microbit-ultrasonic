from microbit import *

class Ultrasonic:
	def __init__(self, pin_trig, pin_echo):
		self.pin_trig = pin_trig
		self.pin_echo = pin_echo

		self.pin_echo.read_digital() # set as input

		self.units = {
		  'mm' : 58 / 10,
		  'cm' : 58,
		  'm'  : 58 * 100,
		  'inch' : 148,
		  'feet' : 148 * 12,
		}

		self.unit = self.units['cm']

	def set_units(self, unit):
		if unit in self.units.keys():
			self.unit = unit

	def get(self):
		# pulse trig pin for >10uS
		self.pin_trig.write_digital(True)
		sleep(1)
		self.pin_trig.write_digital(False)
		
		# read pulse length of echo pin
		while self.pin_echo.read_digital() == False:
			pass
		time_start = running_time()
		while self.pin_echo.read_digital() == True:
			pass
		time_end = running_time()
		return (time_end - time_start) * self.unit