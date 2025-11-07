from moviepy.editor import *
import moviepy.config as conf
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.video.tools.subtitles import SubtitlesClip

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

# INICIALIZAÇÃO DE IMAGENS

# fundo branco pós introdução de começo - pode mudar
white_background = ColorClip(SCREEN_SIZE, color=(255, 255, 255)) \
    .set_start(0) \
    .set_duration(1)

# fundo de quarto: primeiro background
room_background = ImageClip("img/background/bedroom.png") \
    .resize(SCREEN_SIZE) \
    .set_start(1) \
    .set_duration(19)

# gatos que aparecem na cena
cat1 = cat_clip("cat1", 2.5, 4).fadein(1)
cat2 = cat_clip("cat2", 6.5, 3.5)
cat3 = cat_clip("cat4", 10, 4)
cat4 = cat_clip("cat2", 14, 6)

# imagens utilizadas
img1 = ImageClip("img/imgs/competitive-programming.png") \
    .resize((500, 500)) \
    .set_start(10.3) \
    .set_duration(5.5) \
    .set_position((1400, 400)) \
    .crossfadein(0.4).crossfadeout(0.4)

img2 = ImageClip("img/imgs/raciociocio_logico.jpg") \
    .resize((420, 260)) \
    .set_start(12.5) \
    .set_duration(3.5) \
    .set_position((50, 20)) \
    .crossfadeout(0.4)

img3 = ImageClip("img/imgs/matematica.jpeg") \
    .resize((360, 260)) \
    .set_start(13.8) \
    .set_duration(2.2) \
    .set_position((120, 290)) \
    .crossfadeout(0.4)

img4 = ImageClip("img/imgs/sciencephile.jpg") \
    .resize((330, 330)) \
    .set_start(14.8) \
    .set_duration(1.2) \
    .set_position((120, 590)) \
    .crossfadeout(0.4)

# audio da cena
audio_cena1 = AudioFileClip("sound/cena1.mp3") \
    .set_start(3)

audio_final = CompositeAudioClip([audio_cena1])

# gerador de legendas
generator = lambda txt: TextClip(
    txt,
    font="Arial-Bold",
    fontsize=48,
    color="white",
    stroke_color="black",
    stroke_width=2,
    method="caption",
    size=(SCREEN_SIZE[0] - 200, None)
)

subtitle = SubtitlesClip("texto/cena1.srt", generator) \
    .set_position(("center", SCREEN_SIZE[1] - 130))

# todos clips
clips = [white_background, room_background, cat1, cat2, cat3, cat4, img1, img2, img3, img4, subtitle]

# criacao e exportacao de video
video = CompositeVideoClip(clips, size=SCREEN_SIZE) \
    .set_duration(20) \
    .set_audio(audio_final)

video.write_videofile("clips/cena1.mp4", fps=24)