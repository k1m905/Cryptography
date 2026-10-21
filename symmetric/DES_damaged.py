from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

def main():
    cipher_text = bytes.fromhex("00000000000000004E51297B424F90D8B2ACD6ADF010DDC4")
    key = "CSE@YORK".encode("utf-8")
    iv = bytes.fromhex("0123456701234567")

    cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    plain_text = cipher.decrypt(cipher_text)
    plain_text = plain_text[16:]
    plain_text = unpad(plain_text, DES.block_size)

    print(plain_text.decode("utf-8"))
if __name__ == "__main__":
    main()
    