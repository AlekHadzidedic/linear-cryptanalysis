from encrypt import generate_plaintext_ciphertext_pairs
import linear_approximation

round_keys = [3049, 3492, 1038, 357, 6789]
pairs = generate_plaintext_ciphertext_pairs(10000, round_keys)
#print(pairs)

print(linear_approximation.construct_linear_approximation())

print(linear_approximation.exhaust_subkeys(pairs))

