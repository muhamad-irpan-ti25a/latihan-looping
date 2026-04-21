while True:
    angka = int(input("Masukkan angka positif: "))
    
    if angka >= 0:
        break
    else:
        print("Input salah! Harus angka positif.")

print("Angka yang dimasukkan:", angka)