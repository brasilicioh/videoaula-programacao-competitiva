from moviepy import vfx, ColorClip
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

black_bg = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(0)
    .with_duration(1)
)
room_bg= (
    img_clip("img/background/bedroom.png", SCREEN_SIZE, 1, 19, (0,0))
)

cat1 = (
    cat_clip("cat1", 2.25, 3)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat2 = (
    cat_clip("cat2", 5.25, 3.9)
)
cat3 = (
    cat_clip("cat4", 9.15, 4.85)
)
cat4 = (
    cat_clip("cat2", 14, 6)
)

competitive_prog = (
    img_clip("img/imgs/competitive-programming.png", (500, 500), 10.2, 6.8, (1400, 460))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
logic_meme = (
    img_clip("img/imgs/raciociocio_logico.jpg", (740, 380), 12.5, 4.5, (50, 20))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
math_meme = (
    img_clip("img/imgs/matematica.jpeg", (500, 540), 13.3, 3.7, (120, 430))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
brainAI = (
    img_clip("img/imgs/sciencephile.jpg", (400, 400), 14.1, 2.9, (1300, 15))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)

audio = audio_clip("cena1", 3)

subtitle = subtitle_clip("cena1")

clips = [
    black_bg, room_bg, 
    cat1, cat2, cat3, cat4, 
    competitive_prog, logic_meme, math_meme, brainAI, 
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena1.mp4", fps=24)