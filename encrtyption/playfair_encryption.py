from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import(read_file, write_file, clean_txt)

data_folder = project_folder / "data"
input_file = data_folder / "PLAINTEXT.txt"
output_file = data_folder / "playfair_encrypt.txt"

def create_matrix(key):
    key = clean_txt(key).replace("J","I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    letters = ""

    for char in key + alphabet:
        if char not in letters:
            letters += char
    matrix = []

    for i in range(5):
        row = []

        for j in range(5):
            row.append(letters[i * 5 + j])

        matrix.append(row)

    return matrix

def prepare_text(text):
    text = clean_txt(text).replace("J","I")

    result = ""
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]
        else:
            second = "X"

        if first == second:
            second = "X" if first != "X" else "Q"
            i += 1
        else:
            i += 2
        result += first + second

    return result

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    raise ValueError("Letter not found")

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    txt = prepare_text(text)

    cipher_text = ""

    for i in range(0, len(txt), 2):
        first = txt[i]
        second = txt[i + 1]

        r1, c1 = find_position(matrix, first)
        r2, c2 = find_position(matrix, second)

        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 =(r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else: 
            c1, c2 = c2, c1

        cipher_text += matrix[r1][c1]
        cipher_text += matrix[r2][c2]

    return cipher_text

def main():
    plain_text = read_file(input_file)
    cipher_text = playfair_encrypt(plain_text, "MONOARCHY")
    write_file(output_file, cipher_text)
    print(cipher_text)

if __name__ == "__main__":
    main()

