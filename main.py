import sys

if __name__ == "__main__":
	if len(sys.argv) > 1:
		filename = ""
		for i in range(1,len(sys.argv)):
			filename += sys.argv[i] + " "
		filename = filename[:-1]
		print(filename)
	else:
		print("This script requires the input file name as an argument if run directly.")