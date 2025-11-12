from moviepy import vfx, ColorClip
from clips import (
    subtitle_clip,
    audio_clip,
    cat_clip,
    img_clip,
    video_clip,
    SCREEN_SIZE
)

wall = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 0, 19.7)
    .with_effects([vfx.CrossFadeOut(1)])
)
competitive_bg = (
    img_clip("img/imgs/competitive-programming2.jpg", SCREEN_SIZE, 19.7, 6.4)
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
black_bg = (
    ColorClip(SCREEN_SIZE, color=(0, 0, 0))
    .with_start(26.1)
    .with_duration(1)
    .with_effects([vfx.CrossFadeIn(1)])
)

cat1 = (
    cat_clip("cat5", 0, 3.6)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat2 = (
    cat_clip("cat2", 3.6, 4.8)
    .with_effects([vfx.CrossFadeOut(0.5)])
)
cat3 = (
    cat_clip("cat1", 8.4, 4.3, (50, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat4 = (
    cat_clip("cat4", 12.7, 7, (50, "center"))
    .with_effects([vfx.CrossFadeOut(0.5)])
)

sbc_logo = (
    img_clip("img/logo/sbc.jpg", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5), 10, 2.9, (700, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
ano1978 = (
    img_clip("img/imgs/1978.jpg", (SCREEN_SIZE[0]*0.43, SCREEN_SIZE[1]*0.43), 12.9, 2.6, (750, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
cartaz_sbc = (
    img_clip("img/imgs/sbc_cartaz.png", (850, 850), 15.5, 2.3, (780, 80))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
pessoas_sbc = (
    img_clip("img/imgs/sbc_pessoas.jpg", (SCREEN_SIZE[0]*0.65, SCREEN_SIZE[1]*0.65), 17.8, 1.9, (600, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
obi_logo = (
    img_clip("img/logo/obi.png", (300, 500), 22.7, 3.4, (1450, 50))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)
maratona_logo = (
    img_clip("img/logo/maratona_sbc.jpg", (550, 450), 23.5, 2.6, (800, 200))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

audio = audio_clip("cena5")

subtitle = subtitle_clip("cena5")

clips = [wall, competitive_bg, black_bg, cat1, cat2, cat3, cat4, 
         sbc_logo, ano1978, cartaz_sbc, pessoas_sbc, obi_logo, 
         maratona_logo, subtitle] 

video = video_clip(clips, audio.mix)

video.write_videofile("clips/cena5.mp4", fps=24)