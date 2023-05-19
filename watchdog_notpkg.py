import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import shutil 
import os
import glob
import shutil

## The Watcher object initializes and manages monitoring the specified folder (and its subfolders). 
class Watcher:

    def __init__(self, directory, handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")

## The Handler object applies your code to determine what to do in response to events. 
## under created_file() you can modify the code according to your application
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        object.__init__(self)

    def created_file(self, event):
        ## check the type of event that's taking place while watchdog is running,
        ## we only need event_type "created" for checking download
        if event.event_type == "created":
            
            ## check 'sort_files.py' for detailed explanation
            direc_ = {
                        "excecutables"             :"*.exe",
                        "pdf"                      :"*.pdf",
                        "compressed files"         :"*.zip",
                        "media"                    :"*.jpg",
                        "Windows Installer Package":"*.msi"
                        }

            for path in direc_.keys():
                try:
                
                    p = Path(path)
                    p.mkdir(exist_ok=True)
                    print(direc_[path])
                    for name in glob.glob(direc_.get(path)):
                        dst = path
                        shutil.move(name,dst)
                        print(name)
                    print("------------------")
                
                except :
                    print("Error ")
                    
    
    def on_created(self, event):
        self.created_file(event)
                


if __name__=="__main__":

    ## enter the path to your downloads correctly here
    os.chdir('/path/to/Downloads')
    cur_dir = os.getcwd()
    w = Watcher(cur_dir, MyHandler())
    w.run()