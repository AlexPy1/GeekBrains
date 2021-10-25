import os
import shutil

folder =os.getcwd()
new_folder = os.path.join(os.getcwd(),'my_project_2/templates')

for root, dirs, files in os.walk(folder):
    for dir in dirs:
        for file in os.listdir(os.path.join(root,dir)):
            if file.endswith('.html'):
                new_root = os.path.join(root, dir)
                new_folder2 =os.path.join(new_folder,dir)
                shutil.copytree(new_root, new_folder2)
                break



