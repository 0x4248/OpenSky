# Open sky add tool
# A repository of open source sky images.
# Github: https://www.github.com/lewisevans2007/opensky
# Licence: Unlicense

import os

def count_images():
    dataset_dir = "dataset"
    count = 0
    for subdir in os.listdir(dataset_dir):
        subdir_path = os.path.join(dataset_dir, subdir)
        if os.path.isdir(subdir_path):
            raw_dir = os.path.join(subdir_path, "raw")
            if os.path.isdir(raw_dir):
                for filename in os.listdir(raw_dir):
                    if os.path.isfile(os.path.join(raw_dir, filename)):
                        count += 1
    return count
                


if __name__ == "__main__":
    count = 0
    for file in os.listdir("dataset"):
        if os.path.isdir("dataset/"+file):
            count += 1
    with open("README.md", "r") as f:
        readme = f.read()
    lines = readme.split("\n")
    lines[3] = "There are `"+str(count)+"` entries in this dataset."
    lines[5] = "There are `"+str(count_images())+"` images in this dataset."
    with open("README.md", "w") as f:
        f.write("\n".join(lines))