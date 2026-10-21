from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def main():
    cipher_text = bytes.fromhex("3188073EA5DB3F5C05B6307B3595607135F5D4B22F2C3EB710AA31377F78B997")
    key = "DO NOT TELL EVE!".encode("utf-8")
    iv = bytes.fromhex("20FC19123087BF6CAC8D0F1254123004")

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    plain_text = cipher.decrypt(cipher_text)
    plain_text = unpad(plain_text, AES.block_size)

    print(plain_text.decode("utf-8"))

if __name__ == "__main__":
    main()