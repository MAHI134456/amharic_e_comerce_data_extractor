import re

def clean_amharic_text(text):
    if not text:
        return ""

    # Remove emojis and non-Amharic unicode
    text = re.sub(r"[^\u1200-\u137F\s]", " ", text)  # Only keep Amharic characters + space

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()
