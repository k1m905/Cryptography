from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import(read_file, write_file, clean_txt)
from encrtyption.playfair_encryption import (create_matrix, find_position)

data_folder = project_folder / "data"
input_file = data_folder / "playfair_encrypt.txt"
output_file = data_folder / "playfair_decrypt.txt"

def playfair_decrypt(text, key):
    matrix = create_matrix(key)
    txt = clean_txt(text).replace("J","I")

    if len(txt) % 2 != 0:
        raise ValueError("Ciphertext must have even length")
    

    plain_text = ""

    for i in range(0, len(txt), 2):
        first = txt[i]
        second = txt[i + 1]

        r1, c1 = find_position(matrix, first)
        r2, c2 = find_position(matrix, second)

        if r1 == r2:
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
        elif c1 == c2:
            r1 =(r1 - 1) % 5
            r2 = (r2 - 1) % 5
        else: 
            c1, c2 = c2, c1

        plain_text += matrix[r1][c1]
        plain_text += matrix[r2][c2]

    return plain_text

def main():
    cipher_text = read_file(input_file)
    plain_text = playfair_decrypt(cipher_text, "MONOARCHY")
    write_file(output_file, plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()

