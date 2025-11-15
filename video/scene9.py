from moviepy import vfx, ColorClip
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    gif_clip,
    SCREEN_SIZE
)

black_bg1 = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(0)
    .with_duration(0.5)
)
university_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0.5, 13.3)
    .with_effects([vfx.CrossFadeOut(1)])
)
gif1 = (
    gif_clip("img/imgs/cyberwave.gif", SCREEN_SIZE, 13.8, 9.8)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
wall_background = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 23.4, 8.1)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
img1 = (
    img_clip("img/imgs/windows.jpg", SCREEN_SIZE, 31, 7)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
black_bg2 = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(38)
    .with_duration(1)
)

cat1 = (
    cat_clip("cat6", 1, 4.8)
    .with_effects([vfx.CrossFadeIn(1)])
)
cat2 = (
    cat_clip("cat2", 5.8, 4.2)
)
cat3 = (
    cat_clip("cat4", 10, 3.8)
)
cat4 = (
    cat_clip("cat6", 23.4, 7.6)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
cat5 = (
    cat_clip("cat3", 31, 7, (150,"center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip("cena9", 1)

subtitle = subtitle_clip("cena9")

clips = [
    black_bg1, university_background, gif1, wall_background, 
    img1, black_bg2,
    cat1, cat2, cat3, cat4, cat5,
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena9.mp4", fps=24)