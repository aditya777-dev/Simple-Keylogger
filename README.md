# Simple-Keylogger-Spyware
A python code for a simple keylogger application that records all key strokes while application is running and logs them in a logfile.

# Download simple-keylogger.py file
executing simple-keylogger.py will start the recording and updating all recorded keys and mouse clicks in keylog.txt file in the same folder

# To convert this file into an executable
1. install PyInstaller

> ' pip install pyinstaller==5.13.2 '

> use this specific version to avoid error: win32ctypes.pywin32.pywintypes.error: (225, 'BeginUpdateResourceW', 'Operation did not complete successfully because the file contains a virus or potentially unwanted software.')

2. use this command to convert python file to an executable

> ' python -m PyInstaller --noconsole --onefile simple-keylogger.py '

> ' --noconsole ' supresses console output to maintain stealth of the application

> ' --onefile ' creates a single executable file of the code rather than an entire folder; this might raise an alert for windows defender and it will not allow the execution of the file
 
> this process may take some time

> after completion, the application file (simple-keylogger.exe) will be available in 'dist' folder

3. to execute application on startup (hidden and running in background)

> create a shortcut of the application

> press 'win+r', type 'shell:startup', this opens startup folder

> move shortcut to the startup folder

> now when device is powered on, the keylogger will be active and hidden in background

> all keystrokes will be recorded in 'keylog.txt' file in 'dist' folder 

4. to stop keylogger

> press 'ctrl + shift + esc', to open task manager

> find keylogger process, select and end task
