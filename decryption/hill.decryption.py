import sys
from pathlib import Path
import math

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import (
    read_file,
    write_file,
    clean_txt,    
)
data_folder = project_folder / "data"
input_file = data_folder / "hill_encrypt.txt"
output_file = data_folder / "hill_decrypt.txt"

def hill_decrypt(text, key):
    cipher_text = read_file(text)
    cipher_text = clean_txt(cipher_text)

    if len(cipher_text) % 2 != 0:
        raise ValueError("Cipher text must have even length")

    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]

    determinant = (a * d - b * c) % 26

    if math.gcd(determinant, 26) != 1:
        raise ValueError("Key matrix is not inverted")

    inverted_dat = pow(determinant, -1 , 26)

    inverted_key = [
        [(inverted_dat * d) % 26, (inverted_dat * -b) % 26],
        [(inverted_dat * -c) % 26, (inverted_dat * a) % 26]
    ]

    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        first = ord(cipher_text[i]) - ord('A')
        second = ord(cipher_text[i+1]) - ord('A')

        p1 = (inverted_key[0][0] * first + inverted_key[0][1] * second) % 26
        p2 = (inverted_key[1][0] * first + inverted_key[1][1] * second) % 26

        plain_text += chr(p1 + ord('A'))
        plain_text += chr(p2 + ord('A'))

    return plain_text

def main():
    key = [
        [3,3],
        [2,5]
    ]

    plain_text = hill_decrypt(input_file, key)
    write_file(output_file,plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()
