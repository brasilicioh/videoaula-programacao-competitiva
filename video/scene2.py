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

room_bg = (
    img_clip("img/background/bedroom.png", SCREEN_SIZE, 0, 3.6)
    .with_effects([vfx.CrossFadeOut(1)])
)
texas_bg = (
    img_clip("img/imgs/texas.jpg", SCREEN_SIZE, 3.5, 11.2)
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
)
world_bg_gif = (
    gif_clip("img/imgs/mundo_gira.gif", (SCREEN_SIZE[0], SCREEN_SIZE[1]*0.9), 14.6, 3, ("center", "top"))
    .with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(0.7)])
)
icpc_bg = (
    img_clip("img/logo/icpc.png", SCREEN_SIZE, 17.5, 6.9)
    .with_effects([vfx.CrossFadeIn(0.7), vfx.CrossFadeOut(0.5)])
)
room1_bg = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 24.3, 0.7)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

cat1 = (
    cat_clip("cat2", 0, 3.5)
)
cat2 = (
    cat_clip("cat5", 5.2, 6)
    .with_effects([vfx.CrossFadeIn(0.5)])
)

year70 = (
    img_clip("img/imgs/decada70.jpg", (500, 500), 1.4, 2.1, (60, 100))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.3)])
)
date_gif = (
    gif_clip("img/imgs/calendario.gif", (SCREEN_SIZE[0] * 0.8, SCREEN_SIZE[1] * 0.8), 11.2, 3.4)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
team1 = (
    img_clip("img/imgs/icpc_teams.jpg", (SCREEN_SIZE[0]*0.7, SCREEN_SIZE[1]*0.7), 20, 4.1)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.6)])
)
team2 = (
    img_clip("img/imgs/icpc_team1.jpg", (SCREEN_SIZE[0]*0.6, SCREEN_SIZE[1]*0.6), 21.25, 2.85)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.6)])
)
team3 = (
    img_clip("img/imgs/icpc_team2.jpg", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5), 22.5, 1.6)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.6)])
)

audio = audio_clip("cena2")

subtitle = subtitle_clip("cena2")

clips = [
    room_bg, texas_bg, world_bg_gif, icpc_bg, room1_bg,
    cat1, cat2, 
    year70, date_gif, team1, team2, team3, 
    subtitle
]

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena2.mp4", fps=24)