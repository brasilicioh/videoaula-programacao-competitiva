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
             0, 89.57)
)

cat1 = (
    cat_clip("cat2", 0, 15)
)

sbc_logo = (
    img_clip("img/logo/sbc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             2, 3.5, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

fundamental = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             7, 1.7, (1244, "center"))
    .with_effects([vfx.Crop(x2=480), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
ens_medio = (
    img_clip("img/imgs/alunos.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             8.2, 1.8, (1244, "center"))
    .with_effects([vfx.Crop(x1=480), vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

#TODO: pegar imagem da Unicamp

obi_logo = (
    img_clip("img/logo/obi.png", (360, 600),
             9.5, 5.25, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

cat2 = (
    cat_clip("cat3", 15, 47)
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

# 00:36

iniciacao = (
    img_clip("img/imgs/prova_iniciacao.png", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             35, 10, (1244, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

cat3 = (
    cat_clip("cat4", 62, 26)
)

ioi_logo = (
    img_clip("img/logo/ioi.jpg", (SCREEN_SIZE[0]*0.35, SCREEN_SIZE[1]*0.35),
             76, 7, (1219, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

cat4 = (
    cat_clip("cat6", 88, 1.57)
)

audio = audio_clip("cena7") # pega o cena7.mp3

subtitle = subtitle_clip("cena7") # pega o srt da cena7

clips = [background,
         cat1, cat2, cat3, cat4,
         sbc_logo, obi_logo, ioi_logo,
         fundamental, ens_medio,
         chorando, programacao, iniciacao,
         subtitle] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

#video = video.subclipped(0, 14)

video.write_videofile("clips/cena7.mp4", fps=24) # exporta o audio