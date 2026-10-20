import re
from pathlib import Path

data_folder = Path(__file__).resolve().parent.parent / "data"

input_file = data_folder / "PLAINTEXT.txt"
output_file = data_folder / "encrypted.txt"

def caesar_encrypt(plain_text, key):
    cipher_text = ""
    reading_plain_text = plain_text.read_text(encoding="utf-8")
    cleaned_plain_text = re.sub(r"[^a-zA-Z]", "", reading_plain_text).upper()

    for char in cleaned_plain_text:
        if char.isalpha():
            shift_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            cipher_text += shift_char
    return cipher_text

def main():
    cipher_text = caesar_encrypt(input_file, 3)
    output_file.write_text(cipher_text, encoding="utf-8")
    print(cipher_text)

if __name__ == "__main__":
    main()
