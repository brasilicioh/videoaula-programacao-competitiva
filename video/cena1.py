from moviepy.editor import *
import moviepy.config as conf
from moviepy.audio.AudioClip import CompositeAudioClip

# necessário para utilizar legendas; confirme se o caminho do computador é esse
conf.change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.2-Q16-HDRI/magick.exe"})

TAMANHO_TELA = (1920, 1080)

white_background = ColorClip(TAMANHO_TELA, color=(255, 255, 255)) \
    .set_start(0) \
    .set_duration(2)

room_background = ImageClip("img/background/bedroom.png") \
    .resize(TAMANHO_TELA) \
    .set_start(2) \
    .set_duration(16)

cat1 = ImageClip("img/character/cat1.png") \
    .resize(height=TAMANHO_TELA[1]*0.45) \
    .set_start(3) \
    .set_duration(15) \
    .set_position(("center", "center"))

audio_cena1 = AudioFileClip("sound/cena1.mp3") \
    .set_start(3) \
    .set_duration(15)

audio_final = CompositeAudioClip([audio_cena1])

video = CompositeVideoClip([white_background, room_background, cat1], size=TAMANHO_TELA) \
    .set_duration(18) \
    .set_audio(audio_final)

video.write_videofile("clips/cena1.mp4", fps=24)