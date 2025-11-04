from moviepy.editor import *

tempo = 18.0
video_size = (1080, 720)

audio_clip = AudioFileClip("sound\\saida_audio.mp3")

bg_clip = ImageClip("img\\background\\bedroom.png").set_duration(tempo).resize(video_size)

char1 = ImageClip("img\\background\\wall.png").resize(height=video_size[1] * 0.4).set_position(("center", "center"))
char2 = ImageClip("img\\background\\school.png").resize(height=video_size[1] * 0.4).set_position(("center", "center"))

# Clip 1: Personagem 1 (Começa em 0s, dura 6s)
char_clip1 = char1.set_duration(6).set_start(0.0)
# Clip 2: Personagem 2 (Começa em 6s, dura 6s)
char_clip2 = char2.set_duration(6).set_start(6)
# Clip 3: Personagem 1 (Começa em 12s, dura 6s)
char_clip3 = char1.set_duration(6).set_start(12)

textos_legendas = [f"Legenda {i+1}" for i in range(6)]

font_size = 40
font_color = 'white'
stroke_color = 'black'
stroke_width = 1.5
font_style = 'Arial' 

lista_de_clipes_texto = []
duracao_por_legenda = tempo / len(textos_legendas)

for i, texto in enumerate(textos_legendas):
    # Define o tempo de início de cada legenda
    start_time = i * duracao_por_legenda
    
    legenda_clip = TextClip(
        texto,
        fontsize=font_size,
        color=font_color,
        font=font_style,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
        size=(video_size[0] * 0.8, None), # Largura max de 80% do vídeo
        method='caption' # Faz o texto quebrar a linha automaticamente
    )
    
    legenda_clip = legenda_clip.set_start(start_time).set_duration(duracao_por_legenda)
    legenda_clip = legenda_clip.set_position(('center', video_size[1] - 100))
    
    lista_de_clipes_texto.append(legenda_clip)

# A ordem importa: o primeiro item fica no fundo, os últimos ficam na frente.
todos_os_clipes = [
    bg_clip,
    char_clip1,
    char_clip2,
    char_clip3
] + lista_de_clipes_texto # Adiciona as legendas por cima de todo o resto

# CompositeVideoClip junta todas as camadas
final_video = CompositeVideoClip(
    todos_os_clipes,
    size=video_size
)

final_video = final_video.set_duration(tempo).set_audio(audio_clip)

final_video.write_videofile(
    "videoaula.mp4",
    fps=24,
    codec='libx264',
    audio_codec='aac'
)