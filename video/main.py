import os
from moviepy import VideoFileClip, concatenate_videoclips

arquivos = os.listdir("clips/")

clips = [VideoFileClip(f"clips/cena{i}.mp4") for i in range(1, len(arquivos)+1)]

clips.insert(0, VideoFileClip("clips/start.mov"))
clips.append(VideoFileClip("clips/end.mov"))

video_final = concatenate_videoclips(clips, method="compose")

video_final.write_videofile("videoaula.mp4", fps=24)
