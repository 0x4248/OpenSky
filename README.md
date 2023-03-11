# 🌥 OpenSky
Open sky is a repository of open source sky images. You are free to use them for any purpose in your projects. The entire dataset is automated and generated by a script.

<img src="https://github.com/awesomelewis2007/OpenSky/blob/master/readme_animation.gif?raw=true" width="200" style="display: inline-block;">

## Prerequisites
- [make](https://www.gnu.org/software/make/)
- [python3](https://www.python.org/)
- [ffmpeg](https://ffmpeg.org/)

### Installing prerequisites on debian/ubuntu
```bash
sudo apt install make python3 ffmpeg
```

### Installing prerequisites on arch
```bash
sudo pacman -S make python ffmpeg
```

## Directory structure
- `dataset/` - contains the dataset
- `dataset/<NUMBER>` - contains an entry in the dataset
- `dataset/<NUMBER>/raw` - contains the raw images added to the dataset
- `dataset/<NUMBER>/processed` - contains the processed images added to the dataset
- `dataset/<NUMBER>/processed/1000` - contains the processed images at 1000px width and height
- `dataset/<NUMBER>/processed/bw` - contains the processed images in black and white
- `dataset/<NUMBER>/processed/bw_1000` - contains the processed images in black and white at 1000px width and height
- `panoramas/` - contains panoramas of the sky

## Usage ideas
There a lot of things you can do with this dataset. Here are some ideas:
- Use the images to train a neural network
- Use the images to train a GAN
- Use the images to predict the weather
- Use the images to calculate the cloud cover
- Use the images to figure out cloud types

## How to add to the dataset
You can use github codespaces to add to the dataset.

1. Fork the repository
2. Read the [contributing guidelines](CONTRIBUTING.md)
2. install make and ffmpeg on your system `sudo apt install make ffmpeg`
3. run `make` in the root directory of the repository
4. Follow the prompts
5. Open a pull request
