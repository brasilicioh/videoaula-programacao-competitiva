from moviepy import vfx # vfx para efeitos crossfadein/out; se necessario, separado por virgula, importe mais coisas
from clips import (
    subtitle_clip, # para fazer legendas -> ja feito
    audio_clip, # para fazer o audio -> ja feito
    cat_clip, # retorna um ImageClip do gato
    img_clip, # retorna um ImageClip de uma imagem
    video_clip, # junta todos ImageClip's e retorna um VideoClip
    SCREEN_SIZE # tamanho constante de tela -> Full HD
)

# 
# t is a value from 0-1
def ease_inout(t: float) -> float:
    return 2 * t * t if t < 0.5 else 1 - (-2 * t + 2)**2 / 2;

# aqui, utilize o cat_clip para fazer gatos
# img_clip para fazer fotos e background
# se necessario, importe outras coisas para fazer mais clips
# veja a cena 1 e 2 para tomar como exemplo

# recomendacao: na construcao do video, coloque as variaveis em ordem cronologica
# se lembre de colocar todas variaveis no array clips seguindo a ordem de prioridade do array
# ao terminar a codificacao, organize as variaveis em ordem igual a ordem do array

room_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 56)
    .with_effects([vfx.CrossFadeIn(1)])
)

cat1 = (
    cat_clip("cat4", 0, 8.7)
)

# vai ter que fazer uma gambiarra aqui, o vfx.MirrorX deixa um espaço preto atrás
cat2 = (
    cat_clip("cat3", 8.7, 1.8)
)

#TODO: gato fica desenha no mesmo lugar que antes,
# deixando uma marca preta e não renderizando parte do gato
cat3 = (
    cat_clip("cat3", 10.5, 1)
    .with_effects([vfx.MirrorX()])
)

cat4 = (
    cat_clip("cat3", 11.5, 1.75)
)

cat5 = (
    cat_clip("cat5", 13.25, 32.67) # until 1.3700
    .with_position(lambda t: (
        # this makes sense pls, don't mess with it
        max(SCREEN_SIZE[0]/2 - 300 - 640*ease_inout(min(t/2, 1)), 20),
        "center"))
)

cat6 = (
    cat_clip("cat2", 45.82, 10.18)
)

maratona_logo = (
    img_clip("img/logo/maratona_sbc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             9, 3.7, (1144, 20))
)
icpc_logo = (
    img_clip("img/logo/icpc.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             10.5, 2.2, (200, 20))
)
obi_logo = (
    img_clip("img/logo/obi.png", (SCREEN_SIZE[0]*0.2, SCREEN_SIZE[1]*0.3),
             11, 1.7, (200, 770))
)
ioi_logo = (
    img_clip("img/logo/ioi.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             11.8, 0.9, (1144, 770))
)

# equipe de três pessoas
# Computador.jpg
# computador.jpg
# Hacker.jpeg

equipe_pessoa1 = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2 - SCREEN_SIZE[0]*0.285/2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.MirrorX(),
                   vfx.Crop(0, 0, SCREEN_SIZE[0]*0.285/2, SCREEN_SIZE[1])])
)
equipe_pessoa2 = (
    img_clip("img/imgs/computador.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.MirrorX(),
                   vfx.Crop(0, 0, SCREEN_SIZE[0]*0.285/2, SCREEN_SIZE[1])])
)
equipe_pessoa3 = (
    img_clip("img/imgs/Hacker.jpeg", (SCREEN_SIZE[0]*0.2, SCREEN_SIZE[1] * 0.3),
             23.5, 7, (SCREEN_SIZE[0] / 2 + SCREEN_SIZE[0]*0.285/2, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
)

audio = audio_clip("cena6") # pega o cena6.mp3

subtitle = subtitle_clip("cena6") # pega o srt da cena6

clips = [room_background,
         cat1, cat2, cat3, cat4, cat5, cat6,
         maratona_logo, icpc_logo, obi_logo, ioi_logo,
         equipe_pessoa1, equipe_pessoa2, equipe_pessoa3,
         subtitle] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena6.mp4", fps=24) # exporta o audio