from moviepy import vfx
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    gif_clip,
    video_clip,
    SCREEN_SIZE
)

school = (
    img_clip("img/background/school.png", SCREEN_SIZE, 0, 2.3)
)
room = (
    img_clip("img/background/room2.png", SCREEN_SIZE, 11.28, 12.72)
)
matrix = (
    gif_clip("img/imgs/matrix.gif", SCREEN_SIZE, 24, 8)
)
wall = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 32, 10.2)
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
    cat_clip("cat6", 19.1, 4.9, (480, 300))
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat4 = (
    cat_clip("cat4", 32, 3.1)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat5 = (
    cat_clip("cat1", 35.1, 2.1)
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
    img_clip("img/questions/tomadas/c.png", (750, 940), 24, 1.5)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cpp_response = (
    img_clip("img/questions/tomadas/cpp.png", (750, 940), 25.5, 1.5)
)
js_response = (
    img_clip("img/questions/tomadas/js.png", (900, 800), 27, 1.5)
)
py_response = (
    img_clip("img/questions/tomadas/py.png", (1100, 500), 28.5, 1.5)
)
rs_response = (
    img_clip("img/questions/tomadas/rs.png", (1320, 790), 30, 2)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
c_cpp_car = (
    img_clip("img/imgs/c_cpp.jpg", (SCREEN_SIZE[0]*0.8, SCREEN_SIZE[1]*0.7), 37.2, 4.2)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip([
    ("cena4-1", 0),
    ("cena4-2", 11.28),
    ("cena4-3", 32.2)
])

subtitle = subtitle_clip("cena4")

clips = [
    school, room, matrix, wall, 
    cat1, cat2, cat3, cat4, cat5, 
    question1, question2, tomada] + tomadas + tomadasX + \
    [c_response, cpp_response, js_response, py_response, 
    rs_response, c_cpp_car,
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena4.mp4", fps=24)