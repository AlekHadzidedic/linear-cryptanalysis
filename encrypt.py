import random

from linear_approximation import s_box_encrypt
from utils import binary_splice


def encrypt(plaintext, round_keys):
    num_rounds = 5
    temp_plaintext = plaintext
    rounds_counter = 0
    for i in range(num_rounds - 2):
        # 1 XOR Plaintext with First round key
        v = key_xor(temp_plaintext, round_keys[rounds_counter])

        # 2 Substitute each bye
        u = substitute_16_bit(v)

        # 3 Permutate binary string
        w = permutate(u)

        temp_plaintext = w

        rounds_counter += 1

    # Round 4 (no permutation)
    a = key_xor(temp_plaintext, round_keys[rounds_counter])
    b = substitute_16_bit(a)

    # Round 5 (xor with K5)
    rounds_counter += 1
    c = key_xor(int(f'0b{b}', 2), round_keys[rounds_counter])

    c_string = ""
    for i in range(len(c)):
        c_string += binary_splice(bin(c[i]), 4)

    return c_string


def substitute_16_bit(v):
    substituted_string = ""
    for i in range(len(v)):
        substituted_string += binary_splice(bin(s_box_encrypt(v[i])), 4)

    return substituted_string


def key_xor(plaintext, key):
    xor_sum = plaintext ^ key
    bin_num = binary_splice(bin(xor_sum), 16)
    s_box_partition = []

    for i in range(4):
        s_box_partition.append(int('0b' + bin_num[4 * i:4 * (i + 1)], 2))

    return s_box_partition


def permutate(ciphertext):
    ciphertext_list = list(ciphertext)
    permutation_map = {0: 0, 1: 4, 2: 8, 3: 12, 4: 1, 5: 5, 6: 9, 7: 13}

    for i in range(8):
        temp = ciphertext_list[i]
        ciphertext_list[i] = ciphertext_list[permutation_map[i]]
        ciphertext_list[permutation_map[i]] = temp

    return int('0b' + ''.join(ciphertext_list), 2)


def generate_plaintext_ciphertext_pairs(n, round_keys):
    plaintext_sample = random.sample(range(1, 2 ** 16), n)
    pairs = []

    for plaintext in plaintext_sample:
        pairs.append((binary_splice(bin(plaintext), 16), encrypt(plaintext, round_keys)))

    return pairs
