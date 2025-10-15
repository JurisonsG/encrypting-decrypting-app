def window(root, x, y, title):

    size = str(x) + "x" + str(y)

    root.geometry(size)

    root.title(title)

    root.config()

def closeWindow(root):
    root.destroy()

def createFile(text, filename):

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def bytes_to_bitstring(data):
    """
    Pārvērš bytes objektu par bitu stringu '01001101...'.
    data: baitu virkne
    return: bitu string
    """
    return ''.join(f'{byte:08b}' for byte in data)


def bitstring_to_bytes(bitstring):
    """
    Pārvērš bitu stringu '01001101...' uz bytes objektu.
    bitstring: string, garums %8 == 0
    return: bytes
    """
    if len(bitstring) % 8 != 0:
        raise ValueError("Bitu stringa garumam jābūt dalāmam ar 8")
    
    data = bytearray()
    for i in range(0, len(bitstring), 8):
        byte_str = bitstring[i:i+8]
        byte = int(byte_str, 2)
        data.append(byte)
    return bytes(data)
