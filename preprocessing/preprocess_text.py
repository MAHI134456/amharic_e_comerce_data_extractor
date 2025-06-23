import csv
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from cleaner import clean_amharic_text


input_file = "data/raw_media/telegram_messages.csv"  # or telegram_live.csv
output_file = "data/processed_media/cleaned_telegram_messages.csv"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["cleaned_text"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row["cleaned_text"] = clean_amharic_text(row["text"])
        writer.writerow(row)

print("✅ Cleaned Amharic text saved to:", output_file)
