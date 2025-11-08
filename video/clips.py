from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy import vfx, TextClip, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip
from typing import NamedTuple

SCREEN_SIZE = (1920, 1080)

def subtitle_clip(name: str) -> SubtitlesClip:
    return (
        SubtitlesClip(f"text/srt/{name}.srt", make_textclip=generator_text, encoding="utf-8")
        .with_position(("center", SCREEN_SIZE[1] - 130))
    )

class AudioBundle(NamedTuple):
    raw: AudioFileClip
    mix: CompositeAudioClip

def audio_clip(name: str, start: float = 0) -> AudioBundle:
    audio = AudioFileClip(f"sound/{name}.mp3").with_start(start)
    return AudioBundle(audio, CompositeAudioClip([audio]))

def cat_clip(name: str, start: float, duration: float, position: tuple = ("center", "center")) -> ImageClip:
    return (
        ImageClip(f"img/character/{name}.png")
        .with_effects([vfx.Resize(height=SCREEN_SIZE[1]*0.55)])
        .with_start(start)
        .with_duration(duration)
        .with_position(position)
    )

def img_clip(path: str, size: tuple, start: float, duration: float, position: tuple = ("center", "center")) -> ImageClip:
    return (
        ImageClip(path)
        .with_effects([vfx.Resize(size)])
        .with_start(start)
        .with_duration(duration)
        .with_position(position)
    )

def video_clip(clips: list, audio: CompositeAudioClip) -> CompositeVideoClip:
    duration = max([c.end for c in clips] + [audio.duration])
    return (
        CompositeVideoClip(clips, size=SCREEN_SIZE)
        .with_duration(duration)
        .with_audio(audio.with_duration(duration))
    )

generator_text = lambda txt: TextClip(
    font="C:/Windows/Fonts/arial.ttf",
    text = txt,
    font_size=54,
    color="white",
    stroke_color="black",
    stroke_width=2,
    method="caption",
    size=(SCREEN_SIZE[0] - 200, None)
)