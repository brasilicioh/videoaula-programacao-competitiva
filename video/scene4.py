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

cat1 = (
    cat_clip("cat2", 0, 2.3)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

question1 = (
    img_clip("img/questions/tomadas/description1.png", SCREEN_SIZE, 2.3, 5.98)
    .with_effects([vfx.FadeIn(0.5)])
)
question2 = (
    img_clip("img/questions/tomadas/description2.png", SCREEN_SIZE, 8.28, 3)
    .with_effects([vfx.CrossFadeOut(0.5)])
)

room = (
    img_clip("img/background/room2.png", SCREEN_SIZE, 11.28, 7.82)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

cat2 = (
    cat_clip("cat1", 11.28, 7.82)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

audio = audio_clip([
    ("cena4-1", 0),
    ("cena4-2", 11.28),
    ("cena4-3", 29.22)
])

subtitle = subtitle_clip("cena4")

clips = [school, room, cat1, cat2, question1, question2, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena4.mp4", fps=24)