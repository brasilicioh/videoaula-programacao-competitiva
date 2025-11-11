from moviepy import vfx
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
# TODO: testar e finalizar
pessoas_sbc = (
    img_clip("img/imgs/sbc_pessoas.jpg", (SCREEN_SIZE[0]*0.7, SCREEN_SIZE[1]*0.7), 17.8, 1.9, (700, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(1)])
)

audio = audio_clip("cena5")

subtitle = subtitle_clip("cena5")

clips = [wall, cat1, cat2, cat3, cat4, sbc_logo, ano1978, cartaz_sbc, pessoas_sbc, subtitle] 

video = video_clip(clips, audio.mix).subclipped(12.5, 20.3)

video.write_videofile("clips/cena5.mp4", fps=24)