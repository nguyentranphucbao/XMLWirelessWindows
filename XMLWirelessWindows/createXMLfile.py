XMLCode = '''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>{ssid}</name>
	<SSIDConfig>
		<SSID>
			<name>{ssid}</name>
		</SSID>
	</SSIDConfig>
	<connectionType>
		ESS
	</connectionType>
	<connectionMode>
		auto
	</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>{authen}</authentication>
				<encryption>{encryp}</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>{passwd}</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
		<enableRandomization>false</enableRandomization>
		<randomizationSeed>3231738979</randomizationSeed>
	</MacRandomization>
</WLANProfile>
'''

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

keywords = ['{ssid}', '{passwd}', '{authen}', '{encryp}']

SpecialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '~', '`']

from random import *
from .algorithms import replaces
import os
import sys
sys.setrecursionlimit(1500)

class XML(object):
    def __init__(self, ssid, passwd, authen ="WPA2PSK", encryp="AES"):
        self.ssid = ssid
        self.passwd = passwd
        self.authen = authen
        self.encryp = encryp
        self.path = ""
    @property
    def _ssid(self):
        return self.ssid 

    @_ssid.setter
    def _ssid(self, value):
        self.ssid = value

    @property
    def _passwd(self):
        return self.passwd
    
    @_passwd.setter
    def _passwd(self, value):
        self.passwd = value

    @property
    def _authen(self):
        return self.authen

    @_authen.setter
    def _authen (self, value):
        self.authen = value

    @property
    def _encryp (self):
        return self.encryp

    @_encryp.setter
    def _encryp (self,value):
        self.encryp = value

    @property
    def _path(self):
        return self.path

    def initFile(self):
        XML = replaces(XMLCode, keywords, ssid = self.ssid, passwd = self.passwd, authen= self.authen, encryp = self.encryp)
        keywords[0] = self.ssid
        keywords[1] = self.passwd
        keywords[2] = self.authen
        keywords[3] = self.encryp
        namefile = ""
        for i in range(4):
            namefile += char[randrange(0, 52)]
        for i in range(8):
            namefile += str(randrange(10))
        files = open(namefile + '.xml', 'w')
        files.write(XML)
        self.path = namefile + '.xml'

    def delFile(self):
        os.system("del /F " + '"{}"'.format(self.path))
