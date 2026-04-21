while True:
    print("=== MENU ===")
    print("1. halo")
    print("2. keluar")
    
    pilihan = int(input("pilih menu: "))

    if pilihan == 1:
        print("halo user")
    elif pilihan == 2:
        print("program berhenti")
        break
    else:
        print("pilihan tidak valid, coba lagi")
