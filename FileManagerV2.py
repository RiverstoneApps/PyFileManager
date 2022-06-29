# Import Shutil(File Mover, Copier and Renamer), OS(Operating System Commands) and Subprocess(Unknown Use)
import FileManageModule
import os

os.system('clear')
os.system('cls')

# Defining Functions

def Menu():
    # Clears the screen, and gives the user their options on what to do
    os.system('clear')
    os.system('cls')
    run=1
    while(run==1):
        os.system('clear')
        os.system('cls')
        print('\n>>>>>>>>>>>File Manager Version 2.7<<<<<<<<<<\n')
        print('\nChoose what to do with files: \n')
        dec=int(input('''1.Read a file
2.Write to a file
3.Add to a file
4.Delete a file
5.List files in a directory
6.Check file existence
7.Move a file
8.Copy a file
9.Rename a file
10.Create a directory
11.Delete a directory
12.Open a program
13.Exit

    '''))
        # Determines what will happen based on what the user inputed
        if dec==1:
            FileManageModule.Read()
        if dec==2:
            FileManageModule.Write()
        if dec==3:
            FileManageModule.Add()
        if dec==4:
            FileManageModule.Delete()
        if dec==5:
            FileManageModule.Dirlist()
        if dec==6:
            FileManageModule.Check()
        if dec==7:
            FileManageModule.Move()
        if dec==8:
            FileManageModule.Copy()
        if dec==9:
            FileManageModule.Rename()
        if dec==10:
            FileManageModule.Mkdir()
        if dec==11:
            FileManageModule.Rmdir()
        if dec==12:
            FileManageModule.OpenFile()
        if dec==13:
            exit()
        else:
            print('Error: Unknown Request')
        run=int(input("1.Return to menu\n2.Exit \n"))
        if run==2:
            exit()

Menu()
