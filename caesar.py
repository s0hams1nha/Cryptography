dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
text = "ABCDE"
shift = 3
ciphertext = ""

for i in text:
    new_char = chr(((ord(i) - ord('A') + shift) % 5) + ord('A'))
    ciphertext += new_char

print(ciphertext)