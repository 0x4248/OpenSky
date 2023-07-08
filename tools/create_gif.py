# Open sky readme animation tool
# A repository of open source sky images.
# Github: https://www.github.com/lewisevans2007/opensky
# Licence: Unlicense

import os
import random

PATH = "dataset/"

def create_gif():
    os.system("ffmpeg -y -framerate 2 -i gif_tmp/%*.jpg  readme_animation.gif")

if __name__ == "__main__":
    picked = []
    for i in range(5):
        while True:
            choice = random.choice(os.listdir(PATH))
            if choice not in picked:
                break
        picked.append(choice)
    os.mkdir("gif_tmp")
    for i in range(len(picked)):
        os.system("cp "+PATH+picked[i]+"/processed/1000/"+"* gif_tmp")
        for i in range(len(os.listdir("gif_tmp"))):
            os.rename("gif_tmp/"+os.listdir("gif_tmp")[i], "gif_tmp/"+str(random.randint(0, 100000000))+".jpg")
    create_gif()
