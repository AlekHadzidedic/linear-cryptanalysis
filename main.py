from encrypt import encrypt

plain_text = 34859
round_keys = [3049, 3492, 1038, 357, 6789]

x = encrypt(plain_text, round_keys)
