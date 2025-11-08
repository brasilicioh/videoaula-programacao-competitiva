from moviepy import vfx, VideoFileClip
from Clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

room_background = (
    img_clip("img/background/bedroom.png", SCREEN_SIZE, 0, 3.2)
    .with_effects([vfx.CrossFadeOut(1)])
)
university_background = (
    img_clip("img/imgs/texas.jpg", SCREEN_SIZE, 3.2, 10.3)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
world_background = (
    img_clip("img/imgs/mundo.jpg", SCREEN_SIZE, 13.5, 3)
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
)
icpc_background = (
    img_clip("img/logo/icpc.jpg", SCREEN_SIZE, 16, 7)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

cat1 = cat_clip("cat2", 0, 3)
cat2 = (
    cat_clip("cat5", 5, 5, ("center", "center"))
    .with_effects([vfx.CrossFadeIn(0.75)])
)

img1 = (
    img_clip("img/imgs/decada70.jpg", (500, 500), 1.2, 1.9, (60, 100))
    .with_effects([vfx.CrossFadeIn(0.7), vfx.CrossFadeOut(0.3)])
)
img2 = (
    VideoFileClip("img/imgs/calendario.gif")
    .with_effects([vfx.Loop(duration=3.5)])
    .with_effects([vfx.Resize((SCREEN_SIZE[0] * 0.8, SCREEN_SIZE[1] * 0.8))])
    .with_start(10)
    .with_position(("center", "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
img3 = (
    img_clip("img/imgs/icpc_teams.jpg", (SCREEN_SIZE[0]*0.7, SCREEN_SIZE[1]*0.7), 18, 4.25)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
img4 = (
    img_clip("img/imgs/icpc_team1.jpg", (SCREEN_SIZE[0]*0.6, SCREEN_SIZE[1]*0.6), 19.25, 3)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
img5 = (
    img_clip("img/imgs/icpc_team2.jpg", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5), 20.75, 2)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

audio = audio_clip("cena2")

subtitle = subtitle_clip("cena2")

clips = [room_background, university_background, world_background, icpc_background, 
         cat1, cat2, img1, img2, img3, img4, img5, subtitle]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena2.mp4", fps=24)