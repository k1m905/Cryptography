from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "vigenere_encrypt.txt"
output_file = data_folder / "vigenere_decrypt.txt"

def vigenere_decryption(text, key):
    cipher_text = read_file(text)
    cipher_text = clean_txt(cipher_text)
    key = clean_txt(key)

    plain_text = ""

    if not key:
        raise ValueError("Key cannot be empty")

    for i in range(len(cipher_text)):
        c = ord(cipher_text[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')

        p= (c - k) % 26

        plain_text += chr(p + ord('A'))
    return plain_text

def main():
    plain_text = vigenere_decryption(input_file, "LEMON")
    write_file(output_file, plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()