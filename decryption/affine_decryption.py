from pathlib import Path
import sys
import math

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import(read_file, write_file, clean_txt)

data_folder = project_folder / "data"
input_file = data_folder / "affine_encrypt.txt"
output_file = data_folder / "affine_decrypt.txt"

def affine_decrypt(text, a, b):
    plain_text = ""

    cipher_text = read_file(text)
    cipher_text = clean_txt(cipher_text)

    if math.gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26")

    a_inverse = pow(a, -1, 26)
    for char in cipher_text:
        c = ord(char) - ord('A')
        p = a_inverse * (c - b) % 26

        plain_text_char = chr(p + ord('A'))
        plain_text += plain_text_char
    return plain_text

def main():
    decrypted_text = affine_decrypt(input_file, 5, 8)
    write_file(output_file, decrypted_text)
    print(decrypted_text)

if __name__ == "__main__":
    main()