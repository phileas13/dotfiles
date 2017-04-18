import fileinput
import configparser
import sys
import getopt
import os

ROFI_PATH = '/home/phileas/.Xresources'
I3CONFIG_PATH = '/home/phileas/.config/i3/config'
TERMITE_PATH = '/home/phileas/.config/termite/config'
help = 'ricer.py -i <inputfile>'

def rollback():
	#os.system('mv ' + rofi_path + '.bak ' + rofi_path)
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

def write_i3(colors, I3CONFIG_PATH):
	#backup(I3CONFIG_PATH)
	findandreplace('        background ', '        background ' + colors['background'], I3CONFIG_PATH)
	findandreplace('        statusline ', '        statusline ' + colors['foreground'], I3CONFIG_PATH)
	findandreplace('        separator ', '        separator ' + colors['foreground'], I3CONFIG_PATH)

def write_rofi(colors, ROFI_PATH):
	#backup(ROFI_PATH)
	findandreplace('rofi.color-window: ', 'rofi.color-window: ' + colors['background'] + ', ' + colors['color0'] + ', '
		+ colors['color10'] + ', ' + colors['color0'], ROFI_PATH)
	findandreplace('rofi.color-normal: ', 'rofi.color-normal: ' + colors['background'] + ', ' + colors['color15'] + ', '
		+ colors['color0'] + ', ' + colors['color10'] + ', ' + colors['color0'], ROFI_PATH)
	findandreplace('rofi.color-active: ', 'rofi.color-active: ' + colors['background'] + ', ' + colors['color15'] + ', '
		+ colors['color0'] + ', ' + colors['color10'] + ', ' + colors['color0'], ROFI_PATH)
	findandreplace('rofi.color-active: ', 'rofi.color-active: ' + colors['background'] + ', ' + colors['color15'] + ', '
		+ colors['color0'] + ', ' + colors['color10'] + ', ' + colors['color0'], ROFI_PATH)
	findandreplace('rofi.color-urgent: ', 'rofi.color-urgent: ' + colors['background'] + ', ' + colors['color9'] + ', '
		+ colors['color0'] + ', ' + colors['color9'] + ', ' + colors['color15'], ROFI_PATH)

def write_termite(colors, TERMITE_PATH):
	findandreplace('foreground_bold', 'foreground_bold      = ' + colors['foreground'] + ' #fett', TERMITE_PATH)
	findandreplace('foreground ', 'foreground      = ' + colors['foreground'] + ' #nomal', TERMITE_PATH)
	findandreplace('cursor', 'cursor      = ' + colors['foreground'], TERMITE_PATH)
	findandreplace('background      = ', 'background      = ' + colors['background'], TERMITE_PATH)
	findandreplace('color0', 'color0      = ' + colors['color0'], TERMITE_PATH)
	findandreplace('color8', 'color8      = ' + colors['color8'], TERMITE_PATH)
	findandreplace('color1', 'color1      = ' + colors['color1'], TERMITE_PATH)
	findandreplace('color9', 'color9      = ' + colors['color9'], TERMITE_PATH)
	findandreplace('color2', 'color2      = ' + colors['color2'], TERMITE_PATH)
	findandreplace('color10', 'color10      = ' + colors['color10'], TERMITE_PATH)
	findandreplace('color3', 'color3      = ' + colors['color3'], TERMITE_PATH)
	findandreplace('color11', 'color11      = ' + colors['color11'], TERMITE_PATH)
	findandreplace('color4', 'color4      = ' + colors['color4'], TERMITE_PATH)
	findandreplace('color12', 'color12      = ' + colors['color12'], TERMITE_PATH)
	findandreplace('color5', 'color5      = ' + colors['color5'], TERMITE_PATH)
	findandreplace('color5', 'color5      = ' + colors['color5'], TERMITE_PATH)
	findandreplace('color13', 'color13      = ' + colors['color13'], TERMITE_PATH)
	findandreplace('color6', 'color6      = ' + colors['color6'], TERMITE_PATH)
	findandreplace('color14', 'color14      = ' + colors['color14'], TERMITE_PATH)
	findandreplace('color7', 'color7      = ' + colors['color7'], TERMITE_PATH)
	findandreplace('color15' , 'color15      = ' + colors['color15'], TERMITE_PATH)
	#Change:
	#findandreplace('color15' , 'color15      = {}'.format(colors['color15']), TERMITE_PATH)



def main(argv, help, I3CONFIG_PATH, ROFI_PATH, TERMITE_PATH):
	if len(argv) == 0:
		print(help)
		sys.exit(2)
	scheme_path = ''
	try:
		opts, args = getopt.getopt(argv,"i:",["ifile="])
	except getopt.GetoptError:
		print(help)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(help)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
	colors = readconfig(inputfile)
	write_i3(colors, I3CONFIG_PATH)
	write_rofi(colors, ROFI_PATH)
	write_termite(colors, TERMITE_PATH)
	reloadconfigs()

if __name__ == '__main__':
	main(sys.argv[1:], help, I3CONFIG_PATH, ROFI_PATH, TERMITE_PATH)
#read config to dict
#back files up
#rewrite files
#restart i3
