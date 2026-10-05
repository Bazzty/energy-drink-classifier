"""Reduce las fotos de data/ a 512 px de lado mayor (en el lugar), corrigiendo la rotación EXIF.

Uso: uv run python reducir_fotos.py
"""
from pathlib import Path

from PIL import Image, ImageOps

MAX_SIDE = 512
EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".webp"}

for path in sorted(Path("data").rglob("*")):
    if path.suffix.lower() not in EXTENSIONS:
        continue
    image = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    image.thumbnail((MAX_SIDE, MAX_SIDE))
    image.save(path.with_suffix(".jpg"), quality=90)
    if path.suffix.lower() != ".jpg":
        path.unlink()
    print(path, image.size)
