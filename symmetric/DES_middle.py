from Crypto.Cipher import DES
from pathlib import Path
project_folder = Path(__file__).resolve().parent.parent

data_folder = project_folder / "data"
input_file = data_folder / "DES_hex.txt"

def main():
    cipher_text = input_file.read_text(encoding = "utf-8")
    key = b"FACEBOOK"
    complement_key = b""

    for b in key:
        complement = b ^ 0xFF
        complement_key += bytes([complement]) 
    cipher_hex = bytes.fromhex(cipher_text)

    cipher1 = DES.new(complement_key, DES.MODE_ECB)
    middle = cipher1.decrypt(cipher_hex)

    cipher2 = DES.new(key, DES.MODE_ECB)
    plain_text = cipher2.decrypt(middle)

    print(plain_text.decode("utf-8"))

if __name__ == "__main__":
    main()

