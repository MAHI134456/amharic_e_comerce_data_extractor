import random
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))


input_file = 'data/labeled/amharic_labeled.conll_a.txt'
train_path = 'data/processed_media/train_conll.txt'
test_path = 'data/processed_media/test_conll.txt'

def split_conll(input_path, train_path, test_path, split_ratio=0.8, seed=42):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Each sentence is separated by a double newline
    samples = content.strip().split("\n\n")
    random.seed(seed)
    random.shuffle(samples)

    split_point = int(len(samples) * split_ratio)
    train_samples = samples[:split_point]
    test_samples = samples[split_point:]

    with open(train_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(train_samples).strip() + "\n")

    with open(test_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(test_samples).strip() + "\n")

    print(f"✅ Total: {len(samples)}, Train: {len(train_samples)}, Test: {len(test_samples)}")
    print(f"Train saved to: {train_path}")
    print(f"Test saved to: {test_path}")


# ...existing code...

if __name__ == "__main__":
    split_conll(input_file, train_path, test_path)