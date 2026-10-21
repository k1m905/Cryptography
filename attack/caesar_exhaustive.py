from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import (write_file,letter_frequency,dot_product,ENGLISH_FREQ)
from decryption.caesar_decryption import caesar_decrypt

data_folder = project_folder / "data"
encrypted_file = data_folder / "encrypted.txt"
exhaustive_attack = data_folder / "attack.txt"

def main():
    best_key = 0
    best_score = -1

    for key in range(26):
        text = caesar_decrypt(encrypted_file, key)

        freq = letter_frequency(text)
        score = dot_product(freq, ENGLISH_FREQ)

        if score > best_score:
            best_score = score
            best_key = key

    print("Best Key: ", best_key)
    print("Best Score: ", best_score)
    plain_text = caesar_decrypt(encrypted_file, best_key)\

    result = f"Best Key: {best_key}\n"
    result += f"Best Score: {best_score}\n"
    result += f"Plain Text: {plain_text}"
    write_file(exhaustive_attack, result)

    print("text: ", plain_text)

if __name__ == "__main__":
    main()
