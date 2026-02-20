# This module contains the formulas built to answer tasks 7 - 8.
# See ReadMe.md for references used.

def move_over_encrypt(word: str, key: int) -> str:
    # This holds the logic for task 7. It will utilize "move over" encryption by shifting the characters.
    # It will shift everything in place as if 'K' were the first letter of the alphabet.
    n = len(word)
    k = key % n
    if k == 0:
        return word
    else:
        return word[-k:] + word[:-k]

def skip_ahead_encrypt(word: str, key: int) -> str:
    # This holds the logic for task 8.
    # It will operate by reording characters into a new list, while jumping forward by defined positions.
    # Will utilize wrapping with modulo for the key.
    n = len(word)
    cipher = [""] * n
    idx = 0
    for ch in word:
        cipher[idx] = ch
        idx = (idx + key) % n
    return "".join(cipher)

