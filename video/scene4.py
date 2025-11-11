from moviepy import vfx
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

school = (
    img_clip("img/background/school.png", SCREEN_SIZE, 0, 2.3)
)
room = (
    img_clip("img/background/room2.png", SCREEN_SIZE, 11.28, 12.52)
)
wall = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 30.22, 9.31)
)

cat1 = (
    cat_clip("cat2", 0, 2.3)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
cat2 = (
    cat_clip("cat1", 11.28, 7.82, (480, 300))
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat3 = (
    cat_clip("cat6", 19.1, 4.7, (480, 300))
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat4 = (
    cat_clip("cat4", 30.22, 3.08)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat5 = (
    cat_clip("cat1", 33.3, 1.75)
    .with_effects([vfx.CrossFadeOut(0.5)])
)

question1 = (
    img_clip("img/questions/tomadas/description1.png", SCREEN_SIZE, 2.3, 5.98)
    .with_effects([vfx.FadeIn(0.5)])
)
question2 = (
    img_clip("img/questions/tomadas/description2.png", SCREEN_SIZE, 8.28, 3)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
tomada = (
    img_clip("img/imgs/tomada.png", (470, 160), 13.3, 5.5, (1300, 30))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
tomadas = [(
        img_clip("img/imgs/tomada.png", (470, 160), 13.6 + 0.3*i, 2.2 - 0.3*i, (1300, 280 + 250*i))
        .with_effects([vfx.CrossFadeIn(0.5)])
    ) for i in range(3)
]
tomadasX = [(
        img_clip("img/imgs/tomadaX.png", (470, 160), 15.8, 3, (1300, 280 + 250*i))
        .with_effects([vfx.CrossFadeOut(0.5)])
    ) for i in range(3)
]
c_response = (
    img_clip("img/questions/tomadas/c.png", (650, 640), 23.8, 6.42, ("left", "top"))
    .with_effects([vfx.CrossFadeIn(1)])
)
cpp_response = (
    img_clip("img/questions/tomadas/cpp.png", (640, 640), 24.6, 5.62, (655, "top"))
    .with_effects([vfx.CrossFadeIn(1)])
)
js_response = (
    img_clip("img/questions/tomadas/js.png", (620, 640), 25.6, 4.62, ("right", "top"))
    .with_effects([vfx.CrossFadeIn(1)])
)
py_response = (
    img_clip("img/questions/tomadas/py.png", (1400, 430), 26.75, 3.47, ("center", "bottom"))
    .with_effects([vfx.CrossFadeIn(1)])
)
rs_response = (
    img_clip("img/questions/tomadas/rs.png", (1650, 645), 27.8, 2.42, ("center", "top"))
    .with_effects([vfx.CrossFadeIn(1)])
)
c_cpp = (
    img_clip("img/imgs/c_cpp.jpg", (SCREEN_SIZE[0]*0.8, SCREEN_SIZE[1]*0.65), 35.05, 4.48, ("center", 200))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip([
    ("cena4-1", 0),
    ("cenaa", 11.28),
    ("cena4-3", 30.22)
])

subtitle = subtitle_clip("cena4")

clips = [school, room, wall, cat1, cat2, cat3, cat4 , cat5, question1, question2, 
         tomada] + tomadas + tomadasX + [c_response, cpp_response, 
         js_response, py_response, rs_response, c_cpp, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena4.mp4", fps=24)