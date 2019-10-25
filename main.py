from encrypt import generate_plaintext_ciphertext_pairs
import linear_approximation

print("Person 1 cryptanalysis")
round_keys_person_1 = [3049, 3492, 1038, 357, 6789]
pairs_person_1 = generate_plaintext_ciphertext_pairs(10000, round_keys_person_1, 0)
print(linear_approximation.exhaust_subkeys(pairs_person_1)[:10])


print("Person 2 cryptanalysis")
round_keys_person_2 = [4023, 234, 457, 1100, 9834]
pairs_person_2 = generate_plaintext_ciphertext_pairs(10000, round_keys_person_2, 20)
print(linear_approximation.exhaust_subkeys(pairs_person_2)[:10])

