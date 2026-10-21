from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "PLAINTEXT.txt"
output_file = data_folder / "vigenere_encrypt.txt"

def vigenere_encryption(text, key):
    plain_text = read_file(text)
    plain_text = clean_txt(plain_text)

    cipher_text = ""

    if not key:
        raise ValueError("Key cannot be empty")

    for i in range(len(plain_text)):
        p = ord(plain_text[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')

        c= (p + k) % 26

        cipher_text += chr(c + ord('A'))
    return cipher_text

def main():
    cipher_text = vigenere_encryption(input_file, "LEMON")
    write_file(output_file, cipher_text)
    print(cipher_text)

if __name__ == "__main__":
    main()