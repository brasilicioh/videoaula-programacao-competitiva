from moviepy import vfx 
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

background = (
    img_clip("img/background/school.png", SCREEN_SIZE,
             0, 89.57)
)

cat1 = (
    cat_clip("cat2", 0, 15)
)
cat2 = (
    cat_clip("cat3", 15, 47)
)
cat3 = (
    cat_clip("cat4", 62, 26)
)
cat4 = (
    cat_clip("cat6", 88, 1.57)
)

sbc_logo = (
    img_clip("img/logo/sbc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             2, 3.5, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

fundamental = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             7, 1.7, (1244, "center"))
    .with_effects([vfx.Crop(x2=480), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
ens_medio = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             8.2, 1.8, (1244, "center"))
    .with_effects([vfx.Crop(x1=480), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

obi_logo = (
    img_clip("img/logo/obi.png", (360, 600),
             9.5, 5.25, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

chorando = (
    img_clip("img/imgs/chorando.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             17.2, 2.8, (100, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

programacao = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             18, 2, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

iniciacao = (
    img_clip("img/imgs/prova_iniciacao.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             35, 10, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

ioi_logo = (
    img_clip("img/logo/ioi.jpg", (SCREEN_SIZE[0]*0.35, SCREEN_SIZE[1]*0.35),
             76, 7, (1219, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip("cena7")

subtitle = subtitle_clip("cena7")

clips = [
    background,
    cat1, cat2, cat3, cat4,
    sbc_logo, obi_logo, ioi_logo, fundamental, ens_medio,
    chorando, programacao, iniciacao,
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena7.mp4", fps=24)