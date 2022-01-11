#comment
def encrypt_caesar(plaintext, shift=3):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    if shift >= 52:
        shift //= 52
    chiphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            b = ord(plaintext[i])
            if plaintext[i].isupper() and b >= 91 - shift:
                chiphertext += chr(b - 26 + shift)
            elif plaintext[i].islower() and b >= 123 - shift:
                chiphertext += chr(b - 26 + shift)
            else:
                chiphertext += chr(b + shift)
        else:
            chiphertext += plaintext[i]
    return chiphertext


def decrypt_caesar(chiphertext, shift=3):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(chiphertext)):
        if chiphertext[i].isalpha():
            b = ord(chiphertext[i])
            if chiphertext[i].isupper() and b <= 64 + shift:
                plaintext += chr(b + 26 - shift)
            elif chiphertext[i].islower() and b <= 96 + shift:
                plaintext += chr(b + 26 - shift)
            else:
                plaintext += chr(b - shift)
        elif chiphertext.isspace():
            continue
        else:
            plaintext += chiphertext[i]
    return plaintext


# def caesar_breaker_brute_force(chiphertext, dictionary):
#     """
#     Brute force breaking a Caesar cipher.
#     """
#     best_shift = 0
#     # PUT YOUR CODE HERE
#     return best_shift

print(decrypt_caesar("SBWKRQ"))
