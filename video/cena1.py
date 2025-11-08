from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import ColorClip, AudioFileClip, TextClip, CompositeVideoClip, CompositeAudioClip
from clips import cat_clip, img_clip

# necessário para utilizar legendas; confirme se o caminho do computador é esse
import moviepy.config as conf
conf.change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.2-Q16-HDRI/magick.exe"})

# tamanho constante de todas telas da videoaula
SCREEN_SIZE = (1920, 1080)

# INICIALIZAÇÃO DE IMAGENS

# fundo branco pós introdução de começo - pode mudar
white_background = ColorClip(SCREEN_SIZE, color=(255, 255, 255)) \
    .set_start(0) \
    .set_duration(1)

# fundo de quarto: primeiro background
room_background = img_clip("img/background/bedroom.png", SCREEN_SIZE, 1, 19, (0,0))

# gatos que aparecem na cena
cat1 = cat_clip("cat1", 2.5, 3).crossfadein(1)
cat2 = cat_clip("cat2", 5.5, 4.3)
cat3 = cat_clip("cat4", 9.8, 4.2)
cat4 = cat_clip("cat2", 14, 6)

# imagens utilizadas
img1 = img_clip("img/imgs/competitive-programming.png", (500, 500), 10.3, 5.5, (1400, 400)) \
    .crossfadein(0.4).crossfadeout(0.4)
img2 = img_clip("img/imgs/raciociocio_logico.jpg", (420, 260), 13, 3, (50, 20)) \
    .crossfadeout(0.4)
img3 = img_clip("img/imgs/matematica.jpeg", (360, 260), 13.8, 2.2, (120, 290)) \
    .crossfadeout(0.4)
img4 = img_clip("img/imgs/sciencephile.jpg", (330, 330), 14.8, 1.2, (120, 590)) \
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