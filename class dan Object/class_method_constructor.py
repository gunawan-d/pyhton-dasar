# Membuat class cat dengan property dan menambahkan method constructor
# Kita akan menambahkan method constructor untuk mengubah nilai dari properti color
class cat:
    color = "black"

    def __init__(self, color):
        self.color = color

# Membuat objek baru
cat1 = cat("orange")
print(cat1.color) # orange