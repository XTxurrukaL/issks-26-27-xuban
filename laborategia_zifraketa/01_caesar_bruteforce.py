#!/usr/bin/env python3
# Caesar zifratuaren indar-erasoa.
# Gaztelaniarako maiztasun-analisia erabiliz gako probableena aurkitzen du.

import string

CIPHERTEXT = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

# Gutxi gorabeherako letra-maiztasunak gaztelaniaz.
FREQ_ES = {
    'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586,
    'e': 0.1368, 'f': 0.0069, 'g': 0.0101, 'h': 0.0070,
    'i': 0.0625, 'j': 0.0044, 'k': 0.0002, 'l': 0.0497,
    'm': 0.0315, 'n': 0.0671, 'ñ': 0.0031, 'o': 0.0868,
    'p': 0.0251, 'q': 0.0088, 'r': 0.0687, 's': 0.0798,
    't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001,
    'x': 0.0022, 'y': 0.0090, 'z': 0.0052
}

ALPHABET = string.ascii_lowercase

def decrypt(text, key):
    result = []
    for ch in text:
        low = ch.lower()
        if low in ALPHABET:
            dec = ALPHABET[(ALPHABET.index(low) - key) % 26]
            result.append(dec.upper() if ch.isupper() else dec)
        else:
            result.append(ch)
    return ''.join(result)

def chi_square(text):
    letters = [c.lower() for c in text if c.lower() in ALPHABET]
    n = len(letters)
    if n == 0:
        return float("inf")

    counts = {c: letters.count(c) for c in ALPHABET}
    score = 0.0

    # ñ ez da Caesar alfabetoan sartzen; gainerako letrak normalizatuta.
    total_freq = sum(FREQ_ES[c] for c in ALPHABET)
    for c in ALPHABET:
        expected = n * (FREQ_ES[c] / total_freq)
        if expected > 0:
            score += (counts[c] - expected) ** 2 / expected
    return score

candidates = []
for key in range(26):
    plaintext = decrypt(CIPHERTEXT, key)
    candidates.append((chi_square(plaintext), key, plaintext))

candidates.sort()

print("5 aukera probableenak:\n")
for score, key, plaintext in candidates[:5]:
    print(f"Gakoa {key:2d} | puntuazioa {score:8.2f} | {plaintext}")

best = candidates[0]
print("\nGako probableena:", best[1])
print("Mezua:", best[2])
