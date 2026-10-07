#!/usr/bin/env python3
# Ordezkapen sinpleko zifraketaren laguntzaile interaktiboa.
# Dokumentuko maiztasun-taularekin batera erabili.
#
# Ideia: zifratutako letra bakoitza plaintext-eko letra batekin mapatu.
# Adibidez: J -> E, I -> Z, etab.
#
# Programak uneko ordezkapena erakusten du eta erabiltzaileak aldaketak
# egin ditzake. Ez da komeni ordezkapen guztiak literalki probatzea:
# 26! aukera daude.

CIPHERTEXT = """JIYQ WQIEtYLP YtXLLW OPLP! CWXYM SPMQPLtP YEYQWtP CPOX PLZP SBPJPQX bPBQXWYtPQX bPtYPM. JYLYM bPW, XLPWM HYMCY PEQX PtYLPtJYM CP HPWJQWbYB WQIEtYLP; tRPBXPQ YtP tRPBXPQ, YtP «PISP, HPWJQWbYB!» XWFIPQ WJPM CWLP MPOIEW WbWBbWCY XEXPM. QPBY MPOIEWP YLY HPCP YJ CP BYFYM bYJPWM OPtPJQPtEIP, bPWMP, XLPWMCWQ YLY, JYMbPWt YZPQIZY OPJtYQ SPEPYLPM bWJQPLLP YZPM CWXtY HPWJQWbYBW, SPLtY FPLtJYP bPWZYMtJYM CWYM QXMSPWMWP bPQPLLPLW."""

def apply_mapping(text, mapping):
    out = []
    for ch in text:
        low = ch.lower()
        if low in mapping:
            new = mapping[low]
            out.append(new.upper() if ch.isupper() else new)
        else:
            out.append(ch)
    return ''.join(out)

def show_frequencies(text):
    counts = {}
    total = 0
    for ch in text.lower():
        if ch.isalpha() and ch.isascii():
            counts[ch] = counts.get(ch, 0) + 1
            total += 1
    print("\nMaiztasunak:")
    for ch, n in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ch}: {n:3d} ({100*n/total:5.2f}%)")

mapping = {}

while True:
    print("\n--- ORDEZKAPEN SINPLEA ---")
    print("1) Maiztasunak erakutsi")
    print("2) Ordezkapena gehitu/aldatu")
    print("3) Uneko deskodetzea erakutsi")
    print("4) Ordezkapen guztiak erakutsi")
    print("5) Amaitu")

    option = input("Aukera: ").strip()

    if option == "1":
        show_frequencies(CIPHERTEXT)

    elif option == "2":
        src = input("Zifratutako letra (adib. J): ").strip().lower()
        dst = input("Jatorrizko letra (adib. e): ").strip().lower()

        if len(src) != 1 or not src.isalpha() or len(dst) != 1 or not dst.isalpha():
            print("Sartu letra bana.")
            continue

        mapping[src] = dst
        print(f"{src} -> {dst} gehitu da.")

    elif option == "3":
        print("\n" + apply_mapping(CIPHERTEXT, mapping))

    elif option == "4":
        if not mapping:
            print("Oraindik ez dago ordezkapenik.")
        else:
            print(" ".join(f"{a}->{b}" for a, b in sorted(mapping.items())))

    elif option == "5":
        break

    else:
        print("Aukera okerra.")
