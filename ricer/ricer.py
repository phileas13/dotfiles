#!/usr/bin/env python3

import fileinput
import configparser
import sys
import getopt
import os

ROFI_PATH = '/home/phileas/.Xresources'
I3CONFIG_PATH = '/home/phileas/.config/i3/config'
TERMITE_PATH = '/home/phileas/.config/termite/config'
HELP = 'ricer.py -i <inputfile>'

def rollback():
	#os.system('mv ' + rofi_path + '.bak system' + rofi_path)
	pass

def backup(path):
	backupcommand = 'cp ' + path + ' ' + path + '.bak'
	os.system(backupcommand)

def reloadconfigs():
	os.system('xrdb /home/phileas/.Xresources')
	os.system('i3-msg restart') 
	os.system('killall -USR1 termite')

def readconfig(inputfile):
	config = configparser.ConfigParser()
	config.read(inputfile)
	colors  = config['colors']
	return colors#, options, files

def findandreplace(pattern, subst, file):
	x = fileinput.input(file, inplace=1)
	for line in x:
		if pattern in line:
			line = subst
			print(line)
		else:
			sys.stdout.write(line)
	x.close()
			
def iterateforreplace(d, path):
	for key, value in d.items():
		findandreplace(key, value, path)
	
def write_i3(colors, I3CONFIG_PATH):
	#backup(I3CONFIG_PATH)
	d = {
		'        background ': '        background {}'.format(colors['background']),
		'        statusline ': '        statusline {}'.format(colors['foreground']),
		'        separator ': '        separator {}'.format(colors['foreground'])
	}
	iterateforreplace(d, I3CONFIG_PATH)

def write_rofi(colors, ROFI_PATH):
	#backup(ROFI_PATH)
	d = {
		'rofi.color-window: ': 'rofi.color-window: {}, {}, {}, {}'.format(colors['background'], colors['color0'], colors['color10'], colors['color0']),
		'rofi.color-normal: ': 'rofi.color-normal: {}, {}, {}, {}, {}'.format(colors['background'], colors['color15'], colors['color0'], colors['color10'], colors['color0']),
		'rofi.color-active: ': 'rofi.color-active: {}, {}, {}, {}, {}'.format(colors['background'], colors['color15'], colors['color0'], colors['color10'], colors['color0']),
		'rofi.color-active: ': 'rofi.color-active: {}, {}, {}, {}, {}'.format(colors['background'], colors['color15'], colors['color0'], colors['color10'], colors['color0']),
		'rofi.color-urgent: ': 'rofi.color-urgent: {}, {}, {}, {}, {}'.format(colors['background'], colors['color9'], colors['color0'], colors['color9'], colors['color15'])
	}
	iterateforreplace(d, ROFI_PATH)

def write_termite(colors, TERMITE_PATH):
	d = {
		'foreground_bold': 'foreground_bold      = {}'.format(colors['foreground']),
		'foreground ': 'foreground      = {}'.format(colors['foreground']),
		'cursor': 'cursor      = {}'.format(colors['foreground']),
		'background      = ': 'background      = {}'.format(colors['background']),
		'color0': 'color0      = {}'.format(colors['color0']),
		'color8': 'color8      = {}'.format(colors['color8']),
		'color1': 'color1      = {}'.format(colors['color1']),
		'color9': 'color9      = {}'.format(colors['color9']),
		'color2': 'color2      = {}'.format(colors['color2']),
		'color10': 'color10      = {}'.format(colors['color10']),
		'color3': 'color3      = {}'.format(colors['color3']),
		'color11': 'color11      = {}'.format(colors['color11']),
		'color4': 'color4      = {}'.format(colors['color4']),
		'color12': 'color12      = {}'.format(colors['color12']),
		'color5': 'color5      = {}'.format(colors['color5']),
		'color5': 'color5      = {}'.format(colors['color5']),
		'color13': 'color13      = {}'.format(colors['color13']),
		'color6': 'color6      = {}'.format(colors['color6']),
		'color14': 'color14      = {}'.format(colors['color14']),
		'color7': 'color7      = {}'.format(colors['color7']),
		'color15': 'color15      = {}'.format(colors['color15'])
	}
	iterateforreplace(d, TERMITE_PATH)

def main(argv, HELP, I3CONFIG_PATH, ROFI_PATH, TERMITE_PATH):
	if len(argv) == 0:
		print(HELP)
		sys.exit(2)
	scheme_path = ''
	try:
		opts, args = getopt.getopt(argv,"i:",["ifile="])
	except getopt.GetoptError:
		print(HELP)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(HELP)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
	colors = readconfig(inputfile)
	write_i3(colors, I3CONFIG_PATH)
	write_rofi(colors, ROFI_PATH)
	write_termite(colors, TERMITE_PATH)
	reloadconfigs()

if __name__ == '__main__':
	main(sys.argv[1:], HELP, I3CONFIG_PATH, ROFI_PATH, TERMITE_PATH)
