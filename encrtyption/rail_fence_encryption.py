from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "PLAINTEXT.txt"
output_file = data_folder / "rail_fence_encrypt.txt"


def rail_fence_encrypt(text, key):
    plain_text = read_file(text)
    plain_text = clean_txt(plain_text)

    if key < 2:
        raise ValueError("Key must be at least 2")

    rails = []

    for i in range(key):
        rails.append("")

    row = 0
    direction = 1

    for char in plain_text:
        rails[row] += char

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    cipher_text = ""

    for rail in rails:
        cipher_text += rail

    return cipher_text

def main():
    cipher_text = rail_fence_encrypt(input_file, 3)
    write_file(output_file,cipher_text)
    print(cipher_text)

if __name__ == "__main__":
    main()
