# Laborategia - Zifraketa simetrikoa

Laborategiko programak:

- `01_caesar_bruteforce.py` — Caesar-en indar-erasoa.
- `02_substitution_bruteforce.py` — ordezkapen sinplearen analisi interaktiboa.
- `03_xor_flux.py` — XOR bidezko fluxu-zifraketa.
- `04_openssl.sh` — AES, 3DES eta DES zifratu/deszifratu OpenSSL erabiliz.

## Exekutatu

```bash
python3 01_caesar_bruteforce.py
python3 02_substitution_bruteforce.py
python3 03_xor_flux.py

chmod +x 04_openssl.sh
./04_openssl.sh
```

## OpenSSL

Ubuntu-n:

```bash
sudo apt update
sudo apt install openssl
```

`04_openssl.sh` script-ak `mezua.txt` eta `gako.txt` sortzen ditu eta ondoren AES-256-CBC, Triple DES eta DES probatzen ditu.

## GitHub

```bash
git init
git add .
git commit -m "Laborategiko zifraketa programak"
git branch -M main
git remote add origin https://github.com/ERABILTZAILEA/ERREPOSITORIOA.git
git push -u origin main
```
