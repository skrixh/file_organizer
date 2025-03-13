import os
import shutil

#list files in a folder
folder_path = "/Users/user/Downloads" #current directory
files = os.listdir(folder_path)

print("Files in the current directory:")

#Identify file extensions
for file in files:
    if "/Users/user/Downloads" in file: #To avoid folders   
        extension = file.split(".")[-1]
        print(f"File: {file},Extension: {extension}")
#splits the filename buy . and gets the last part(the extension)
#This code will print the files in the current directory and their extensions.

#create folders based on extensions
folder_path = "/Users/user/Downloads"

for file in os.listdir(folder_path):
    if "." in file:
        extension = file.split(".")[-1]
        folder_name = os.path.join(folder_path, extension.upper())

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

#Move files to their folders
for file in os.listdir(folder_path):
    if "." in file:
        extension = file.split(".")[-1]
        folder_name = os.path.join(folder_path, extension.upper())

        #move the file
        shutil.move(os.path.join(folder_path,file),os.path.join(folder_name, file))
        print(f"Moved {file} to {folder_name}/")