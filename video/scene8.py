from moviepy import vfx, ColorClip
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    gif_clip,
    video_clip,
    SCREEN_SIZE
)

wall_background = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 0, 18)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
interval1_bg = (
    img_clip("img/questions/distinto/description1.png", SCREEN_SIZE, 18, 10.76)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
interval2_bg = (
    img_clip("img/questions/distinto/description2.png", (SCREEN_SIZE[0], SCREEN_SIZE[1]*0.5), 28.26, 3.24, ("center", "top"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
interval3_bg = (
    img_clip("img/questions/distinto/description3.png", (SCREEN_SIZE[0], SCREEN_SIZE[1]*0.5), 28.26, 3.24, ("center", "bottom"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
room_bg = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 31, 17.03)
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(0.5)])
)
matrix = (
    gif_clip("img/imgs/matrix.gif", SCREEN_SIZE, 48, 8.1)
    .with_effects([vfx.CrossFadeOut(0.5)])
)


cat1 = (
    cat_clip("cat4", 0, 3.2)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat2 = (
    cat_clip("cat3", 3.2, 4.35)
)
cat3 = (
    cat_clip("cat5", 7.55, 5.75)
)
cat4 = (
    cat_clip("cat1", 13.3, 4.7)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat5 = (
    cat_clip("cat2", 31, 6.6)
    .with_effects([vfx.CrossFadeIn(1)])
)
cat6 = (
    cat_clip("cat3", 37.6, 5.6)
)
cat7 = (
    cat_clip("cat4", 43.2, 4.83)
    .with_effects([vfx.CrossFadeOut(0.5)])
)

img1 = (
    img_clip("img/questions/distinto/c.png", (1000, 1000), 48.2, 1.2)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
img2 = (
    img_clip("img/questions/distinto/cpp.png", (1000, 1000), 49.4, 1.7)
)
img3 = (
    img_clip("img/questions/distinto/js.png", (1000, 1000), 51.1, 1.5)
)
img4 = (
    img_clip("img/questions/distinto/py.png", (1000, 1000), 52.6, 1.5)
)
img5 = (
    img_clip("img/questions/distinto/rs.png", (1000, 1000), 54.1, 2)
    .with_effects([vfx.CrossFadeOut(0.5)])
)

black_bg = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(56)
    .with_duration(0.5)
)

audio = audio_clip([
    ("cena8-1", 0),
    ("cena8-2", 31.53),
])

subtitle = subtitle_clip("cena8")

clips = [wall_background, interval1_bg, interval2_bg, interval3_bg, 
         room_bg, matrix, cat1, cat2, cat3, cat4, cat5, 
         cat6, cat7, img1, img2, img3, img4, img5, black_bg, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena8.mp4", fps=24)