from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import TextClip, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip
from typing import NamedTuple
import moviepy.config as conf
conf.change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.2-Q16-HDRI/magick.exe"})

SCREEN_SIZE = (1920, 1080)

def subtitle_clip(name: str) -> SubtitlesClip:
    return (
        SubtitlesClip(f"texto/{name}.srt", generator_text)
        .set_position(("center", SCREEN_SIZE[1] - 130))
    )

class AudioBundle(NamedTuple):
    raw: AudioFileClip
    mix: CompositeAudioClip

def audio_clip(name: str, start: float = 0) -> AudioBundle:
    audio = AudioFileClip(f"sound/{name}.mp3").set_start(start)
    return AudioBundle(audio, CompositeAudioClip([audio]))

def cat_clip(name: str, start: float, duration: float, position: tuple = ("center", "center")) -> ImageClip:
    return (
        ImageClip(f"img/character/{name}.png")
        .resize(height=SCREEN_SIZE[1]*0.55)
        .set_start(start)
        .set_duration(duration)
        .set_position(position)
    )

def img_clip(path: str, size: tuple, start: float, duration: float, position: tuple = ("center", "center")) -> ImageClip:
    return (
        ImageClip(path)
        .resize(size)
        .set_start(start)
        .set_duration(duration)
        .set_position(position)
    )

def video_clip(clips: list, audio: CompositeAudioClip) -> CompositeVideoClip:
    duration = max([c.end for c in clips] + [audio.duration])
    return (
        CompositeVideoClip(clips, size=SCREEN_SIZE)
        .set_duration(duration)
        .set_audio(audio.set_duration(duration))
    )

generator_text = lambda txt: TextClip(
    txt,
    font="Arial-Bold",
    fontsize=54,
    color="white",
    stroke_color="black",
    stroke_width=2,
    method="caption",
    size=(SCREEN_SIZE[0] - 200, None)
)