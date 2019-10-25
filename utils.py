import random


def generate_key():
    key = ''
    for i in range(16):
        bit = random.randint(0, 1)
        key += str(bit)

    return key


def s_box_encrypt(binary_input):
    mapping = [
        bin(12),
        bin(6),
        bin(0),
        bin(4),
        bin(11),
        bin(8),
        bin(2),
        bin(13),
        bin(1),
        bin(15),
        bin(7),
        bin(5),
        bin(14),
        bin(3),
        bin(9),
        bin(10)
    ]

    return mapping[int(binary_input, 2)]


def s_box_decrypt(binary_input):
    mapping = [
        bin(2),
        bin(8),
        bin(6),
        bin(13),
        bin(3),
        bin(11),
        bin(1),
        bin(10),
        bin(5),
        bin(14),
        bin(15),
        bin(4),
        bin(0),
        bin(7),
        bin(12),
        bin(9)
    ]

    return mapping[int(binary_input, 2)]
