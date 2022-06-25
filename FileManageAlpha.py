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

def Dirlist():
    path=input("Enter the Directory path to display:")
    sortlist=sorted(os.listdir(path))
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+1

def Check():
    fp=int(input('Check exsistence of \n1.File \n2.Directory\n'))
    if fp==1:
        path=input("Enter the file path:")
        os.path.isfile(path)

    if os.path.isfile(path)==True:
        print('File Found')
    else:
        print('File Not Found')
    if fp==2:
       path=input("Enter the Directory path:")
       os.path.isdir(path)
       if os.path.isdir(path)==False:
           print('Directory Found')
       else:
           print('Directory Not Found')

#Still need to define Move(Move()), Copy(Copy()), MakeDirectory(Mkdir()), RemoveDirectory(RmDir()) and OpenFile(Openfile())
#Then need to add code to list options and run them accordingly.
