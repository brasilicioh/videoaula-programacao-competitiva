from moviepy.editor import ImageClip

def cat_clip(name: str, start: float, duration: float) -> ImageClip:
    cat: ImageClip = ImageClip(f"img/character/{name}.png") \
        .resize(height=1080*0.55) \
        .set_start(start) \
        .set_duration(duration) \
        .set_position(("center", "center"))
    return cat

def img_clip(path: str, size: tuple, start: float, duration: float, position: tuple) -> ImageClip:
    img: ImageClip = ImageClip(path) \
        .resize(size) \
        .set_start(start) \
        .set_duration(duration) \
        .set_position(position)
    return img
