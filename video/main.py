import os
from moviepy import VideoFileClip, concatenate_videoclips

arquivos = os.listdir("clips/")

clips = []

for i in range(0, len(arquivos)):
    try:
        clips.append(VideoFileClip(f"clips/cena{i}.mp4"))
    except:
        clips.append(VideoFileClip(f"clips/cena{i}.mov"))

video_final = concatenate_videoclips(clips, method="compose")

video_final.write_videofile("videoaula.mp4", fps=24)
