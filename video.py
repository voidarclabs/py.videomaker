import os

def create(time, asprat,  bg, size, fontcolor, text, output):
    os.system('ffmpeg -f lavfi -i color=size=' + asprat + ':duration=' + time + ':rate=25:color=' + bg + ' -vf "drawtext=fontfile=font.ttf:fontsize=' + size + ':fontcolor=' + fontcolor + ':x=(w-text_w)/2:y=(h-text_h)/2:text=' + text + '" ' + output + '.mp4')