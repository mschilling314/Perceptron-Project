import common


def classify(w, f):
	d = 0
	for n in range(len(w)):
		d += w[n] * f[n]
	if d >= 0:
		return 1
	return 0



def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	weights = [0, 0, 0]
	lr = 1
	not_done = True
	while not_done:
		not_done = False
		incorrect = 0
		for d in data_train:
			f = [d[0], d[1], 1]
			c = classify(weights, f)
			booler = (c == int(d[2]))
			#print(weights)
			if not booler:
				incorrect += 1
				if c == 1:
					weights[0] -= lr*f[0]
					weights[1] -= lr*f[1]
					weights[2] -= lr*f[2]
				else:
					weights[0] += lr*f[0]
					weights[1] += lr*f[1]
					weights[2] += lr*f[2]
		nooo = incorrect / len(data_train)
		#print(nooo)
		if nooo > 0:
			not_done = True
	for z in data_test:
		f = [z[0], z[1], 1]
		z[2] = classify(weights, f)
	return


def mclassify(weights, f):
	l = []
	for w in weights:
		d = 0
		for n in range(3):
			d += w[n] * f[n]
		l.append(d)
	mind = 0
	maxer = l[0]
	for x in range(1, 10):
		if l[x] > maxer:
			mind = x
			maxer = l[x]
	return mind


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8weights = [0, 0, 0]
	weights = []
	for i in range(10):
		weights.append([0, 0 , 0])
	lr = 0.01
	not_done = True
	while not_done:
		not_done = False
		incorrect = 0
		for d in data_train:
			f = [d[0], d[1], 1]
			c = mclassify(weights, f)
			booler = (c == int(d[2]))
			#print(weights)
			if not booler:
				incorrect += 1
				weights[c][0] -= lr*f[0]
				weights[c][1] -= lr*f[1]
				weights[c][2] -= lr*f[2]
				weights[int(d[2])][0] += lr*f[0]
				weights[int(d[2])][1] += lr*f[1]
				weights[int(d[2])][2] += lr*f[2]
		nooo = incorrect / len(data_train)
		#print(nooo)
		if nooo > 0.02:
			not_done = True
	for z in data_test:
		f = [z[0], z[1], 1]
		z[2] = mclassify(weights, f)
	return
