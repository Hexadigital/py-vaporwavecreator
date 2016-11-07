import os, random, sys
from shutil import copyfile
from time import sleep

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
	
	def rejoin(self):
		snippets = []
		for root, folders, filenames in os.walk('temp/'):
			for filename in [f for f in filenames if (f.endswith('.wav'))]:
				snippets.append(filename)
		i = 1
		copyfile("temp/" + random.choice(snippets),"vaporwave.wav")
		while i < 100:
			os.system('sox --combine concatenate vaporwave.wav ' + "temp/" + random.choice(snippets) + " vaporwave2.wav")
			os.remove("vaporwave.wav")
			copyfile("vaporwave2.wav","vaporwave.wav")
			os.remove("vaporwave2.wav")
			i += 1

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
		vw.rejoin()
	else:
		print("TRY: main.py FILENAME BPM")