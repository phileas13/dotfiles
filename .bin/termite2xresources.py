import executor
import configparser
import sys


#XRESOURCES_PATH = '/home/phileas/.Xresources'

def write_xresources(path, colors, options):
	#executor.run('cp ' + path + ' ' + path + '.bak')
	#file = open(path, 'w')
	#file.truncate()
	text = gen_xresources(colors)
	executor.run('cp ' + path + ' ' + path + '.bak')
	file = open(path, 'w')
	file.truncate()
	file.write(text)
	file.close()
	#file.write(xr)
	#file.close()

def gen_rofi(colors, options):
	file = ('! rofi\n'
	'rofi.modi: run\n'
	'rofi.font: ' + options['font'] + ' ' + options['rofi_font_size']
	'rofi.separator-style:	none\n'
	'rofi.lines: 10\n'
	'rofi.hide-scrollbar: true\n'
	'rofi.opacity: 95\n'
	'ofi.color-enabled: true\n'
	'!                    bg       fg      altbg    hlbg     hlfg\n'
	'rofi.color-window: #273238, #273238, #1e2529\n'
	'rofi.color-normal: #273238, #c1c1c1, #273238, #394249, #ffffff\n'
	'rofi.color-active: #273238, #80cbc4, #273238, #394249, #80cbc4\n'
	'rofi.color-urgent: #273238, #ff1844, #273238, #394249, #ff1844\n'
	'rofi.bw: 2\n'
	'rofi.padding: 15\n'
	'rofi.fuzzy: false\n')
	return file

def gen_xresources(colors):
	file = ('! special\n'
	'*.foreground:   ' + colors['foreground'] + '\n'
	'*.background:   ' + colors['background'] + '\n'
	'*.cursorColor:  ' + colors['cursor'] + '\n'

	'! black\n'
	'*.color0:       ' + colors['color0'] + '\n'
	'*.color8:       ' + colors['color8'] + '\n'

	'! red\n'
	'*.color1:       ' + colors['color1'] + '\n'
	'*.color9:       ' + colors['color9'] + '\n'

	'! green\n'
	'*.color2:       ' + colors['color2'] + '\n'
	'*.color10:      ' + colors['color10']+ '\n'

	'! yellow\n'
	'*.color3:       ' + colors['color3'] + '\n'
	'*.color11:      ' + colors['color11'] + '\n'

	'! blue\n'
	'*.color4:       ' + colors['color4'] + '\n'
	'*.color12:      ' + colors['color12'] + '\n'

	'! magenta\n'
	'*.color5:       ' + colors['color5'] + '\n'
	'*.color13:      ' + colors['color13'] + '\n'

	'! cyan\n'
	'*.color6:       ' + colors['color6'] + '\n'
	'*.color14:      ' + colors['color14'] + '\n'

	'! white\n'
	'*.color7:       ' + colors['color7'] + '\n'
	'*.color15:      ' + colors['color15'] + '\n')
	return file

def gen_termite():
	pass

def write_rofi(path, colors, options):
	text = gen_rofi(colors, options)
	executor.run('cp ' + path + ' ' + path + '.bak')
	file = open(path, 'w')
	file.truncate()
	file.write(text)
	file.close()

def write_termite(path, colors, options):
	pass


def readconfig(schemepath):
	config = configparser.ConfigParser()
	config.read(schemepath)
	colors  = config['colors']
	options = config['options']
	files = config['files']
	return colors, options, files

def rollback():
	pass

def main():
	schemepath = sys.argv[1]
	colors, options, files = readconfig(schemepath)
	if 'termite' in files:
		write_termite(files['termite'], colors, options)

	if 'rofi' and 'xresources' in files:
		if files['rofi'] == files['xresources']:
			write_xresources(files['xresources'], colors, rofi=True)
	elif 'rofi' in files:
		write_rofi()
	elif 'xresources' in files:
		write_xresources(files['xresources'], colors)



if __name__ == '__main__':
	main()

#config = configparser.ConfigParser()
#config.read(schemepath)
#color1 = config['colors']['color1']
#foreground      = config['colors']['foreground']
#foreground_bold = config['colors']['foreground_bold']
#cursor          = config['colors']['cursor']
#background      = config['colors']['background']
#color0  = config['colors']['color0']
#color8  = config['colors']['color8']
#color1  = config['colors']['color1']
#color9  = config['colors']['color9']
#color2  = config['colors']['color2']
#	color10 = config['colors']['color10']
#color3  = config['colors']['color3']
#color11 = config['colors']['color11']
#color4  = config['colors']['color4']
#color12 = config['colors']['color12']= 
#color5  = config['colors']['color5']
#color13 = config['colors']['color13']
#color6  = config['colors']['color6']
#color14 = config['colors']['color14']
#color7  = config['colors']['color7']
#color15 = config['colors']['color15']


