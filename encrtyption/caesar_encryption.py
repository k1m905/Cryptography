import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import (
    read_file,
    write_file,
    clean_txt,    
)
data_folder = project_folder / "data"
input_file = data_folder / "PLAINTEXT.txt"
output_file = data_folder / "encrypted.txt"

def caesar_encrypt(plain_text, key):
    cipher_text = ""
    reading_plain_text = read_file(plain_text)
    cleaned_plain_text = clean_txt(reading_plain_text)

    for char in cleaned_plain_text:
        if char.isalpha():
            shift_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            cipher_text += shift_char
    return cipher_text

def main():
    cipher_text = caesar_encrypt(input_file, 3)
    write_file(output_file, cipher_text)
    print(cipher_text)

if __name__ == "__main__":
    main()
