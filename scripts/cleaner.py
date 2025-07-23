import re

def clean_amharic_text(text):
    if not isinstance(text, str):
        return ""

    # Replace emojis and unwanted chars
    text = re.sub(r"[^\u1200-\u137F0-9A-Za-z@፡።፣\s\n\-\:,]", " ", text)

    # Normalize punctuation
    text = text.replace("፡", " ").replace("።", ".")
    text = text.replace(":", " ").replace("‑", "-").replace("—", "-")

    # Ensure spaces between numbers and words
    text = re.sub(r"(\d)([፡።A-Za-z\u1200-\u137F])", r"\1 \2", text)
    text = re.sub(r"([፡።A-Za-z\u1200-\u137F])(\d)", r"\1 \2", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

