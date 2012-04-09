def eval_loop():
	x = ''
	while True:
		statement = raw_input('Input python command:\n')		
		if statement == 'done':			
			print x
			break
		else:
			x = eval(statement)
			print x

