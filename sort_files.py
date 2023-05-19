import os
from pathlib import Path
import glob
import shutil

## step 1 : change directory
os.chdir('/path/to/Downloads')
cur_dir = os.getcwd()

## step 2 : list all the files in the directory
for entry in os.listdir(cur_dir):
    if os.path.isfile(os.path.join(cur_dir, entry)):
        print(entry)

## step 3 : create new directory/folder
p = Path('example_directory')
p.mkdir(exist_ok=True) #exist_ok checks if dir already exits

## step 4 : move all(*) the files that ends with .txt 
for name in glob.glob('*.txt'):
    destination = 'example_directory'
    shutil.move(name, destination)
    # print(name)
print("All .exe files moved to {}".format(destination))


## step 5: combining above steps
os.chdir('/path/to/downloads')
cur_dir = os.getcwd()

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

        








