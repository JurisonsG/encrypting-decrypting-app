def cryptToText(bText, key):
    if not bText or not key:
        return ""
    
    key_len = len(key)
    result = ""

    lines = bText.split("\n")

    for line_idx, line in enumerate(lines):
        if not line.strip():
            result += "\n"
            continue

        bchars = line.strip().split(" ")
        decrypted_line = ""

        for i, c in enumerate(bchars):
            if not c:
                continue

            encrypted_char = chr(int(c, 2))
            key_c = key[i % key_len]
            decrypted_char = chr(ord(encrypted_char) ^ ord(key_c))
            decrypted_line += decrypted_char

        result += decrypted_line
        if line_idx < len(lines) - 1:
            result += "\n"

    return result
