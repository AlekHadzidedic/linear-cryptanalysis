def calculate_xor_sum(binary_string):
    xor_sum = 0
    for bit in binary_string:
        xor_sum = xor_sum ^ int(bit)

    return xor_sum


def binary_splice(bin_num, padding):
    return bin_num[2:].zfill(padding)
