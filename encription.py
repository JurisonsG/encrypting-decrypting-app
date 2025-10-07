def textToencrypt(text, key):
    if not text or not key:
        return ""
    
    key_len = len(key)
    result = ""
    
    for i, c in enumerate(text):
        key_c = key[i % key_len]
        # XOR operācija starp simbolu un atslēgas simbolu
        encrypted_char = chr(ord(c) ^ ord(key_c))
        # Pārvēršam katru simbolu binārā 8 bitu formātā
        result += format(ord(encrypted_char), '08b') + " "
    
    return result.strip()

def createFile(text, filename):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
