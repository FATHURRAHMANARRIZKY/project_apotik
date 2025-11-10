obat = [
    ["OB001", "Paracetamol", 5000, 10],
    ["OB002", "Amoxicillin", 12000, 8],
    ["OB003", "Vitamin C", 8000, 15],
    ["OB004", "OBH Combi", 10000, 5]
]

layanan_kesehatan = [
    ["LK001", "Cek Tekanan Darah", 15000],
    ["LK002", "Cek Kolesterol", 25000],
    ["LK003", "Konsultasi Dokter", 30000]
]

vaksinasi = [
    ["V001", "Vaksin Influenza", 80000],
    ["V002", "Vaksin Covid-19", 120000],
    ["V003", "Vaksin Hepatitis", 100000]
]

konsultasi = [
    ["K001", "Konsultasi Obat Ringan", 10000],
    ["K002", "Konsultasi Obat Kronis", 20000],
    ["K003", "Konsultasi Anak", 15000]
]

transaksi = []
pasien_list = []
total_pendapatan = 0

menu = ""
while menu != "7":
    print("=" * 60)
    print("\t\tAPOTEK GIRSANG - LAYANAN & PENJUALAN")
    print("=" * 60)
    print("1. Konsultasi Obat")
    print("2. Penjualan Obat")
    print("3. Layanan Kesehatan & Pemeriksaan")
    print("4. Layanan Vaksinasi")
    print("5. Laporan Transaksi & Data Pasien")
    print("6. Tambah / Cek Stok Obat")
    print("7. Keluar")
    print("=" * 60)
    menu = input("Pilih menu: ")

    if menu == "1":
        print("\n=== INPUT DATA PASIEN ===")
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])

        print("\n=== LAYANAN KONSULTASI ===")
        print("Kode\tNama Layanan\t\tHarga")
        print("-" * 50)
        for k in konsultasi:
            print(k[0], "\t", k[1], "\t", k[2])
        kode = input("\nMasukkan kode konsultasi: ")

        ditemukan = 0
        for k in konsultasi:
            if k[0] == kode:
                status = input("Apakah Member? (y/n): ")
                total = k[2]
                if status == "y":
                    total = total - (total * 0.1)
                    print("Diskon member 10% diterapkan.")
                transaksi.append([nama, k[1], 1, total])
                total_pendapatan += total

                print("\n===================================")
                print("           STRUK KONSULTASI        ")
                print("===================================")
                print("Nama Pasien :", nama)
                print("Umur         :", umur)
                print("Keluhan      :", keluhan)
                print("Layanan      :", k[1])
                print("Total Bayar  : Rp", total)
                print("===================================")
                print("Terima kasih telah berkunjung!\n\n")
                print("Tekan 0 untuk kembali ke menu utama.")
                kembali = input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode konsultasi tidak ditemukan.")

    elif menu == "2":
        print("\n=== PENJUALAN OBAT ===")
        print("Kode\tNama Obat\t\tHarga\tStok")
        print("-" * 50)
        for o in obat:
            print(o[0], "\t", o[1], "\t\t", o[2], "\t", o[3])

        kode = input("\nMasukkan kode obat: ")
        ditemukan = 0
        for o in obat:
            if o[0] == kode:
                nama = input("Nama Pembeli: ")
                status = input("Apakah Member? (y/n): ")
                jumlah = int(input("Jumlah beli: "))

                if jumlah > o[3]:
                    print("Stok tidak cukup! Sisa stok:", o[3])
                else:
                    total = jumlah * o[2]
                    if total > 100000:
                        print("Diskon 5% untuk pembelian di atas Rp100.000")
                        total = total - (total * 0.05)
                    if status == "y":
                        print("Diskon member 10% diterapkan.")
                        total = total - (total * 0.1)

                    o[3] -= jumlah
                    transaksi.append([nama, o[1], jumlah, total])
                    total_pendapatan += total

                    print("\n===================================")
                    print("            STRUK PEMBELIAN        ")
                    print("===================================")
                    print("Nama Pembeli :", nama)
                    print("Obat Dibeli  :", o[1])
                    print("Jumlah       :", jumlah)
                    print("Total Bayar  : Rp", total)
                    print("Sisa Stok    :", o[3])
                    print("===================================")
                    print("Terima kasih telah berbelanja!\n\n")
                    print("Tekan 0 untuk kembali ke menu utama.")
                    kembali = input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode obat tidak ditemukan.")

    elif menu == "3":
        print("\n=== INPUT DATA PASIEN ===")
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])

        print("\n=== LAYANAN KESEHATAN ===")
        print("Kode\tNama Pemeriksaan\t\tHarga")
        print("-" * 50)
        for l in layanan_kesehatan:
            print(l[0], "\t", l[1], "\t\t", l[2])
        kode = input("\nMasukkan kode layanan: ")

        ditemukan = 0
        for l in layanan_kesehatan:
            if l[0] == kode:
                status = input("Apakah Member? (y/n): ")
                total = l[2]
                if status == "y":
                    total = total - (total * 0.1)
                    print("Diskon member 10% diterapkan.")
                transaksi.append([nama, l[1], 1, total])
                total_pendapatan += total

                print("\n===================================")
                print("         STRUK PEMERIKSAAN         ")
                print("===================================")
                print("Nama Pasien :", nama)
                print("Umur         :", umur)
                print("Layanan      :", l[1])
                print("Total Bayar  : Rp", total)
                print("===================================")
                print("Terima kasih telah menggunakan layanan!\n\n")
                print("Tekan 0 untuk kembali ke menu utama.")
                kembali = input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode layanan tidak ditemukan.")

    elif menu == "4":
        print("\n=== INPUT DATA PASIEN ===")
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])

        print("\n=== LAYANAN VAKSINASI ===")
        print("Kode\tJenis Vaksin\t\tHarga")
        print("-" * 50)
        for v in vaksinasi:
            print(v[0], "\t", v[1], "\t\t", v[2])
        kode = input("\nMasukkan kode vaksin: ")

        ditemukan = 0
        for v in vaksinasi:
            if v[0] == kode:
                status = input("Apakah Member? (y/n): ")
                total = v[2]
                if status == "y":
                    total = total - (total * 0.1)
                    print("Diskon member 10% diterapkan.")
                transaksi.append([nama, v[1], 1, total])
                total_pendapatan += total

                print("\n===================================")
                print("           STRUK VAKSINASI         ")
                print("===================================")
                print("Nama Pasien :", nama)
                print("Umur         :", umur)
                print("Jenis Vaksin :", v[1])
                print("Total Bayar  : Rp", total)
                print("===================================")
                print("Terima kasih telah vaksinasi di Apotek Girsang!\n\n")
                print("Tekan 0 untuk kembali ke menu utama.")
                kembali = input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode vaksin tidak ditemukan.")

    elif menu == "5":
        print("\n=== LAPORAN TRANSAKSI & DATA PASIEN ===")
        print("-" * 60)
        print("Nama\t\tLayanan/Obat\t\tJumlah\tTotal")
        for t in transaksi:
            print(t[0], "\t", t[1], "\t", t[2], "\tRp", t[3])
        print("-" * 60)
        print("Total Pendapatan Hari Ini: Rp", total_pendapatan)
        print("-" * 60)
        print("\nData Pasien:")
        for p in pasien_list:
            print("-", p[0], "(", p[1], "th ) |", p[3], "|", p[4], "kg /", p[5], "cm")

    elif menu == "6":
        print("\n=== CEK / TAMBAH STOK OBAT ===")
        print("Kode\tNama Obat\tStok")
        print("-" * 40)
        for o in obat:
            print(o[0], "\t", o[1], "\t", o[3])
        print("-" * 40)
        sub = input("Tambah stok obat? (y/n): ")
        if sub == "y":
            kode = input("Masukkan kode obat: ")
            ditemukan = 0
            for o in obat:
                if o[0] == kode:
                    tambahan = int(input("Tambah stok: "))
                    o[3] += tambahan
                    print("Stok obat", o[1], "sekarang:", o[3])
                    ditemukan = 1
                    break
            if ditemukan == 0:
                print("Kode obat tidak ditemukan.")

    elif menu == "7":
        print("\n=== TERIMA KASIH ===")
        print("Total pendapatan hari ini: Rp", total_pendapatan)
        print("Sampai jumpa kembali!\n")

    else:
        print("Pilihan tidak valid, coba lagi!\n")