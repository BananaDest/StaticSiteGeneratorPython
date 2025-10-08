def extract_title(markdown):
    if not markdown.startswith("# "):
        raise ValueError("no header")
    return markdown.strip("# ")
