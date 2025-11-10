from moviepy import vfx, ColorClip
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

room_bg = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 16.5)
)

cat1 = (
    cat_clip("cat2", 0, 8)
    .with_effects([vfx.CrossFadeOut(0.5)])
)

img1 = (
    img_clip("img/imgs/meme_helloworld.jpg", (600, 600), 2.5, 5.1, (90, 100))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

cat2 = (
    cat_clip("cat3", 8, 8.4, ("left", "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

img2 = (
    img_clip("img/imgs/io.webp", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1]*0.4), 8, 8.4, ("center", "center"))
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(0.5)])
)

leetcode1_bg = (
    img_clip("img/imgs/leetcode1.png", SCREEN_SIZE, 16.5, 2)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

leetcode2_bg = img_clip("img/imgs/leetcode2.png", SCREEN_SIZE, 18.5, 2.8)

black_bg = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(20.3)
    .with_duration(26.1)
)

img3 = (
    img_clip("img/imgs/sciencephile.jpg", (530, 530), 20.3, 5.8, (400, 200))
    .with_effects([vfx.CrossFadeIn(0.5)])
)

audio = audio_clip("cena3")

subtitle = subtitle_clip("cena3")

clips = [room_bg, leetcode1_bg, leetcode2_bg, black_bg, img3, cat1, cat2, img1, img2, subtitle]

video = video_clip(clips, audio.mix).subclipped(14, 26.1)

video.write_videofile("clips/cena3.mp4", fps=24)