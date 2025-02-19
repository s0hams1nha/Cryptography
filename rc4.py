def rc4(text, key):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    keystream = []

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        keystream_byte = S[(S[i] + S[j]) % 256]
        keystream.append(ord(char)^keystream_byte)
    return (bytes(keystream).hex())

text = input("Enter Text: ")
key = input("Enter Key: ")

print("Ciphertext is: ", rc4(text, key))