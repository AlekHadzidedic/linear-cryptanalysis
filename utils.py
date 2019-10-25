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
        and_product_input = input_sum & i
        str_product_input = str(and_product_input)[2:len(and_product_input)]

        output_mapping = s_box_encrypt(i)
        and_product_output = output_sum & output_mapping
        str_product_output = str(and_product_output)[2:len(and_product_output)]

        input_xor_sum = calculate_xor_sum(str_product_input)
        output_xor_sum = calculate_xor_sum(str_product_output)

        if input_xor_sum == output_xor_sum:
            equation_satisfaction_count += 1

    return equation_satisfaction_count


def calculate_xor_sum(binary_string):
    xor_sum = 0
    for bit in binary_string:
        xor_sum = xor_sum ^ int(bit)

    return xor_sum


def s_box_encrypt(x):
    mapping = [
        12,
        6,
        0,
        4,
        11,
        8,
        2,
        13,
        1,
        15,
        7,
        5,
        14,
        3,
        9,
        10
    ]

    return mapping[x]


def s_box_decrypt(y):
    mapping = [
        2,
        8,
        6,
        13,
        3,
        11,
        1,
        10,
        5,
        14,
        15,
        4,
        0,
        7,
        12,
        9
    ]

    return mapping[y]


def linear_approximation():
    return [[sub_linear_approximation(i, j) for i in range(16)] for j in range(16)]


def s_box_encrypt_temp(x):
    mapping = [
        14,
        4,
        13,
        1,
        2,
        15,
        11,
        8,
        3,
        10,
        6,
        12,
        5,
        9,
        0,
        7
    ]

    return mapping[x]


def s_box_decrypt_temp(y):
    mapping = [
        14,
        3,
        4,
        8,
        1,
        12,
        10,
        15,
        7,
        13,
        9,
        6,
        11,
        2,
        0,
        5
    ]

    return mapping[y]

