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
output_file = data_folder / "hill_encrypt.txt"

def hill_encrypt(text, key):
    plain_text = read_file(text)
    plain_text = clean_txt(plain_text)

    if len(plain_text) % 2 != 0:
        plain_text += "X"

    cipher_text = ""

    for i in range(0, len(plain_text), 2):
        first = ord(plain_text[i]) - ord('A')
        second = ord(plain_text[i + 1]) - ord('A')

        c1 = (key[0][0] * first + key[0][1] * second) % 26
        c2 = (key[1][0] * first + key[1][1] * second) % 26

        cipher_text += chr(c1 + ord('A'))
        cipher_text += chr(c2 + ord('A'))

    return cipher_text

def main():
    key = [
        [3,3],
        [2,5]
    ]

    cipher_text = hill_encrypt(input_file, key)
    write_file(output_file, cipher_text)
    print(cipher_text)

if __name__ == "__main__":
    main()
