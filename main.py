import os
import shutil

path = "D:/"

for i in os.listdir(path):
	if len(i) == 2:
		print("FOUND: " + i)
		tmpPath = path + i
		print("PATH: " + tmpPath)
		
		if os.access(tmpPath, os.R_OK):
			print("Read perms granted")
		else: 
			print("Read perms not granted")
		if os.access(tmpPath, os.W_OK):
			print("Write perms granted")
		else:
			print("Write perms not granted")
		if os.access(tmpPath, os.X_OK):
			print("Execute perms granted")
		else:
			print("Execute perms not granted")
		print("------------")
		
		shutil.rmtree(tmpPath)
		print("FOLDER REMOVED ")
		
		tmpPath = ""