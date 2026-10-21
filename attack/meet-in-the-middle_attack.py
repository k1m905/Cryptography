def encrypt(text, key):
    return (text + key) % 256

def decrypt(text, key):
    return (text - key) % 256

def main():
    plain_text = 42

    key1 = 25
    key2 = 70

    middle = encrypt(plain_text, key1)
    cipher_text = encrypt(middle, key2)

    table = {}

    for k1 in range(256):
        middle = encrypt(plain_text, k1)

        if middle not in table:
            table[middle] = []

        table[middle].append(k1)

        candidate = []

        for k2 in range(256):
            middle = decrypt(cipher_text, k2)

            if middle in table:
                for k1 in table[middle]:
                    candidate.append((k1,k2))

    print("Number of candidates:", len(candidate))
    print("Original key pair:", (key1, key2))
if __name__ == "__main__":
    main()