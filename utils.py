import random


def generate_key():
    key = ''
    for i in range(16):
        bit = random.randint(0, 1)
        key += str(bit)

    return key


def sub_linear_approximation(input_sum, output_sum):
    equation_satisfaction_count = 0
    for i in range(16):
        and_product = input_sum & i
        str_product = str(and_product)[2:len(and_product)]


def calculate_xor_sum(binary_string):
    xor_sum = 0
    for bit in binary_string:
        xor_sum = xor_sum ^ bit

    return xor_sum


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
