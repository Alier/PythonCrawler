import webbrowser
import sys
import os

filename = sys.argv[1]
file = open(filename, 'r')
urls = file.readlines()
for url in urls:
    if url.find("http") >= 0:
        webbrowser.open(url)

#file.close()
#os.remove(filename)
