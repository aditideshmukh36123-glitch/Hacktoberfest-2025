import sys
from collections import Counter
import string

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Basic counts
    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    print(f"File: {file_path}")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {chars}")

    # Most common words
    # Remove punctuation and convert to lowercase
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]
    counter = Counter(cleaned_words)
    most_common = counter.most_common(5)
    print("\nMost common words:")
    for word, count in most_common:
        print(f"{word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python text_analyzer.py <filename.txt>")
    else:
        analyze_file(sys.argv[1])
