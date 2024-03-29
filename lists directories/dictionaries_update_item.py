firstPerson = {
    "first_name": "Gunawan",
    "last_name":  "Dwi Cahyo",
    "age": 23

}

# Ada 2 cara untuk mengubah atau mengupdate sebuah value dari item pada Dictionaries

# Cara Pertama
firstPerson['age'] = 23

# Cara Kedua dengan method "update"
# Jika kita menggunakan cara ini, ketika item yang di update berdasarkan key (age) ditemukan,
# maka akan diupdate.
# Namun jika item belum ada, maka otomatis akan menambahkan item baru
firstPerson.update({"age": 23})

firstPerson.update({"hair_color": "black"})
print(firstPerson)  # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 15, 'hair_color': 'black'}
