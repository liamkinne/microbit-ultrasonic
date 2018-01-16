from microbit import *

class Ultrasonic:
	def __init__(self, pin_trig, pin_echo):
		self.pin_trig = pin_trig
		self.pin_echo = pin_echo

		self.units = {
		  'mm' : 58 * 10,
		  'cm' : 58,
		  'm'  : 58 / 100,
		  'inch' : 148,
		  'feet' : 148 / 12,
		}

		self.unit = units['cm']

	def set_units(self, unit):
		if unit in self.units.keys():
			self.unit = unit
