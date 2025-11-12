from moviepy import vfx # vfx para efeitos crossfadein/out; se necessario, separado por virgula, importe mais coisas
from clips import (
    subtitle_clip, # para fazer legendas -> ja feito
    audio_clip, # para fazer o audio -> ja feito
    cat_clip, # retorna um ImageClip do gato
    img_clip, # retorna um ImageClip de uma imagem
    gif_clip,
    video_clip, # junta todos ImageClip's e retorna um VideoClip
    SCREEN_SIZE # tamanho constante de tela -> Full HD
)

# aqui, utilize o cat_clip para fazer gatos
# img_clip para fazer fotos e background
# se necessario, importe outras coisas para fazer mais clips
# veja a cena 1 e 2 para tomar como exemplo

# recomendacao: na construcao do video, coloque as variaveis em ordem cronologica
# se lembre de colocar todas variaveis no array clips seguindo a ordem de prioridade do array
# ao terminar a codificacao, organize as variaveis em ordem igual a ordem do array
wall_background = (
    img_clip("img/background/wall.png", SCREEN_SIZE, 0, 19.0)
    .with_effects([vfx.CrossFadeOut(1)]) #adicione 1 segundo a mais na cena, para dar tempo do fade
)
interval_background = (
    img_clip("img/questions/distinto/description1.png", SCREEN_SIZE, 18.5, 28.0)
    .with_effects([vfx.CrossFadeIn(0.5)]) #adicione 1 segundo a mais na cena, para dar tempo do fade
)
university_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 31.0, 23.0 )
    .with_effects([vfx.CrossFadeIn(1)]) #adicione 1 segundo a mais na cena, para dar tempo do fade
    .with_effects([vfx.CrossFadeOut(1)])
)



cat4 = (
    cat_clip("cat4", 0, 5)
)
cat3 = (
    cat_clip("cat3", 5, 7)
)
cat5 = (
    cat_clip("cat5", 12, 6.5)
)

cat6 = (
    cat_clip("cat6", 32, 11)
)



img1 = (
    img_clip("img/questions/distinto/c.png", (1000,1000), 48.30, 0.7)
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
img2 = (
    img_clip("img/questions/distinto/cpp.png", (1000,1000), 49, 1.5)
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
img3 = (
    img_clip("img/questions/distinto/js.png", (1000,1000), 50.5, 1.3)
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
img4 = (
    img_clip("img/questions/distinto/py.png", (1000,1000), 51.8, 1.0 )
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
img5 = (
    img_clip("img/questions/distinto/rs.png", (1000,1000), 52.8, 1.2)
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)


gif1 = (
    gif_clip("img/imgs/matrix.gif", SCREEN_SIZE, 43, 11)
)


audio = audio_clip([
    ("cena8-1", 0), # pega o cena8-1 e começa em 0 31s
    ("cena8-2", 31.53), # pega o cena8-2 -> start definido pelo tempo no srt 27s
])

subtitle = subtitle_clip("cena8") # pega o srt da cena8

clips = [wall_background, interval_background, university_background,
        cat3, cat4, cat5, cat6,
        gif1,img1, img2, img3, img4, img5,
        subtitle
        ] # adicione nessa lista todos os clips seguindo 
# essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena8.mp4", fps=4) # exporta o audio