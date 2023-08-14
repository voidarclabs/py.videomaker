import video, os

num = int(input('number of videos: '))
len = str(input('length of videos: '))
color = str(input('color of video: '))
colortext = str(input('color of text: '))
aspectratio = str(input('aspect ratio: '))
textsize = str(input('size of text: '))
os.chdir('output')

for i in range(num):
    video.create(len, aspectratio, color, textsize, colortext, str(i + 1), str(i + 1) + 'video')