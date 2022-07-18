# Menghentikan perulangan jika nilai x adalah 3
# Pada kode dibawah ini, jika nilai x sama dengan 3,
# Maka perulangan akan dihentikan, walaupun seharusnya
# Perulangan akan berhenti setelah 5 kali berjalan
for x in range(10):
    print(x)
    if x == 9:
        break