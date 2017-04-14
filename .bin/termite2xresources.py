import executor
import configparser
import sys


XRESOURCES_PATH = '/home/phileas/.Xresources'

def write_xresources(path, colors):
	#executor.run('cp ' + path + ' ' + path + '.bak')
	#file = open(path, 'w')
	#file.truncate()
	xr = ('! special\n'
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
	#file.write(xr)
	#file.close()
	print(xr)


def readconfig(schemepath):
	config = configparser.ConfigParser()
	config.read(schemepath)
	colors  = config['colors']
	return colors

def main():
	schemepath = sys.argv[0]
	config = readconfig(schemepath)
	write_xresources(XRESOURCES_PATH, colors)

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


