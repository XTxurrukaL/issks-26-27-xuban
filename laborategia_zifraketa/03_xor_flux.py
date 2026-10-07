#!/usr/bin/env python3
# XOR bidezko fluxu-zifraketa sinplea.
# Laborategiko datuak erabiliz:
# Mezua: GURE MEZUA HAU DA
# Gakoa: GAKO1234567890

def xor_bytes(data, key):
    if len(data) != len(key):
        raise ValueError("Mezuak eta gakoak byte luzera bera izan behar dute.")
    return bytes(a ^ b for a, b in zip(data, key))

message = "GURE MEZUA HAU DA"
key = "GAKO1234567890"

message_bytes = message.encode("utf-8")
key_bytes = key.encode("utf-8")

cipher = xor_bytes(message_bytes, key_bytes)
decoded = xor_bytes(cipher, key_bytes)

print("Jatorrizko mezua :", message)
print("Gakoa            :", key)
print("Mezua HEX        :", message_bytes.hex())
print("Gakoa HEX        :", key_bytes.hex())
print("Kriptograma HEX  :", cipher.hex())
print("Deszifratutako HEX:", decoded.hex())
print("Deszifratutako mezua:", decoded.decode("utf-8"))
print("Egiaztapena:", "OK" if decoded == message_bytes else "ERROREA")
