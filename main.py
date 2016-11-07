import os, sys

class VaporwaveCreator:
	def __init__(self, filename):
		if os.path.isfile(filename):
			self._filename = filename
		else:
			raise IOError("The file specified could not be found.")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = ""
		for i in range(1,len(sys.argv)):
			filename += sys.argv[i] + " "
		filename = filename[:-1]
		print(filename)
		vw = VaporwaveCreator(filename)
	else:
		print("This script requires the input file name as an argument if run directly.")