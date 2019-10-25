from utils import binary_splice, calculate_xor_sum


def s_box_encrypt(x):
    mapping = [12, 6, 0, 4, 11, 8, 2, 13, 1, 15, 7, 5, 14, 3, 9, 10]
    return mapping[x]


def s_box_decrypt(y):
    mapping = [2, 8, 6, 13, 3, 11, 1, 10, 5, 14, 15, 4, 0, 7, 12, 9]
    return mapping[y]


def construct_linear_approximation():
    return [[construct_sub_linear_approximation(i, j) for j in range(16)] for i in range(16)]


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


def exhaust_subkeys(pairs):
    table = []
    for key in range(256):
        bin_str = binary_splice(bin(key), 8)
        partial_key_1 = bin_str[0:4]
        partial_key_2 = bin_str[4:]

        counter = 0
        for pair in pairs:
            partial_ct_1 = pair[1][0:4]
            partial_ct_2 = pair[1][12:]

            pt_1 = int('0b' + partial_ct_1, 2) ^ int('0b' + partial_key_1, 2)
            pt_2 = int('0b' + partial_ct_2, 2) ^ int('0b' + partial_key_2, 2)

            eq_val_1 = s_box_decrypt(pt_1)
            eq_val_2 = s_box_decrypt(pt_2)

            x1 = binary_splice(bin(eq_val_1), 4)
            x2 = binary_splice(bin(eq_val_2), 4)

            equation = x1[0] + x1[3] + x2[0] + x2[3] + pair[0][1]

            xor_sum = calculate_xor_sum(equation)

            if xor_sum == 0:
                counter += 1

        bias = (counter - 5000)/10000
        table.append((binary_splice(bin(key), 8), counter, bias))

    table.sort(key=lambda tup: tup[2], reverse=True)
    return table
