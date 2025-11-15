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

room1_bg = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 16.5)
)
leetcode1_bg = (
    img_clip("img/imgs/leetcode1.png", SCREEN_SIZE, 16.5, 2)
)
leetcode2_bg = (
    img_clip("img/imgs/leetcode2.png", SCREEN_SIZE, 18.5, 2.8)
)
black_bg = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(20.3)
    .with_duration(26.1)
)
school_bg = (
    img_clip("img/background/school.png", SCREEN_SIZE, 39.1, 31)
)

cat1 = (
    cat_clip("cat2", 0, 8, (900, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
cat2 = (
    cat_clip("cat3", 8, 8.4, ("left", "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
cat3 = (
    cat_clip("cat6", 39.1, 5.7)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat4 = (
    cat_clip("cat4", 44.8, 5.1)
)
cat5 = (
    cat_clip("cat2", 49.9, 5.6)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat6 = (
    cat_clip("cat5", 55.5, 7.5, (100, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat7 = (
    cat_clip("cat1", 63, 7.1, (100, "center"))
    .with_effects([vfx.CrossFadeOut(0.5)])
)

helloworld = (
    img_clip("img/imgs/meme_helloworld.jpg", (770, 770), 2.5, 5.1, (90, 100))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
io_img = (
    img_clip("img/imgs/io.webp", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1]*0.4), 8, 8.4, ("center", "center"))
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(0.5)])
)
brainIA = (
    img_clip("img/imgs/sciencephile.jpg", (530, 530), 20.3, 3.7, ("center", 10))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
submit_gif = (
    gif_clip("img/imgs/submit.gif", (852, 520), 20.6, 3.4, ("center", 590))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
io_gif = (
    gif_clip("img/imgs/io.gif", SCREEN_SIZE, 23, 3)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
io_sheet1 = (
    img_clip("img/imgs/tabela.png", (SCREEN_SIZE[0]*0.7, SCREEN_SIZE[1]*0.7), 26, 3.5)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
io_sheet2 = (
    img_clip("img/imgs/tabela2.png", (SCREEN_SIZE[0]*0.7, SCREEN_SIZE[1]*0.7), 29.5, 6.6)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
deslikes_position = [(x, y) for y in ["top", "center", "bottom"] for x in ["left", "center", "right"]]
deslikes_array = [
    img_clip("img/imgs/deslike.png", (300, 300), 31.2 + 0.3*i, 4.9 - 0.3*i, deslikes_position[i])
    .with_effects([vfx.CrossFadeOut(0.75)]) for i in range(9)
]
time_limit = (
    img_clip("img/imgs/time-limit-exceeded.jpg", (600, 800), 36.1, 3)
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
)
submissions1 = (
    img_clip("img/imgs/submissions.png", (850, 850), 55.5, 5, (700, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)
submissions2 = (
    img_clip("img/imgs/submissions2.png", (850, 850), 60.5, 2.5, (700, "center"))
    .with_effects([vfx.CrossFadeOut(0.5)])
)
correto = (
    img_clip("img/imgs/correto.png", (400, 400), 65, 4, (1300, 0))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
parcial = (
    img_clip("img/imgs/maismenos.png", (400, 400), 65.8, 3.4, (1000, 330))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
errado = (
    img_clip("img/imgs/errado.png", (400, 400), 66.4, 2.8, (650, 580))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip("cena3")

subtitle = subtitle_clip("cena3")

clips = [
    room1_bg, leetcode1_bg, leetcode2_bg, black_bg, school_bg, 
    cat1, cat2, cat3, cat4, cat5, cat6, cat7, 
    helloworld, io_img, 
    brainIA, submit_gif, io_gif, io_sheet1, io_sheet2] + \
    deslikes_array + [time_limit, submissions1, submissions2, 
    correto, parcial, errado, 
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena3.mp4", fps=24)