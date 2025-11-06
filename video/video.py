from moviepy.editor import *
import moviepy.config as conf

conf.change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.2-Q16-HDRI/magick.exe"})

TAMANHO_TELA = (1920, 1080)


# fundo branco por 2s
whiteBg = ColorClip(TAMANHO_TELA, color=(255, 255, 255)) \
    .set_duration(2) \
    .set_start(0)

# background1 de 2 até 18
firtsBg = ImageClip("img/background/bedroom.png") \
    .resize(TAMANHO_TELA) \
    .set_start(2) \
    .set_duration(16)

# personagem1 de 3 até 18
char1 = ImageClip("img/character/cat1.png") \
    .resize(height=TAMANHO_TELA[1]*0.45) \
    .set_position(("center", "bottom")) \
    .set_start(3) \
    .set_duration(15) \
    .set_position(("center", "center"))

audio_clip = AudioFileClip("sound/cena1.mp3").set_start(3)

video = CompositeVideoClip([whiteBg, firtsBg, char1], size=TAMANHO_TELA).set_duration(18).set_audio(audio_clip)

video.write_videofile("video.mp4", fps=24)