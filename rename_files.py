import os
import re

def rename_files():
    #Change currentDir to have the program rename all files within it
    currentDir = r"C:\Users\Production\Desktop\example"
    #1 Get file Names
    file_list = os.listdir(currentDir)
    saved_path = os.getcwd()

    #2 Rename Files
    os.chdir(currentDir)
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + re.sub(r'\d+', '', file_name))
        os.rename(file_name, re.sub(r'\d+', '', file_name))

rename_files()

