import os
import socket 
import logging
import time
import sys
import json
import RPi.GPIO as GPIO # GPIO PIN CONTROLLER

tick = 10 # seconds for waiting for next request

inet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inet_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#function for gathering sensor 
def ErrorHandler(errortype, error):
	print(errortype + ": " + error)
	if errortype == 'warn':
		logging.warning(errortype + ': ' + error)
	if errortype == 'debug':
		logging.debug(errortype + ': ' + error)
	return

class SensorGatherer:
	def __init__(self):

	def send((host,address),CMD,DATA):
		

		
def main():
	#try WAS THIS THE FIRST TIME ALIVE OR A REBOOT?
	# if first time on > Input settings > write to the config
	try:
		CONFIG = open('client_config.ini', 'r')
		try:
			json.dump(CONFIG, CONFIG, *, sort_keys=False,)
		except:
			pass 
		#YOUR UNSCRUBBED DATA PASSES!! SOON CODE WILL SCRUB YOU
		CONFIG.close()
		CONFIG 
	except FileNotFoundError:
		ErrorHandler('warn', 'CONFIG.INI:No config file found at boot.')
		continue
	#future resilience: try: do we have internet?
	#future resilience: try: do we have a connection to mysql?  
	while True:
		server_connection, server_address = 
	if controllerupdate = true:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(2, GPIO.OUT) 
		GPIO.output(2, False)
		#GPIO controls the relay pins
	if controllerupdate = true:
		#Main Tank Sensor/Controller
		#read tank depth
		#read pipe pressure
		#open / close water main valve (open/close)
		#open / close recirc/main tank fill valve (flow control)
		#open / close pump exit valve (o/c)
		#open / close main irrigation valve (o/c)
		#regulate flow recirc/main tank fill valve (flow control)	


if __name__ == '__main__':
	Main()
