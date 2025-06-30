def rsa_encrypt(message, e, n):
    return pow(message, e, n)

def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Example usage
p, q = 3, 11
n = p * q
e = 7
d = 3  # Simplified, normally computed
message = 9
ciphertext = rsa_encrypt(message, e, n)
decrypted = rsa_decrypt(ciphertext, d, n)
print("Encrypted:", ciphertext, "Decrypted:", decrypted)