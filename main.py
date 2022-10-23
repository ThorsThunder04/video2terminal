from PIL import Image
from tqdm import tqdm
import json
import time
import os

def colored(r, g, b, text): # allows for colored text in the terminal
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def make_dataset():
    
    framerate = 15 # desired fps of the dataset
    pixelOffset = 20 # add pixel to dataset every X pixels.



    os.makedirs("./frames", exist_ok=True)
    os.system(f"ffmpeg -i ./input.mp4 -r {framerate}/1 ./frames/%08d.png")

    # holds frames that will then be dumped to the dataset.json
    frames = {}

    for i in tqdm(range(1,len(os.listdir("./frames"))+1)):

        with Image.open(f"./frames/{i:08}.png") as img:
            frames[i] = "" # so we can concatinate strings to current empty dataset frame

            # iterates pixels of current frame
            for y in range(0,img.height, pixelOffset):
                for x in range(0,img.width, pixelOffset):

                    currpix = img.getpixel((x,y)) # rgb value of pixel

                    frames[i] += colored(*currpix, "██") # adds colored text to dataset frame

                frames[i] += "\n" # new line when we change y coordinate
            frames[i]

    with open("dataset.json", "w") as f:
        json.dump(frames,f,indent=4)

def play_video():
    fps = 15 # fps of terminal output

    frames = json.load(open("dataset.json",'r')) # loads dataset

    for elt in list(frames.values()): # prints each frame from dataset to the terminal
        print(elt+"\r",end="")
        time.sleep(1/fps)

make_dataset()
input()
play_video()
    



