#!/usr/bin/env bash
set -e

# Laborategiko mezua eta pasahitza sortu
printf '%s\n' 'Kriptografiak konfidentzialtasuna bermatzen du' > mezua.txt
printf '%s\n' 'Laborategi2026' > gako.txt

echo "=== AES-256-CBC ==="
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt \
  -in mezua.txt -out mezua.aes -pass file:gako.txt

openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 \
  -in mezua.aes -out mezua.aes.deszifratua -pass file:gako.txt

cmp mezua.txt mezua.aes.deszifratua
echo "AES: OK"

echo "=== Triple DES ==="
openssl enc -des-ede3-cbc -provider default -provider legacy -pbkdf2 \
  -iter 100000 -salt -in mezua.txt -out mezua.3des \
  -pass file:gako.txt

openssl enc -d -des-ede3-cbc -provider default -provider legacy -pbkdf2 \
  -iter 100000 -in mezua.3des -out mezua.3des.deszifratua \
  -pass file:gako.txt

cmp mezua.txt mezua.3des.deszifratua
echo "3DES: OK"

echo "=== DES ==="
openssl enc -des-cbc -provider default -provider legacy -pbkdf2 \
  -iter 100000 -salt -in mezua.txt -out mezua.des \
  -pass file:gako.txt

openssl enc -d -des-cbc -provider default -provider legacy -pbkdf2 \
  -iter 100000 -in mezua.des -out mezua.des.deszifratua \
  -pass file:gako.txt

cmp mezua.txt mezua.des.deszifratua
echo "DES: OK"

echo "=== SHA-256 ==="
sha256sum mezua.txt mezua.aes mezua.3des mezua.des
sha256sum mezua.aes.deszifratua mezua.3des.deszifratua mezua.des.deszifratua

echo "Laborategia amaituta."
