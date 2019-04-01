import os

#Returns 0 if the code runs successfully.Otherwise 1
def run_cmd(cmd):
	result = os.system(cmd)
	return result