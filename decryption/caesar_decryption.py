from pathlib import Path

data = Path(__file__).resolve().parent.parent / 'data'

input_file = data / "encrypted.txt"
output_file = data / "decrypted.txt"

def caesar_decrypt(cipher_text, key):
    plain_text = ""
    reading_cipher_text = cipher_text.read_text(encoding="utf-8")
    for char in reading_cipher_text:
        un_shift = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        plain_text += un_shift

    return plain_text

def main():
    plain_text = caesar_decrypt(input_file, 3)
    output_file.write_text(plain_text, encoding="utf-8")
    print(plain_text)

if __name__ == "__main__":
    main()
