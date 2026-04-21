while True:
    angka = int(input("masukkan angka positif: "))
    
    if angka >= 0:
        break
    else:
        print("input salah, harus angka positif.")

print("angka yang dimasukkan:", angka)
