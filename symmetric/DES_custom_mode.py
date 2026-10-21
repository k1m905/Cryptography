from Crypto.Cipher import DES

def main():
    key = bytes.fromhex("6B79466F724D4F50")
    iv = bytes.fromhex("6976466F724D4F50")
    cipher_text = bytes.fromhex("437DBAB5607137A5CFC1031114634087")

    cipher = DES.new(key,DES.MODE_ECB)

    plain_text = b""
    previous = iv

    for i in range(0, len(cipher_text), 8):
        block = cipher_text[i:i+8]

        decrypted = cipher.decrypt(block)

        for a, b in zip(decrypted, previous):
            print(a,b)
            plain_text += bytes([a ^ (b ^ 0xFF)])

        previous = block

    print(plain_text.decode("utf-8"))

if __name__ == "__main__":
    main()