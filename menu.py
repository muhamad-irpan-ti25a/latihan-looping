while True:
    print("=== MENU ===")
    print("1. Halo")
    print("2. Keluar")
    
    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        print("Halo User")
    elif pilihan == 2:
        print("Program berhenti")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")