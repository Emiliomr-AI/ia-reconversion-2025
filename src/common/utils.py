import re

_slug_re = re.compile(r"[^a-z0-9]+")


def slugify(text: str, *, maxlen: int | None = None) -> str:
    """Convierte a slug: minúsculas, alfanumérico+guiones, recorte opcional."""
    s = text.lower().strip()
    s = _slug_re.sub("-", s).strip("-")
    if maxlen is not None:
        s = s[:maxlen].rstrip("-")
    return s
