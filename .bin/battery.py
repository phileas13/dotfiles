import executor


battery = executor.run("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep 'percentage'")
battery = str(battery)
battery = battery.split(' ')
battery = int(battery[10][:-3])
if 90 <= battery <= 100:
	print(' ' + str(battery) + '%')
if 75 <= battery <= 89:
	print(' ' + str(battery) + '%')
if 50 <= battery <= 74:
	print(' ' + str(battery) + '%')
if 25 <= battery <= 49:
	print(' ' + str(battery) + '%')
if 0 <= battery <= 24:
	print(' ' + str(battery) + '%')
