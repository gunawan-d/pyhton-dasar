# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
    "first_name": "Gunawan",
    "last_name": "Dwi Cahyo",
    "age": 10

}
# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name'])
# Cara kedua dengan method "get"
print(firstPerson.get('age'))

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['name','age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values())

