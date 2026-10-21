from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder))

from foundation.util import(
    read_file,
    write_file
                            )

data_folder = project_folder / "data"
input_file = data_folder / "encrypted.txt"
output_file = data_folder / "decrypted.txt"

def caesar_decrypt(cipher_text, key):
    plain_text = ""
    reading_cipher_text = read_file(cipher_text)
    for char in reading_cipher_text:
        un_shift = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        plain_text += un_shift

    return plain_text

def main():
    plain_text = caesar_decrypt(input_file, 3)
    write_file(output_file, plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()
