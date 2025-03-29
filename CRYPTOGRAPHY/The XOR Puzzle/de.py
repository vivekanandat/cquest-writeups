def from_hex(cipher_hex):
    # Convert the hexadecimal string back to a list of integer bytes
    return [int(cipher_hex[i:i+2], 16) for i in range(0, len(cipher_hex), 2)]

def xor_decrypt(cipher_bytes, key):
    plaintext_chars = []
    # XOR each byte with the corresponding key character (repeating the key)
    for i, byte in enumerate(cipher_bytes):
        decrypted_byte = byte ^ ord(key[i % len(key)])
        plaintext_chars.append(chr(decrypted_byte))
    return ''.join(plaintext_chars)

if __name__ == "__main__":
    cipher_hex = input("Enter the ciphertext in hex: ")
    key = input("Enter the decryption key: ")
    
    if not key:
        print("Decryption key cannot be empty!")
        exit(1)

    cipher_bytes = from_hex(cipher_hex)
    plaintext = xor_decrypt(cipher_bytes, key)
    
    print("Decrypted text:", plaintext)