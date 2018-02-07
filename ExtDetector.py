import os
def is_img(path):
	(name,ext) = os.path.splitext(path)
	if ext == '.jpg':
		return True
	elif ext == '.png':
		return True
	elif ext == '.jpeg':
		return True
	else:
		return False
