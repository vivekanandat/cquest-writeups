# KEY = some integer
def xor_encrypt(plaintext, KEY):
    ciphertext = []
    for i, ch in enumerate(plaintext):
        xor_char = ord(ch) ^ ord(KEY[i % len(KEY)])
        ciphertext.append(xor_char)
    return ciphertext

def to_hex(cipher_bytes):
    return ''.join(f'{b:02x}' for b in cipher_bytes)

if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
        
    cipher_bytes = xor_encrypt(plaintext, KEY)
    cipher_hex = to_hex(cipher_bytes)
    print("Ciphertext:", cipher_hex)