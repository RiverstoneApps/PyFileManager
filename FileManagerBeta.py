# Import Shutil(File Mover, Copier and Renamer), OS(Operating System Commands), Time(Displays the Time and Date) and Subprocess(Unknown Use)
import shutil
import os
import time
import subprocess

# Defining Functions
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

def Move():
    path1=input('Enter the source path of the file to move:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the destination path and file name')
        shutil.move(path1,path2)
        print('File Renamed')
    if mr==2:
        path2=input('Enter the path to move:')
        shutil.move(path1,path2)
        print('File Moved')

def Copy():
    path1=input('Enter the path of the file to copy or rename:')
    path2=input('Enter the path to copy to:')
    shutil.copy(path1,path2)
    print('File Copied')

def Rename():
    path=input('Enter the path of the file to rename:')
    name=input('Enter new name for file:')
    shutil.rename(path,name)

def Mkdir():
    path=input("Enter the directory name with path to make \neg. C:\\Hello\\Newdir \nWhere Newdir is new directory:")
    os.makedirs(path)
    print('Directory Created')

def Rmdir():
    
