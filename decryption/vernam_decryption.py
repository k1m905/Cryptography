from pathlib import Path
import sys

project_folder = Path(__file__).resolve().parent.parent

sys.path.insert(0,str(project_folder))

from foundation.util import read_file, write_file, clean_txt

data_folder = project_folder / "data"
input_file = data_folder / "vernam_encrypt.txt"
output_file = data_folder / "vernam_decrypt.txt"

def vernam_decrypt(text, key):
    cipher_text = read_file(text)
    key = clean_txt(key)
    cipher_byte = bytes.fromhex(cipher_text)
    key_byte = key.encode("utf-8")

    if len(cipher_byte) != len(key_byte):
        raise ValueError("Key must have the same byte length as plain text")

    plain_byte = bytearray()

    for i in range(len(cipher_byte)):
        p = cipher_byte[i] ^ key_byte[i]
        plain_byte.append(p)

    return plain_byte.decode("utf-8")

def main():
    plain_text= vernam_decrypt(input_file, "XMCKL")
    write_file(output_file,plain_text)
    print(plain_text)

if __name__ == "__main__":
    main()