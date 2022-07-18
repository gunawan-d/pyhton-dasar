# Melewati perulangan jika nilai x adalah genap (2,4,6 dan seterusnya)
# Pada kode dibawah ini, hanya akan mencetak angka ganjil
# Karena jika angka adalah genap, maka proses mencetak akan
# Kita skip menggunakan keywork "Continue"

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)