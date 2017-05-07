import os

def rename_files():

    #1 Get file Names
    file_list = os.listdir("C:\Users\Production\Desktop\example")

    #2 Rename Files
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
