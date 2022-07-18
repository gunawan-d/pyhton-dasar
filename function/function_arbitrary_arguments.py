#Membuat Function dengan nama belajar_python
#yang memiliki Arbitrart Arguments dengan nama "names"
def belajar_python(*names):
    for name in names:
        print("Hallo, Saya %s" % name)

# Karena Function di atas memiliki Arbitrary Arguments, 
# maka kita bisa mengirimkan banyak value sebagai Arguments ke dalam Function tersebut
belajar_python("Gunawan", "Dwi Cahyo", "no")