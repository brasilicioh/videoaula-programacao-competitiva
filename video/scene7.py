from moviepy import vfx # vfx para efeitos crossfadein/out; se necessario, separado por virgula, importe mais coisas
from clips import (
    subtitle_clip, # para fazer legendas -> ja feito
    audio_clip, # para fazer o audio -> ja feito
    cat_clip, # retorna um ImageClip do gato
    img_clip, # retorna um ImageClip de uma imagem
    video_clip, # junta todos ImageClip's e retorna um VideoClip
    SCREEN_SIZE # tamanho constante de tela -> Full HD
)

background = (
    img_clip("img/background/school.png", SCREEN_SIZE,
             0, 89)
)

cat1 = (
    cat_clip("cat2", 0, 15)
)

sbc_logo = (
    img_clip("img/logo/sbc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             2, 3, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)

fundamental = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             7, 1.7, (1244, "center"))
    .with_effects([vfx.Crop(x1 = 0, x2=320), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
ens_medio = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             8.2, 1.8, (1244, "center"))
    .with_effects([vfx.Crop(x1=256), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

#TODO: pegar imagem da Unicamp

obi_logo = (
    img_clip("img/logo/obi.png", (300, 500),
             9.5, 5.25, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

cat2 = (
    cat_clip("cat3", 15, 20)
)

chorando = (
    img_clip("img/imgs/chorando.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             17.2, 2.8, (100, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

programacao = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             18, 2, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

audio = audio_clip("cena7") # pega o cena7.mp3

subtitle = subtitle_clip("cena7") # pega o srt da cena7

clips = [background,
         cat1, cat2,
         sbc_logo, obi_logo,
         fundamental, ens_medio,
         chorando, programacao,
         subtitle] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena7.mp4", fps=24) # exporta o audio