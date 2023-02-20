#!/usr/bin/python3
import sys

'''
test data "hello world"
68656c6c6f20776f726c64 
68 65 6c 6c 6f 20 77 6f 72 6c 64
0x68 0x65 0x6c 0x6c 0x6f 0x20 0x77 0x6f 0x72 0x6c 0x64
'''

def colsw(col):
	colors = {
		0: "\033[0;0m",		# default terminal color
		1: "\033[0;91m",	# red
		2: "\033[0;92m",	# green
		3: "\033[0;94m"		# blue
	}
	print(colors[col],end='')

def unx(data):
	data = data.split("0x")
	return data[1]

if len(sys.argv) != 2:
	colsw(1)
	print ("\n[!]  Wrong parameters  [!]\n")
	print ("Run script like: python3 script.py ${hex values}\n")
	print ("Hex values can be formated eg. as:\n\n" +
	"\t68656c6c6f20776f726c64\n" +
	"\t\"68656c6c6f20776f726c64\"\n" +
	"\t\"68 65 6c 6c 6f 20 77 6f 72 6c 64\"\n" + 
	"\t\"0x68 0x65 0x6c 0x6c 0x6f 0x20 0x77 0x6f 0x72 0x6c 0x64\"\n")
	colsw(0)

else:
	hexArr = sys.argv[1].split(" ")
	for hexes in hexArr:
		if '0x' in hexes:
			hexes = unx(hexes)
		colsw(3)
		try:
			print(bytes.fromhex(hexes).decode('utf-8'), end="")
		except:
			print(bytes.fromhex(hexes).decode('ascii'), end="")
	colsw(0)
	print()
