from moviepy import vfx # vfx para efeitos crossfadein/out; se necessario, separado por virgula, importe mais coisas
from clips import (
    subtitle_clip, # para fazer legendas -> ja feito
    audio_clip, # para fazer o audio -> ja feito
    cat_clip, # retorna um ImageClip do gato
    img_clip, # retorna um ImageClip de uma imagem
    video_clip, # junta todos ImageClip's e retorna um VideoClip
    gif_clip,
    SCREEN_SIZE # tamanho constante de tela -> Full HD
)

university_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 12.8)
    .with_effects([vfx.CrossFadeIn(1)])
    .with_effects([vfx.CrossFadeOut(1)])
)
wall_background = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 22.4, 12.6)
    .with_effects([vfx.CrossFadeIn(0.5)])
    .with_effects([vfx.CrossFadeOut(0.5)])
)



cat6 = (
    cat_clip("cat6", 0, 4.8)
)
cat2 = (
    cat_clip("cat2", 4.8, 4.2)
)
cat4 = (
    cat_clip("cat4", 9, 3.8)
)
cat1 = (
    cat_clip("cat1", 22.4, 5.6)
    .with_effects([vfx.CrossFadeIn(0.5)])
)
cat3 = (
    cat_clip("cat3", 28, 4, position=(200,"center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)




gif1 = (
    gif_clip("img/imgs/cyberwave.gif", SCREEN_SIZE, 12.8, 9.4)
    .with_effects([vfx.CrossFadeIn(0.8), vfx.CrossFadeOut(0.8)])
)
img1 = (
    img_clip("img/imgs/fun.jpg", (750,600), 28, 4, (1100,200))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)


# aqui, utilize o cat_clip para fazer gatos
# img_clip para fazer fotos e background
# se necessario, importe outras coisas para fazer mais clips
# veja a cena 1 e 2 para tomar como exemplo

# recomendacao: na construcao do video, coloque as variaveis em ordem cronologica
# se lembre de colocar todas variaveis no array clips seguindo a ordem de prioridade do array
# ao terminar a codificacao, organize as variaveis em ordem igual a ordem do array

audio = audio_clip("cena10") # pega o cena10.mp3

subtitle = subtitle_clip("cena10") # pega o srt da cena10

clips = [
    university_background, wall_background,
    gif1,
    cat6, cat4, cat2,cat3, cat1,
    img1,
    subtitle
    ] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena10.mp4", fps=12) # exporta o audio