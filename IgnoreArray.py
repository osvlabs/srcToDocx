import os
def IgnoreArray():
	array=[]
	if (os.path.exists('.srcignore')):
		fopen = open('.srcignore', 'r')
		for line in fopen:
			array.append(line.strip())
	return array

#print IgnoreArray()  ----Testing the function