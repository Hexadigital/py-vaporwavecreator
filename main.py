import os, random, sys
from shutil import copyfile
from time import sleep

class VaporwaveCreator:
	def __init__(self, filename, bpm):
		if os.path.isfile(filename):
			self._filename = filename
			self._bpm = bpm
			self._measuretime = (60/bpm)*4
			if not os.path.isdir('temp/'):
				os.mkdir('temp/')
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
		piece = random.choice(snippets)
		copyfile("temp/" + piece,"vaporwave.wav")
		measures = [2,4,8]
		while i < 100:
			piece = random.choice(snippets)
			times = random.choice(measures)
			for x in range(0,times):
				os.system('sox --combine concatenate vaporwave.wav ' + "temp/" + piece + " vaporwave2.wav")
				os.remove("vaporwave.wav")
				copyfile("vaporwave2.wav","vaporwave.wav")
				os.remove("vaporwave2.wav")
				sleep(.1)
				i += 1
	
	def finalize(self):
		slowdown = (random.uniform(0.4,0.6))
		print(slowdown)
		os.system("sox --norm vaporwave.wav vaporwave2.wav speed " + str(slowdown))
		os.remove("vaporwave.wav")
		copyfile("vaporwave2.wav","vaporwave.wav")
		os.remove("vaporwave2.wav")
		os.system("sox --norm vaporwave.wav vaporwave2.wav pad 0 5 reverb 85")
		os.remove("vaporwave.wav")
		copyfile("vaporwave2.wav","vaporwave.wav")
		os.remove("vaporwave2.wav")
		os.system("sox --norm vaporwave.wav vaporwave2.wav phaser 0.9 0.85 4 0.23 1.3 -s")
		os.remove("vaporwave.wav")
		copyfile("vaporwave2.wav","vaporwave.wav")
		os.remove("vaporwave2.wav")
		for root, folders, filenames in os.walk('temp/'):
			for filename in [f for f in filenames if (f.endswith('.wav'))]:
				os.remove('temp/'+filename)


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
		vw.finalize()
	else:
		print("TRY: main.py FILENAME BPM")
