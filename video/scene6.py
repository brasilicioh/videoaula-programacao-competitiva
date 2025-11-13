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
    return 2 * t * t if t < 0.5 else 1 - (-2 * t + 2)**2 / 2

# aqui, utilize o cat_clip para fazer gatos
# img_clip para fazer fotos e background
# se necessario, importe outras coisas para fazer mais clips
# veja a cena 1 e 2 para tomar como exemplo

# recomendacao: na construcao do video, coloque as variaveis em ordem cronologica
# se lembre de colocar todas variaveis no array clips seguindo a ordem de prioridade do array
# ao terminar a codificacao, organize as variaveis em ordem igual a ordem do array

room_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 56.45)
    .with_effects([vfx.CrossFadeIn(1)])
)

cat1 = (
    cat_clip("cat4", 0, 8.7)
)

cat2 = (
    cat_clip("cat3", 8.7, 1.8)
)

cat3 = (
    cat_clip("cat3_lado", 10.5, 1.25)
)

cat4 = (
    cat_clip("cat3", 11.75, 1.7) # 25
)

cat5 = (
    cat_clip("cat5", 13.45, 18.05) # until 1.3700
    .with_position(lambda t: (
        # this makes sense pls, don't mess with it
        max(SCREEN_SIZE[0]/2 - 300 - 10 - 640*ease_inout(min(t/2, 1)), 10),
        "center"))
)

cat6 = (
    cat_clip("cat2", 31.5, 24.95)
    .with_position(lambda t: (
        # this makes sense pls, don't mess with it
        (SCREEN_SIZE[0]/2 - 300 - 10) - (max(SCREEN_SIZE[0]/2 - 300 - 10 - 640*ease_inout(min(t/2, 1)), 430)),
        "center"))
)

mundo = (
    img_clip("img/imgs/mundo.jpg", (SCREEN_SIZE[0]*0.3, SCREEN_SIZE[1]*0.3),
             5, 3, (SCREEN_SIZE[0]*5/8, "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.25)])
)

sbc_competition = (
    img_clip("img/imgs/sbc_ginasio.png", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             15.25, 8.25, (SCREEN_SIZE[0]*3/8, "center"))
    .with_effects([vfx.CrossFadeIn(0.5)])
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

ballon1 = (
    img_clip("img/imgs/balao1.png", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1] * 0.8),
             33, 4, (SCREEN_SIZE[0]*(1/2), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)
# Images cross fade into eachother
ballon2 = (
    img_clip("img/imgs/balao2.png", (SCREEN_SIZE[0]*0.4, SCREEN_SIZE[1] * 0.8),
             36, 2.5, (SCREEN_SIZE[0]*(1/2), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

# Nas competiçoes físicas...

sbc_pessoas = (
    img_clip("img/imgs/sbc_pessoas.jpg", ((SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1] * 0.5)),
             40, 5, (SCREEN_SIZE[0]*(1/2 - 1/32), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
)

icpc_competition = (
    img_clip("img/imgs/icpc_teams.jpg", (SCREEN_SIZE[0]*0.5, SCREEN_SIZE[1]*0.5),
             46, 10.45, (SCREEN_SIZE[0]*(1/2 - 1/32), "center"))
    .with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.25)])
)

audio = audio_clip("cena6") # pega o cena6.mp3

subtitle = subtitle_clip("cena6") # pega o srt da cena6

clips = [room_background,
         cat1, cat2, cat3, cat4, cat5, cat6,
         mundo, sbc_competition,
         maratona_logo, icpc_logo, obi_logo, ioi_logo,
         equipe_pessoa1, equipe_pessoa2, equipe_pessoa3,
         sbc_pessoas, icpc_competition,
         ballon1, ballon2,
         subtitle] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena6.mp4", fps=24, threads=32) # exporta o audio