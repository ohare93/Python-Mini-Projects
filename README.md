# Python-Mini-Projects

### General Setup
1. Make sure [Python is installed](https://www.python.org/downloads/)
    - If you later get the error "Python is not recognised as a command" when you try and execute a project, you need to add your Python install to your Path list (follow part 3 of [this guide](https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File))

2. Download your desired project somewhere onto your computer
3. Open the cmd line or powershell to the folder
4. Run your desired command, explained for each mini project below.


## Test Playlist Generator
Generates a playlist file for Visual Studio, from a txt file containing each test's full path on a separate line.

> python TestPlaylistGenerator.py [<Filename.txt>]

Optional parameter of the filename, otherwise the **default is "tests.txt"**. A ".playlist" file will be generated using the input file name and the current date.

## Mass Image Downloader
Downloads files from a list of links in a txt file. Also attempts to determine the type of file, first checking if it is in the url, then checking via [Python Magic](https://github.com/ahupp/python-magic)

> python MassImageDownloader [<Filename.txt>]

Optional parameter of the filename, otherwise the **default is "images.txt"**. Puts all images into a folder, of the same name as the input file (plus the date). If the folder already exists, it deletes it, then makes it anew.

A list of each image downloaded, in order, is available in the "_Log.txt" file, in each folder.
