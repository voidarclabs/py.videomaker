# PYTHON FFMPEG VIDEOMAKER

This is a python videomaker that uses ffmpeg to mass create variable 
length videos that have a custom background color and text. To use this, 
you will obviously need to install `ffmpeg` systemwide, and python.

## Config / Usage

To run the video maker, open the [videomaker.py](https://github.com/voidarclabs/py.videomaker/blob/main/videomaker.py)
file and fill out the prompts as follows:
```
number of videos: should be a number
length of videos: in seconds (5 for 5 seconds, 60 for 1 min, etc.)
color of video: standard color or hex code
color of text: standard color or hex code
aspect ratio: number x number (1920x1080, *x*)(text will always be centered)
size of text: number (300 == 300px height compared to aspect ratio)
```
To change font, replace the font.ttf file with desired font file (default is 
times new roman)

As always, video.create can be used as a function in other files