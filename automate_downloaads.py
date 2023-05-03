import sys
import os
from pathlib import Path
import glob
import shutil


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

# p3 = Path('pdf')
# p3.mkdir(exist_ok=True)
# for name in glob.glob('*.pdf'):
#     dst = 'pdf'
#     shutil.move(name, dst)
#     # print(name)
# print("All pdf files moved")

# p4 = Path('compressed files')
# p4.mkdir(exist_ok=True)
# for name in glob.glob('*.zip'):
#     dst = 'compressed files'
#     shutil.move(name, dst)
#     # print(name)
# print("All zip files moved")

# p5 = Path('images')
# p5.mkdir(exist_ok=True)
# for name in glob.glob('*.jpg'):
#     dst = 'images'
#     shutil.move(name, dst)
#     # print(name)
# print("All images files moved")

## step 4 : Get .txt files
# print("All pdf files")
# for f_name in os.listdir(cur_dir):
#      if f_name.endswith('.pdf'):
#         #  print(f_name)
#         pass

# print()

# p6 = Path('Windows Installer Package')
# p6.mkdir(exist_ok=True)
# for name in glob.glob('*.msi'):
#     dst = 'Windows Installer Package'
#     shutil.move(name, dst)
#     # print(name)
# print("All .msi files moved")

import pathlib


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
    # p.mkdir(exist_ok=True)
    print(direc_[path])
    for name in glob.glob(direc_.get(path)):
        # dst = path
        # shutil.move(name,dst)
        print(name)
    print("===============================================")
        

"""
import time 
import os
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
#new import to modify a file at the time of program run
from pathlib2 import Path


class OnMyWatch:
    
    def __init__(self):
        self.observer = Observer()
        
    
    def run(self):
        event_handler = Handler() 
        
        self.observer.schedule(event_handler, source_dir, recursive=False)
        self.observer.start()
        self.check_file_touch()
        
        try:
            '''
            adding this code of line to stop observer after 5 minutes 
            '''
            time.sleep(300)
            self.observer.stop()
            print("observer stopped")
        except: 
            self.observer.stop()
            print("observer stopped")
            
        self.observer.join()
    '''
    Added this new method (check_file_touch) as i am running this program once in a day 
    and there might be no changes at that exact time. 
    
    so this method will change the update time of the directory or create one if not exists
    so that the program can know that there are some changes made and it can run
    '''
    @staticmethod    
    def check_file_touch():
        file_name = 'file.test'
        file_directory = os.path.join(source_dir, file_name)
        file_exists = os.path.exists(file_directory)
        if file_exists:
            Path(file_directory).touch()
        else:
            os.mkdir(file_directory)

class Handler(FileSystemEventHandler):
    
    def on_any_event(self, event):
        # necessary to put the folder name as (example - destination), this will determine where the 
        # folder will be sent
        #check if we get folder
        if event.is_directory:
            for folder in os.listdir(source_dir):
                '''
                added new check statement to check if the folder is not one of the two files
                necessary to run this program
                '''
                if folder != 'folder_automation.py' and folder != 'file.test':
                    # splitting the file name and destination (example - python)
                    # it means we want to send the example folder to python destination
                    file,dest = folder.split('-')
                    file = file.strip()                 # removing the extra white space
                    dest = dest.strip().lower()         # removing extra whitespace and making lowercase
                    
                    print(f"{file} should be moved to {dest}")
                    #renaming the folder to required name after removing hyphen(-) from name
                    folder_source = os.path.join(source_dir,file)
                    os.rename(os.path.join(source_dir,folder),folder_source)
                
                    #getting the destination directory from dictionary
                    folder_destination = destination_sources[dest]
                    
                    #calling move_file method that will move the folder to required destination
                    self.move_file(file,folder_source,folder_destination)
                    
    
    @staticmethod                
    def move_file(file, source, destination):
        # same file name if the destination folder is empty
        new_name = file
        # if the destination folder is not empty
        for folder in os.listdir(destination):
            i = 1
            
            #checking if file exists
            file_exists = os.path.exists(os.path.join(destination,new_name))
            while file_exists:
                #using iterator i to give new name to folder if same name exists in destination
                new_name = new_name.strip(" "+str(i))
                i += 1
                new_name = new_name + " " + str(i)
                file_exists = os.path.exists(os.path.join(destination,new_name))
            
        #creating destination directory name as it is necessary in moving     
        new_dest_name = os.path.join(destination, new_name)
        
        #moving folder from source to destination
        '''
        added copy_function = shutil.copytree to move the folder and its complete 
        contents as previously only empty folders were moved
        '''
        shutil.move(source,new_dest_name,copy_function = shutil.copytree)
        print("moved success")
            
               
source_dir = r'C:\Users\somvi\Desktop\Automate files'

destination_sources = {"android": r'C:\Users\somvi\Desktop\android studio',
                       "python": r'C:\Users\somvi\Desktop\Python programming'}    


def check_file_touch():
    file_name = 'file.txt'
    file_directory = os.path.join(source_dir, file_name)
    file_exists = os.path.exists(file_directory)
    if file_exists:
        Path(file_directory).touch()
    else:
        os.mkdir(file_directory)
    
    
if __name__ == "__main__":
    watch = OnMyWatch()
    watch.run()
"""






