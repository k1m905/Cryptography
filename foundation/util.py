from pathlib import Path
import string
import re

ENGLISH_FREQ = [
    0.082, 0.015, 0.028, 0.043, 0.127, 0.022,
    0.020, 0.061, 0.070, 0.0015, 0.0077, 0.040,
    0.024, 0.067, 0.075, 0.019, 0.00095, 0.060,
    0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015,
    0.020, 0.00074
]

def read_file(file_path):
    return Path(file_path).read_text(encoding="utf-8")

def write_file(file_path, data):
    Path(file_path).write_text(data)

def clean_txt(text):
    return re.sub(r"[^a-zA-Z]", "", text).upper()

def letter_frequency(text):
    txt = clean_txt(text)
    freq = [0] * 26 
    total = len(txt)

    if total == 0:
        return freq

    for char in txt:
        index = ord(char) - ord('A')
        freq[index] += 1

    for i in range(26):
        freq[i] = freq[i] / total

    return freq

def index_of_coincidence(text):
    txt = clean_txt(text)
    n = len(txt)
    counts = [0] * 26
    numerator = 0.0
    if n < 2:
        return 0.0

    for char in txt:
        index = ord(char) - ord('A')
        counts[index] += 1

    for i in range(26):
        count = counts[i]
        numerator = numerator + count * (count - 1)

    denominator = n * (n - 1)

    return numerator / denominator

def dot_product(freq1, freq2):
    if len(freq1) != len(freq2):
        raise ValueError("Value must be same length")

    result = 0

    for i in range(len(freq1)):
        result = result + freq1[i] * freq2[i]

    return result