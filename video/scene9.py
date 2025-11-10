from moviepy import vfx # vfx para efeitos crossfadein/out; se necessario, separado por virgula, importe mais coisas
from clips import (
    subtitle_clip, # para fazer legendas -> ja feito
    audio_clip, # para fazer o audio -> ja feito
    cat_clip, # retorna um ImageClip do gato
    img_clip, # retorna um ImageClip de uma imagem
    video_clip, # junta todos ImageClip's e retorna um VideoClip
    SCREEN_SIZE # tamanho constante de tela -> Full HD
)

# aqui, utilize o cat_clip para fazer gatos
# img_clip para fazer fotos e background
# se necessario, importe outras coisas para fazer mais clips
# veja a cena 1 e 2 para tomar como exemplo

university_background = (
    img_clip("img/background/room1.png", SCREEN_SIZE, 0, 30.0 )
    .with_effects([vfx.CrossFadeIn(1)]) #adicione 1 segundo a mais na cena, para dar tempo do fade
    .with_effects([vfx.CrossFadeOut(1)])
)


cat1 = (
    cat_clip("cat1", 0, 7)
)
cat4 = (
    cat_clip("cat4", 7, 9)
)


img1 = (
    img_clip("img/imgs/Hacker.jpeg", SCREEN_SIZE, 16,8)
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
leetcodelogo = (
    img_clip("img/logo/leetcode.jpg", (500,500), 24, 6, (50,50))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
beecrowdlogo = (
    img_clip("img/logo/beecrowd.png", (500,500), 24, 6, (1370,50))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
hakerranklogo = (
    img_clip("img/logo/hackerrank.jpg", (400,250), 25, 5, (50,600))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)
codeforcelogo = (
    img_clip("img/logo/codeforces.jpg", (400,250), 25, 5, (1450,600))
    .with_effects([vfx.CrossFadeIn(0.4), vfx.CrossFadeOut(0.4)])
)








# recomendacao: na construcao do video, coloque as variaveis em ordem cronologica
# se lembre de colocar todas variaveis no array clips seguindo a ordem de prioridade do array
# ao terminar a codificacao, organize as variaveis em ordem igual a ordem do array

audio = audio_clip("cena9") # pega o cena9.mp3, a cena total tem 1:13 min

subtitle = subtitle_clip("cena9") # pega o srt da cena9

clips = [
    university_background,
    cat1, cat4,
    img1, leetcodelogo, beecrowdlogo, hakerranklogo, codeforcelogo,      
    subtitle     
        ] # adicione nessa lista todos os clips seguindo 
                   # essa ordem: backgrounds -> cats -> imgs -> subtitle

video = video_clip(clips, audio.mix) # faz video com o audio e tudo que tiver no array clips

video.write_videofile("clips/cena9.mp4", fps=4) # exporta o audio