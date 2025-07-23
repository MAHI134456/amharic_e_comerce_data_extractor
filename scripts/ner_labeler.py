import re
import json
import csv

# Set of frequent filler words (Amharic + English)
FREQUENT_WORDS = {
    "እና", "ወይም", "በ", "ለ", "ዋጋ", "ብር",
    "አድራሻ", "ቁ", "ፎቅ", "-", ",", "“", "”",
    "and", "the", "to", "in", "on", "of", "with"
}

# Regex pattern to find numeric prices before "birr", "ብር", etc.
re_price = re.compile(r"(?P<num>\d{2,6})(?=\s*(?:ብር|birr|ብር))")


def is_valid_product_token(token):
    has_amharic = bool(re.search(r"[\u1200-\u137F]", token))
    is_eng = token.isupper() or token.istitle()
    return (has_amharic or is_eng) and token not in FREQUENT_WORDS and len(token) > 1


def label_message(tokens):
    labels = ["O"] * len(tokens)
    text = " ".join(tokens)

    for m in re_price.finditer(text):
        num = m.group("num")
        start_char = m.start("num")
        idx0 = text[:start_char].count(" ")
        labels[idx0] = "B-PRICE"

        # Label product tokens (max 3 before price)
        start = max(0, idx0 - 3)
        phrase = tokens[start:idx0]
        if phrase and all(is_valid_product_token(t) for t in phrase):
            labels[start] = "B-Product"
            for j in range(start + 1, idx0):
                labels[j] = "I-Product"

    # Locations: simple keyword detection
    for i, tok in enumerate(tokens):
        if tok in {"የመነሻ", "አድራሻ", "መዚድ", "ጀርባ", "ፎቅ", "ቢሮ"}:
            labels[i] = "B-LOC"

    # Contacts: phone numbers and usernames
    for i, tok in enumerate(tokens):
        if re.match(r"^09\d{8}$", tok) or tok.startswith("@"):
            labels[i] = "B-CONTACT"

    return labels


# Optional: test runner
if __name__ == "__main__":
    input_csv = "data/processed_media/cleaned_new_messages_a.csv"
    output_conll = "data/labeled/labeled_auto.conll"

    with open(input_csv, "r", encoding="utf-8") as infile, open(output_conll, "w", encoding="utf-8") as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
            tokens = json.loads(row["tokens"])
            labels = label_message(tokens)
            for tok, lbl in zip(tokens, labels):
                outfile.write(f"{tok} {lbl}\n")
            outfile.write("\n")

    print(f"✅ Saved CoNLL labels to {output_conll}")
