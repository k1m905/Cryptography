from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "vernam_plaintext.txt"
output_file = data_folder / "vernam_encrypt.txt"

def vernam_encrypt(text, key):
    plain_text = read_file(text)
    plain_text = clean_txt(plain_text)
    key = clean_txt(key)
    plain_byte = plain_text.encode("utf-8")
    key_byte = key.encode("utf-8")

    if len(plain_byte) != len(key_byte):
        raise ValueError("Key must have the same byte length as plain text")

    cipher_byte = bytearray()

    for i in range(len(plain_byte)):
        c = plain_byte[i] ^ key_byte[i]
        cipher_byte.append(c)

    return cipher_byte.hex().upper()

def main():
    cipher_byte= vernam_encrypt(input_file, "XMCKL")
    write_file(output_file,cipher_byte)
    print(cipher_byte)

if __name__ == "__main__":
    main()