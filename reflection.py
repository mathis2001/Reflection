#!/usr/bin/env python3

import sys
import requests

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def main():
	for line in sys.stdin:
		key_wl=[]
		try:
			params = dict(x.split('=') for x in line.split('&'))
			for key, value in params.items():
				key_wl.append(key)
				if len(sys.argv)<2:
					params[key]=value
				else:
					params[key]=sys.argv[1]
			url = '&'.join('{}={}'.format(key, value) for key, value in params.items())
			rq = requests.get(url)
			if len(key_wl) < 2:
				if params[key] in rq.text:
					print(bcolors.INFO+"[REFLECTED]"+bcolors.RESET+url)
				else:
					print(bcolors.FAIL+"[NOT REFLECTED]"+bcolors.RESET+url)
			else:
				for param in key_wl:
					print(bcolors.INFO+"[*]"+bcolors.RESET+" Testing parameter: "+param)
					if param in rq.text:
						print(bcolors.INFO+"[REFLECTED]"+bcolors.RESET+url)
					else:
						print(bcolors.FAIL+"[NOT REFLECTED]"+bcolors.RESET+url)

		except KeyboardInterrupt:
			print("Script canceled.")
			sys.exit(1)
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("A problem has occured.")
		print("Error info:")
		print(e)
