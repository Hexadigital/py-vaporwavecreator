import os, sys

class VaporwaveCreator:
	def __init__(self, filename, bpm):
		if os.path.isfile(filename):
			self._filename = filename
			self._bpm = bpm
			self._measuretime = (60/bpm)
		else:
			raise IOError("The file specified could not be found.")
	
	def split(self):
		cmd = 'sox "' + self._filename + '" temp/temp.wav trim 0 ' + str(self._measuretime) + " : newfile : restart"
		os.system(cmd)	

if __name__ == "__main__":
	if len(sys.argv) > 2:
		filename = ""
		filename = sys.argv[1]
		try:
			bpm = float(sys.argv[2])
		except ValueError:
			raise ValueError(str(sys.argv[2]) + " is not a valid BPM.")
		vw = VaporwaveCreator(filename, bpm)
		vw.split()
	else:
		print("This script requires the input file name as an argument if run directly.")