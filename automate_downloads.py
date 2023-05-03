import sys
import os
from pathlib import Path
import glob
import shutil
import pathlib

## step 1 : change directory
# os.chdir('/users/SANDRA/Downloads')
# cur_dir = os.getcwd()

## step 2 : list all the files in the directory
# for entry in os.listdir(cur_dir):
#     if os.path.isfile(os.path.join(cur_dir, entry)):
#         print(entry)

## step 3 : create new directory/folder
# p = Path('example_directory')
# p.mkdir(exist_ok=True)

# p2 = Path('excecutables')
# p2.mkdir(exist_ok=True)
# for name in glob.glob('*.exe'):
#     dst = 'excecutables'
#     shutil.move(name, dst)
#     # print(name)
# print("All .exe files moved")

## step 4 : Get .txt files
# print("All pdf files")
# for f_name in os.listdir(cur_dir):
#      if f_name.endswith('.pdf'):
#         #  print(f_name)
#         pass


os.chdir('/users/SANDRA/Downloads')
cur_dir = os.getcwd()
# dir = pathlib.Path(cur_dir)


direc_ = {"excecutables"             :"*.exe",
          "pdf"                      :"*.pdf",
          "compressed files"         :"*.zip",
          "media"                    :"*.jpg",
          "Windows Installer Package":"*.msi"
        }

for path in direc_.keys():
    p = Path(path)
    p.mkdir(exist_ok=True)
    print(direc_[path])
    for name in glob.glob(direc_.get(path)):
        dst = path
        shutil.move(name,dst)
        print(name)
    print("===============================================")
        








