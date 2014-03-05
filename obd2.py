#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from obd_conf import auth, obdsim_url
from obd_conf import GREEN, BLUE, PINK, YELLOW, RED, ENDC

class OBDConnection:

	def __init__(self):
		self.content = None
		print PINK + 'Opening connection on ' + BLUE + obdsim_url + ENDC
		try:
			r_string = obdsim_url + "entries.json"
			r = requests.get(r_string, auth=auth)
			if r.status_code == 200:
				print GREEN + 'Successfully connected to ' + obdsim_url + '!' + ENDC
				rj = r.json()
				self.content = rj[u"content"]
			else:
				s_code = "Connection Status Code: {0}".format(r.status_code)
				print RED + s_code + ENDC
				print RED + 'Could not connect! Aborting!' + ENDC
				exit()
		except OSError:
			print RED + 'Could not connect! Aborting!' + ENDC
			exit()

	#gets the ELM 327 version
	def getElmInfo(self):
		try:
			self.ser.write("ATI\r")
			data = self.ser.readline()
			return data[:-1]
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def sendRawCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			return data[:-1]
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def oneByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			split_data = data.split(' ')
			byteA = float(int('0x'+split_data[4], 0 ))
			return byteA
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1

	def twoByteCommand(self, command):
		try:
			self.ser.write(command)
			data = self.ser.readline()
			split_data = data.split(' ')
			byteA = float(int('0x'+split_data[4], 0 ))
			byteB = float(int('0x'+split_data[5], 0 ))
			return byteA, byteB
		except OSError:
			print RED + 'Command timed out!' + ENDC
			return -1, -1


