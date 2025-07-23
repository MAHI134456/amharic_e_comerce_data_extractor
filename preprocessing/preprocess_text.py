import csv, json, os, sys

# Add scripts/ to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from cleaner import clean_amharic_text
from tokenizer import tokenize_amharic_text


input_file = 'data/raw_media/telegram_data_a.csv'
output_file = "data/processed_media/cleaned_new_messages_a.csv"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    text_col = None
    for col in reader.fieldnames:
        if "text" in col.lower():
            text_col = col
            break
    if not text_col:
        raise ValueError("No message text column found!")

    writer = csv.DictWriter(outfile, fieldnames=[
        "channel_title", "channel_username", "message_id",
        "timestamp", "cleaned_text", "tokens"
    ])
    writer.writeheader()

    for r in reader:
        raw = r.get(text_col, "")
        cleaned = clean_amharic_text(raw)
        if not cleaned:
            continue
        tokens = tokenize_amharic_text(cleaned)
        writer.writerow({
            "channel_title": r.get("Channel Title", ""),
            "channel_username": r.get("Channel Username", ""),
            "message_id": r.get("Message ID", ""),
            "timestamp": r.get("Date", ""),
            "cleaned_text": cleaned,
            "tokens": json.dumps(tokens, ensure_ascii=False)
        })

print("✅ Cleaned and tokenized data:", output_file)
