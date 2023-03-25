import time
import json

def play_video():
    fps = 15 # fps of terminal output

    frames = json.load(open("dataset.json",'r')) # loads dataset

    for elt in list(frames.values()): # prints each frame from dataset to the terminal
        print(elt+"\r",end="")
        time.sleep(1/fps)

play_video()