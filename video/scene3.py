from moviepy import vfx
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

room_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 16)
    .with_effects([vfx.CrossFadeOut(1)])
)

cat1 = (
    cat_clip("cat2", 0, 8)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat2 = (
    cat_clip("cat3", 8, 8)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

audio = audio_clip("cena3")

subtitle = subtitle_clip("cena3")

clips = [room_background, cat1, cat2, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena3.mp4", fps=24)