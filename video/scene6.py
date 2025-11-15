from moviepy import vfx 
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

# t is a value from 0-1
def ease_inout(t: float) -> float:
    return 2 * t * t if t < 0.5 else 1 - (-2 * t + 2)**2 / 2


room_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 56.45)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
school_bg = (
    img_clip("img/background/school.png", SCREEN_SIZE, 56.4, 0.9)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

cat1 = (
    cat_clip("cat4", 0, 8.7)
)

cat2 = (
    cat_clip("cat3", 8.7, 1.8)
)

cat3 = (
    cat_clip("cat3_lado", 10.5, 1.25)
)

cat4 = (
    cat_clip("cat3", 11.75, 1.7) # 25
)
cat5 = (
    cat_clip("cat5", 13.45, 18.05) # until 1.3700
    .with_position(lambda t: (
        # this makes sense pls, don't mess with it
        max(SCREEN_SIZE[0]/2 - 300 - 10 - 640*ease_inout(min(t/2, 1)), 10),
        "center"))
)
cat6 = (
    cat_clip("cat2", 31.5, 24.95)
    .with_position(lambda t: (
        # this makes sense pls, don't mess with it
        (SCREEN_SIZE[0]/2 - 300 - 10) - (max(SCREEN_SIZE[0]/2 - 300 - 10 - 640*ease_inout(min(t/2, 1)), 430)),
        "center"))
    .with_effects([vfx.CrossFadeOut(0.5)])
)

mundo = (
    img_clip("img/imgs/mundo.jpg", (SCREEN_SIZE[0]*0.6, SCREEN_SIZE[1]*0.6),
             5, 3, ("center", "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.25)])
)

sbc_competition = (
    img_clip("img/imgs/sbc_ginasio.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             15.25, 8.25, (SCREEN_SIZE[0]*3/8, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)

maratona_logo = (
    img_clip("img/logo/maratona_sbc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             9, 3.7, (1144, 20))
)
icpc_logo = (
    img_clip("img/logo/icpc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             10.5, 2.2, (200, 20))
)
obi_logo = (
    img_clip("img/logo/obi.png", (SCREEN_SIZE[0]*0.2, SCREEN_SIZE[1]*0.3),
             11, 1.7, (200, 580))
)
ioi_logo = (
    img_clip("img/logo/ioi.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             11.8, 0.9, (1144, 580))
)

# equipe de três pessoas
# Computador.jpg
# computador.jpg
# Hacker.jpeg

equipe_pessoa1 = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2 - SCREEN_SIZE[0]*0.285/2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.MirrorX(),
                   vfx.Crop(0, 0, SCREEN_SIZE[0]*0.285/2, SCREEN_SIZE[1])])
)
equipe_pessoa2 = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.MirrorX(),
                   vfx.Crop(0, 0, SCREEN_SIZE[0]*0.285/2, SCREEN_SIZE[1])])
)
equipe_pessoa3 = (
    img_clip("img/imgs/Hacker.jpeg", (SCREEN_SIZE[0]*0.2, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2 + SCREEN_SIZE[0]*0.285/2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)

ballon1 = (
    img_clip("img/imgs/balao1.png", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1] * 0.8),
             33, 4, (SCREEN_SIZE[0]*(1/2), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
# Images cross fade into eachother
ballon2 = (
    img_clip("img/imgs/balao2.png", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1] * 0.8),
             36, 2.5, (SCREEN_SIZE[0]*(1/2), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

# Nas competiçoes físicas...

sbc_pessoas = (
    img_clip("img/imgs/sbc_pessoas.jpg", ((SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1] * 0.5)),
             39.2, 5.8, (SCREEN_SIZE[0]*(1/2 - 1/32), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

icpc_competition = (
    img_clip("img/imgs/icpc_teams.jpg", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             46, 10.45, (SCREEN_SIZE[0]*(1/2 - 1/32), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip("cena6")

subtitle = subtitle_clip("cena6")

clips = [
    room_background, school_bg,
    cat1, cat2, cat3, cat4, cat5, cat6,
    mundo, sbc_competition, maratona_logo, icpc_logo, 
    obi_logo, ioi_logo, equipe_pessoa1, equipe_pessoa2, 
    equipe_pessoa3, sbc_pessoas, icpc_competition, 
    ballon1, ballon2,
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena6.mp4", fps=24)