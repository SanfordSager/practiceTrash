cd ##	Python driver for Keithley 2400
##	Developed by USC Levenson-Falk Lab, driver convention established by James Farmer
##	Contributors:
##					William S. Sager : williamsager7@gmail.com

## This is the second attempt at a driver for
## The Keithley 2400 Source Meter. The first
## Attempt was incorrectly based on tables of
## Commands which would have likely yielded
## A driver which was not as comprehensive
## As it should be.

import pyvisa as visa
from visa import ResourceManager

# Class with comprehensive set of functions
class K2400SM():
	def __init__(self, address, reset=True):
	'''Initialization sequence for the SourceMeter'''
	# Open the K2400SM
	self.inst = ResourceManager().open_resource(address)
	#Shorthand
	self.w = self.inst.write
	self.r = self.inst.read
	self.q = self.inst.query
	#Print K2400SM string for confirmation
	print(self.q('*IDN?'))
	if reset:
		self.w('*RST')

	## From table 18-1: CALCulate commands
	### There are three sets of CALCulate commands, CALC1, CALC2 and CALC3
	### CALCulate[1]: math expressions

	### CALC2: for limit tests
	### CALC3: statistical data on readings stored in the buffer


	## From table 18-2: DISPlay commands

	## From table 18-3: FORMat commands

	## From table 18-4: OUTPut commands

	## From table 18-5: ROUTe commands

	## From table 18-6: SENSe commands

	## From table 18-7: SOURce commands

	## From table 18-8: STATus commands

	## From table 18-9: SYSTem commands

	## From table 18-10: TRACe commands

	## From table 18-11: TRIGger commands
