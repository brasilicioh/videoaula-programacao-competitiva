# >>> pip install moviepy

from moviepy.editor import *

WIDTH = 1280
HEIGHT = 720

background = ImageClip("img/background/bedroom.png").set_duration(3)
background = background.resize(width=WIDTH, height=HEIGHT)

character = ImageClip("img/background/wall.png").set_duration(3)

character_width = background.size[0] * 0.2  # 20% da largura do fundo
character = character.resize(width=character_width)

character = character.set_position((700, 400))  # (x, y) em pixels

video = CompositeVideoClip([background, character])
video.write_videofile("videoaula.mp4", fps=24)
