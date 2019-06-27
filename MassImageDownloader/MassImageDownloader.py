'''
	Mass Image Downloader v1.00
	
	Description: Used to download a list of images, recognising their file names and types
	Author: Jordan Munch O'Hare
	Date: 27-06-2019
'''

import urllib.request
import imghdr
import time
import sys
import shutil
import os
import re
from pathlib import Path

# Take in optional arguments, which can specify the filename
nameOfFileToParse = ""
args = sys.argv[1:]
#print(args)
if(len(args) == 0):
	nameOfFileToParse = "images.txt"
elif(len(args) == 1):
	nameOfFileToParse = args[0]
	if nameOfFileToParse.find('.') == -1:
		print('Filename error, did you forget the filetype ".txt"?')
		exit()
else:
	print("Too many arguments")
	exit()

outFolderName = nameOfFileToParse[:nameOfFileToParse.index('.')] + '-' + time.strftime("%Y-%m-%d") + "/"
outFileName = outFolderName + "_Log" + '.txt'
inputFileName = nameOfFileToParse
lineCount = 0

outFolder = Path(outFolderName)
if(outFolder.is_dir()):
	try:
		shutil.rmtree(outFolderName)
	except OSError as e:
		print ("Error deleting folder: %s - %s." % (e.filename, e.strerror))
		exit()
try:
	outFolder.mkdir(parents=True, exist_ok=True)
except WindowsError as e:
	print ("Error creating folder: %s - %s." % (e.filename, e.strerror))
	exit()

# Check for input file
if(not Path(inputFileName).is_file()):
	print("No input file found. Please create '" + inputFileName + "' with your links on each line.")
	exit()

# Open files, creating the output file if it does not exist
fileIn = open(inputFileName)
fileOut = open(outFileName, 'w+')

##################

cLine = ""
cHasExt = False
cFileName = outFolderName + ""
cFileType = ""

for line in fileIn:
	if line.strip():
		cLine = line.rstrip()
		#print(cLine)
		match = re.search("/([^/]+\.[^/]+)$", cLine)
		if match:
			cFileName = outFolderName + match.group(1)
			cHasExt = True
		else:
			cFileName = outFolderName + "file" + str(lineCount)
			cHasExt = False
		
		urllib.request.urlretrieve(cLine, cFileName)
		
		if not cHasExt:		#If no file extension in the url, then try and figure out the filetype via magic
			cFileType = imghdr.what(cFileName)		
			if not cFileType == None:
				try:
					os.rename(cFileName, cFileName + "." + cFileType)
				except WindowsError:
					os.remove(cFileName + "." + cFileType)
					os.rename(cFileName, cFileName + "." + cFileType)
				cFileName = cFileName + "." + cFileType
		
		fileOut.write(cFileName[len(outFolderName):] + "\n")
		lineCount += 1
		print(str(lineCount) + ": " + cFileName[len(outFolderName):])

fileIn.close()
fileOut.close()

print('Downloaded ' + str(lineCount) + ' files. List of filenames in order stored in ' + outFileName)