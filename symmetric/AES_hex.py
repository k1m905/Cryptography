from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def main():
    cipher_text =bytes.fromhex("F38ADBA8A7B4CC613578355032205D50")
    key = bytes.fromhex("9F0DCEDB322F3C6873F9256E01376BA4")
    iv = bytes.fromhex("20FC19123087BF6CAC8D0F1254123004")

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    plain_text = cipher.decrypt(cipher_text)
    plain_text = unpad(plain_text, AES.block_size)

    print(plain_text.decode("utf-8"))

if __name__ == "__main__":
    main()