from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "rail_fence_encrypt.txt"
output_file = data_folder / "rail_fence_decrypt.txt"


def rail_fence_decrypt(text, key):
    cipher_text = read_file(text)
    cipher_text = clean_txt(cipher_text)

    if key < 2:
        raise ValueError("Key must be at least 2")

    length = len(cipher_text)

    pattern = []
    row = 0
    direction = 1

    for i in range(length):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    rails = []

    for i in range(length):
        rails.append([])

    index = 0

    for r in range(key):
        for i in range(length):
            if pattern[i] == r:
                rails[r].append(cipher_text[index])
                index += 1

    position = [0] * key
    plain_text = ""

    for r in pattern:
        plain_text += rails[r][position[r]]
        position[r] += 1

    return plain_text

def main():
    plain_text = rail_fence_decrypt(input_file, 3)
    write_file(output_file,plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()
