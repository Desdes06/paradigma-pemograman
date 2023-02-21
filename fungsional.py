def input_a_dan_t():
    alas = float(input('Masukkan alas : '))
    tinggi = float(input('Masukkan tinggi : '))

    return alas, tinggi


def hitung_luas(alas, tinggi):
    return 0.5 * alas * tinggi

print(hitung_luas(9, 8))

alas, tinggi = input_a_dan_t()
print(hitung_luas(alas, tinggi))
