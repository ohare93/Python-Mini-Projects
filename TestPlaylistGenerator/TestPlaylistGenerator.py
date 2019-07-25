'''
	Test Playlist Generator v1.02
	
	Description: Used to create a test playlist file for VS
	Author: Jordan Munch O'Hare
	Date: 25-07-2019
	
	Optional Arguments:
		1: Filename to read
		2: Location to save file
'''

import time
import sys
from pathlib import Path

nameOfFileToParse = ""
locationToSaveFile = ""
args = sys.argv[1:]
#print(args)

def Argument1FileName():
	global nameOfFileToParse
	nameOfFileToParse = args[0]
	if nameOfFileToParse.find('.') == -1:
		print('Filename error, did you forget the filetype ".txt"?')
		exit()


if len(args) == 0:
	nameOfFileToParse = "tests.txt"
elif len(args) == 1:
	Argument1FileName()
elif len(args) == 2:
	Argument1FileName()
	locationToSaveFile = args[1]
else:
	print("Too many arguments")
	exit()


outFileName = nameOfFileToParse[:nameOfFileToParse.index('.')] + '-' + time.strftime("%Y-%m-%d") + '.playlist'
inputFileName = nameOfFileToParse
testCount = 0

# Check for input file
if(not Path(inputFileName).is_file()):
	print("No input file found. Please create '" + inputFileName + "' with your desired tests on each line.")
	exit()

# Open files, creating the output file if it does not exist
fileIn = open(inputFileName)
fileOut = open(locationToSaveFile + outFileName, 'w+')

##################

fileOut.write('<Playlist Version="1.0">\n')

for line in fileIn:
	if line.strip():
		#print(line.rstrip())	
		fileOut.write('\t<Add Test="' + line.rstrip() + '"/>\n')
		testCount += 1

fileOut.write('</Playlist>')

fileIn.close()
fileOut.close()

print('Generated ' + locationToSaveFile + outFileName + ' with ' + str(testCount) + ' tests')