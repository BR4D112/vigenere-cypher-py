def vigenere_cipher(text, key, mode, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if not key:
        raise ValueError("La llave no puede estar vacía.")
    if not key.isalpha():
        
        raise ValueError("La llave debe contener solo letras.")
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("El modo debe ser 'encrypt' o 'decrypt'.")

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