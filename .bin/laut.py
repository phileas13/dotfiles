#!/usr/bin/env python3
import subprocess
import sys

import executor

def get_volume():
	volume = executor.run('amixer -D pulse get Master | grep -o "\[.*%\]" | grep -o "[0-9]*" | head -n1')[0]
	#print(volume)
	if volume == '0':
		output = '  muted'
	elif int(volume) <= 30:
		output = ' ' + volume
	elif int(volume) > 30:
		output = ' ' + volume
	return(output)

def set_volume(percentage):
	executor.run('amixer -D pulse sset Master ' + str(percentage) + '%')
	emit_signal()

def emit_signal():
	executor.run('pkill -RTMIN+1 i3blocks')

def write(message):
	sys.stdout.write(message)
	sys.stdout.flush()

def increase(percentage):
	executor.run('amixer -D pulse sset Master ' + str(percentage) + '%+')
	emit_signal()

def decrease(percentage):
	executor.run('amixer -D pulse sset Master ' + str(percentage) + '%-')
	emit_signal()

def mute():
	executor.run('amixer -D pulse sset Master 0%')
	emit_signal

if __name__ == '__main__':
  command = sys.argv[1]

  if command == 'set':
    #set_volume(trim_to_range(sys.argv[2]))
    set_volume(sys.argv[2])
  elif command == 'up':
    #new_volume = trim_to_range(int(get_volume()) + int(sys.argv[2]))
    #set_volume(new_volume)
    increase(sys.argv[2])
  elif command == 'mute':
  	mute()
  elif command == 'down':
    #new_volume = trim_to_range(int(get_volume()) - int(sys.argv[2]))
    #set_volume(new_volume)
    decrease(sys.argv[2])
  elif command == 'get':
    write(get_volume())
  else:
    write('Usage: ' + sys.argv[0] + ' [set|up|down|toggle|read|status] [value]\n')