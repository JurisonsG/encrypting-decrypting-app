def textToencrypt(text, key):
    if not text or not key:
        return ""
    
    key_len = len(key)
    result_lines = []
    
    for line in text.splitlines():
        result = ""
        for i, c in enumerate(line):
            if c == "\n":
                result += "\n"
                continue
            key_c = key[i % key_len]
            encrypted_char = chr(ord(c) ^ ord(key_c))
            result += format(ord(encrypted_char), '08b') + " "
        result_lines.append(result.strip())
    
    return "\n".join(result_lines)
