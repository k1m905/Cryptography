from pathlib import Path
import sys
import math

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import (
    read_file,
    write_file,
    clean_txt
)

data_folder = project_folder / 'data'
plain_file = data_folder / 'PLAINTEXT.txt'
encrypte_file = data_folder / 'affine_encrypt.txt'

def affine_encryption(text, a, b):
    cipher_text = ""

    plain_text = read_file(text)
    plain_text = clean_txt(plain_text)

    if math.gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26")

    for char in plain_text:
        p = ord(char) - ord('A')
        c = (a * p + b) % 26
        encrypted_char = chr(c + ord('A'))
        cipher_text += encrypted_char

    return cipher_text

def main():
    cipher_text = affine_encryption(plain_file, 5, 8)
    write_file(encrypte_file, cipher_text)

    print(cipher_text)

if __name__ == "__main__":
    main()



