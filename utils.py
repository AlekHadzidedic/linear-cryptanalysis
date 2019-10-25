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
    mapping = [12, 6, 0, 4, 11, 8, 2, 13, 1, 15, 7, 5, 14, 3, 9, 10]
    return mapping[x]


def s_box_decrypt(y):
    mapping = [2, 8, 6, 13, 3, 11, 1, 10, 5, 14, 15, 4, 0, 7, 12, 9]
    return mapping[y]


def construct_linear_approximation():
    return [[construct_sub_linear_approximation(i, j) for j in range(16)] for i in range(16)]


def binary_splice(bin_num, padding):
    return bin_num[2:].zfill(padding)





