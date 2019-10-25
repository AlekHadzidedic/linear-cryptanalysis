import random


def generate_key():
    key = ''
    for i in range(16):
        bit = random.randint(0, 1)
        key += str(bit)

    return key


def key_xor(plaintext, key):
    xor_sum = plaintext ^ key
    bin_num = binary_splice(bin(xor_sum), 16)
    s_box_partition = []

    for i in range(4):
        s_box_partition.append(int('0b' + bin_num[4*i:4*(i + 1)], 2))

    return s_box_partition


def permutate(ciphertext):
    ciphertext_list = list(ciphertext)
    permutation_map = {0: 0, 1: 4, 2: 8, 3: 12, 4: 1, 5: 5, 6: 9, 7: 13}

    for i in range(len(ciphertext_list)):
        temp = ciphertext_list[i]
        ciphertext_list[i] = ciphertext_list[permutation_map[i]]
        ciphertext_list[permutation_map[i]] = temp

    return int('0b' + ''.join(ciphertext_list), 2)


def construct_sub_linear_approximation(input_sum, output_sum):
    equation_satisfaction_count = 0
    for i in range(16):
        and_product_input = input_sum & i
        and_product_input = bin(and_product_input)
        str_product_input = binary_splice(and_product_input, 4)

        output_mapping = s_box_encrypt(i)
        and_product_output = output_sum & output_mapping
        and_product_output = bin(and_product_output)
        str_product_output = binary_splice(and_product_output, 4)

        input_xor_sum = calculate_xor_sum(str_product_input)
        output_xor_sum = calculate_xor_sum(str_product_output)

        if input_xor_sum == output_xor_sum:
            equation_satisfaction_count += 1

    return equation_satisfaction_count - 8


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


def construct_linear_approximation():
    return [[construct_sub_linear_approximation(i, j) for j in range(16)] for i in range(16)]


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


def binary_splice(bin_num, padding):
    return bin_num[2:].zfill(padding)


def encrypt(plaintext, round_keys):
    # 1 XOR Plaintext with First round key
    # 2 Substitute each bye
    return


def substitute_16_bit():
    substituted_string = ""
    for i in range(4):
        substituted_string += binary_splice(bin(s_box_encrypt(i)), 4)
    print(substituted_string)
