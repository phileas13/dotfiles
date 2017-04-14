import executor

pingtest = executor.run('ping -c1 8.8.8.8')
if pingtest[1] == 0:
	print(' Up')
else:
	print(' Down') 