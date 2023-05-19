# scripts
## python scripts

Python Automation script to automate your downloads folder cleanup. <br> 
The python file "watchdog_notpkg.py" contains the code for sorting the downloads folder to different subfolders, mainly :<br>
1. Executable files <br>
2. Pdfs <br>
3. Media for images <br>
4. compressed files for zip files <br>

You can add more subfolders and make it more specific according to your preference.<br>
## naming convention
"watchdog_notpkg.py" is short for watchdog_not_package because python throws error if the filename is watchdog(that is, if you are using watchdog library in that file). You can name the file anything other than "watchdog.py".<br>

## script
"sort_files.py" - contains step by step explanation of how sorting of files is done, given a directory(target folder).<br>
"watchdog_notpkg.py" - contains entire code for checking downloads folder for new event(download), and perfoms the action required(sorting).<br> 
