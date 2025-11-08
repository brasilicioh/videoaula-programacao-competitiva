from moviepy import *
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

white_background = (
    ColorClip(SCREEN_SIZE, color=(255, 255, 255))
    .with_start(0)
    .with_duration(1)
)
room_background = img_clip("img/background/bedroom.png", SCREEN_SIZE, 1, 19, (0,0))

cat1 = (
    cat_clip("cat1", 2.5, 3)
    .with_effects([
        vfx.CrossFadeIn(1),
    ])
)
cat2 = cat_clip("cat2", 5.5, 4.3)
cat3 = cat_clip("cat4", 9.8, 4.2)
cat4 = cat_clip("cat2", 14, 6)

img1 = (
    img_clip("img/imgs/competitive-programming.png", (500, 500), 10.3, 5.5, (1400, 400))
    .with_effects([
        vfx.CrossFadeIn(0.4),
        vfx.CrossFadeOut(0.4),
    ])
)
img2 = (
    img_clip("img/imgs/raciociocio_logico.jpg", (420, 260), 13, 3, (50, 20))
    .with_effects([
        vfx.CrossFadeOut(0.4),
    ])
)
img3 = (
    img_clip("img/imgs/matematica.jpeg", (360, 260), 13.8, 2.2, (120, 290))
    .with_effects([
        vfx.CrossFadeOut(0.4),
    ])
)
img4 = (
    img_clip("img/imgs/sciencephile.jpg", (330, 330), 14.8, 1.2, (180, 590))
    .with_effects([
        vfx.CrossFadeOut(0.4),
    ])
)

audio = audio_clip("cena1", 3)

subtitle = subtitle_clip("cena1")

clips = [white_background, room_background, cat1, cat2, cat3, cat4, img1, 
         img2, img3, img4, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena1.mp4", fps=24)