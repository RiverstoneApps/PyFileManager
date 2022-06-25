import shutil
import os
import time
import subprocess

def Read():
    path=input("Enter the file path to read:")
    file=open(path, "r")
    print(file.read())
    input('Press enter to close...')
    file.close()

def Write():
    path=input("Enter the path of file to erite or create:")
    if os.path.isfile(path):
        print('Rebuilding the exsisting file')
    else:
        print('Creating the new file')
    text=input("Enter text:")
    file=open(path, "w")
    file.write(text)

def Add():
    path=input("Enter the file path:")
    text=input("Enter text:")
    file=open(path, "a")
    file.write('\n'+text)

def Delete():
    path=input("Enter the path of the file for deletion:")
    if os.path.exsists(path):
        print('File Found')
        os.remove(path)
        print('File Removed')
    else:
        print('File Not Found')

