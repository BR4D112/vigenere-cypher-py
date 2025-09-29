def vigenere_cipher(text, key, mode, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Encrypts or decrypts a text using the Vigenere cipher.

    Args:
        text: The text to encrypt or decrypt.
        key: The encryption or decryption key.
        mode: 'encrypt' or 'decrypt'.
        alphabet: The alphabet to use.

    Returns:
        The encrypted or decrypted text.
    """
    if not key:
        raise ValueError("Key must not be empty.")
    if not key.isalpha():
        
        raise ValueError("Key must contain only alphabetic characters.")
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'.")

    processed_text = ""
    key_index = 0
    
    text = text.upper()
    key = key.upper()

    for char in text:
        if char in alphabet:
            key_char = key[key_index % len(key)]
            key_shift = alphabet.index(key_char)
            text_shift = alphabet.index(char)

            if mode == 'encrypt':
                result_shift = (text_shift + key_shift) % len(alphabet)
            else: # decrypt
                result_shift = (text_shift - key_shift) % len(alphabet)
            
            processed_text += alphabet[result_shift]
            key_index += 1
        else:
            processed_text += char
            
    return processed_text