import os
import socket 
import logging
import time
import sys
import json
import RPi.GPIO as GPIO # GPIO PIN CONTROLLER

host, port = 'localhost', '8888'
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#function for gathering sensor 
def ErrorHandler(errortype, error):
	print(errortype + ": " + error)
	if errortype == 'warn':
		logging.warning(errortype + ': ' + error)
	if errortype == 'debug':
		logging.debug(errortype + ': ' + error)
	return

def main():
	#try WAS THIS THE FIRST TIME ALIVE OR A REBOOT?
	# if first time on > Input settings > write to the config
	try:
		CONFIG = open('clientconfig.ini', 'r')
		try:
			json.dump(CONFIG, CONFIG, *, sort_keys=False,)
		except:
			pass #YOUR UNSCRUBBED DATA PASSES FOR NOW!!!! SOON CODE WILL SCRUB YOU
		CONFIG.close()
	except FileNotFoundError:
		ErrorHandler('warn', 'CONFIG.INI:No config file found at boot.')
	#future resilience: try: do we have internet?
	#future resilience: try: do we have a connection to mysql?  		
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
