from pynput.keyboard import Key, Controller
import time

message = "your text"
keyboard = Controller()

time.sleep(5)

for num in range(100):
    for text in message:
        keyboard.press(text)
        keyboard.release(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)