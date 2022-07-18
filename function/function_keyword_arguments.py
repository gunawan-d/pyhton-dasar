def belajar_python(name, age):
    print("Hallo, Saya %s, Umur Saya %d" % (name, age))
# Contoh Function di atas. Jika kita memanggil Function dan mengirim Arguments tanpa nama "key" nya
# maka kita harus menuliskannya secara berurutan (name, age)

belajar_python("Gunawan", 23) # Hallo, saya rizki. umur saya 23

# Tetapi jika kira memanggil FUnction dan mengirim Arguments dengan nama "key" nya
# maka kita tidak harus menuliskanya secara beruntun (age, name)
belajar_python(age = 23, name="gunawan")