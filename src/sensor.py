import random

import math

import time

class Sensor():
	
	
	def __init__(self):
		import math
		import random
		self.nxt_val_gen = self.sensor_gen()
	
	
	def sensor_gen(self):
		while(1):
			time.sleep(.2)
			rndm_val = random.expovariate(0.1)
			yield rndm_val
	
	def run(self):
		while(1):
			time.sleep(1)
			print(self.nxt_val_gen.next())
