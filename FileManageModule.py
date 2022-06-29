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
    path=input("Enter the path of file to write or create:")
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
        print('Error: File Not Found')

def Dirlist():
    path=input("Enter the Directory path to display:")
    sortlist=sorted(os.listdir(path))
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+1

def Check():
    fp=int(input('Check existence of \n1.File \n2.Directory\n'))
    if fp==1:
        path=input("Enter the file path:")
        
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
    path2=input('Enter the path to move to:')
    shutil.move(path1,path2)
    print('File Moved')

def Copy():
    path1=input('***********************Warning! Copying A File to the Same Directory With A Different Name Will Only Rename the File*************************/nEnter the path of the file to copy:')
    path2=input('Enter the path to copy to:')
    shutil.copy(path1,path2)
    print('File Copied')

def Rename():
    
    path=input('Enter directory path of file to rename:\nAlso, please end the directory path with a slash.')
    cname=input('Enter current name of file to rename:')
    nname=input('Enter new file name:')
    shutil.move(path+cname,path+nname)

def Mkdir():
    path=input("Enter the directory name with path to make \neg. C:\\Hello\\Newdir \nWhere Newdir is new directory:")
    os.makedirs(path)
    print('Directory Created')

def Rmdir():
    path=input('Enter path of Directory to delete:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()

def OpenFile():
    path=input('Enter the path of program:')
    try:
        os.startfile(path)
    except:
        print('Error: File Not Found')
