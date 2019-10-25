from encrypt import generate_plaintext_ciphertext_pairs

round_keys = [3049, 3492, 1038, 357, 6789]
pairs = generate_plaintext_ciphertext_pairs(10000, round_keys)
print(pairs)
