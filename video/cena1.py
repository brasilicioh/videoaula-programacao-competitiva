from moviepy.editor import *
import moviepy.config as conf
from moviepy.audio.AudioClip import CompositeAudioClip

# método padrão para inicializar gato
def cat_clip(name: str, start: float, duration: float) -> ImageClip:
    cat: ImageClip = ImageClip(f"img/character/{name}.png") \
        .set_start(start) \
        .set_duration(duration) \
        .set_position(("center", "center"))
    return cat

# necessário para utilizar legendas; confirme se o caminho do computador é esse
conf.change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.2-Q16-HDRI/magick.exe"})

# tamanho constante de todas telas da videoaula
SCREEN_SIZE = (1920, 1080)

# fundo branco pós introdução de começo - pode mudar
white_background = ColorClip(SCREEN_SIZE, color=(255, 255, 255)) \
    .set_start(0) \
    .set_duration(1)

room_background = ImageClip("img/background/bedroom.png") \
    .resize(SCREEN_SIZE) \
    .set_start(1) \
    .set_duration(17)

cat1 = cat_clip("cat1", 2.5, 4).fadein(1)
cat2 = cat_clip("cat2", 6.5, 3.5)
cat3 = cat_clip("cat4", 10, 4)
cat4 = cat_clip("cat2", 14, 4)

img1 = ImageClip("img/imgs/competitive-programming.png") \
    .resize((650, 650)) \
    .set_start(11) \
    .set_duration(4) \
    .set_position((SCREEN_SIZE[0] - 650 - 80, "center")) \
    .crossfadein(0.4).crossfadeout(0.4)

# add img2, 3, 4 na hora que ele fala (problemas lógicos, matemáticos e computacionais)

clips = [white_background, room_background, cat1, cat2, cat3, cat4, img1]

audio_cena1 = AudioFileClip("sound/cena1.mp3") \
    .set_start(3) \
    .set_duration(15)

audio_final = CompositeAudioClip([audio_cena1])

video = CompositeVideoClip(clips, size=SCREEN_SIZE) \
    .set_duration(18) \
    .set_audio(audio_final)

video.write_videofile("clips/cena1.mp4", fps=24)