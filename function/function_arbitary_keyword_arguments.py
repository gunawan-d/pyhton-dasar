def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

#memanggil function belajar_python dengan arbitrary keyworkd arguments
belajar_python(age=23, name="Gunawan") #hallo, saya gunawan, umur saya 23