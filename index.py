obat = [
    ["OB001", "Paracetamol", 5000, 10],
    ["OB002", "Amoxicillin", 12000, 8],
    ["OB003", "Vitamin C", 8000, 15],
    ["OB004", "OBH Combi", 10000, 5],
    ["OB005", "Promag", 7000, 12],
    ["OB006", "Bodrex", 6000, 20],
    ["OB007", "Panadol Extra", 9000, 10],
    ["OB008", "Antasida DOEN", 5000, 7],
    ["OB009", "CTM\t", 4000, 25]
]

layanan_kesehatan = [
    ["LK001", "Cek Tekanan Darah\t\t\t", 15000],
    ["LK002", "Cek Kolesterol\t\t\t\t", 25000],
    ["LK003", "Konsultasi Dokter\t\t\t", 30000],
    ["LK004", "Cek Gula Darah\t\t\t\t", 20000],
    ["LK005", "Cek Asam Urat\t\t\t\t", 18000],
    ["LK006", "Cek Hemoglobin (HB)\t\t\t", 22000],
    ["LK007", "Cek BMI (Berat & Tinggi Badan)\t\t", 10000]
]

vaksinasi = [
    ["V001", "Vaksin Influenza\t\t", 80000],
    ["V002", "Vaksin Covid-19\t\t", 120000],
    ["V003", "Vaksin Hepatitis\t\t", 100000],
    ["V004", "Vaksin Tetanus\t\t\t", 90000],
    ["V005", "Vaksin HPV\t\t\t", 150000],
    ["V006", "Vaksin Rabies\t\t\t", 110000],
    ["V007", "Vaksin MR (Campak Rubella)\t", 95000]
]

konsultasi = [
    ["K001", "Konsultasi Obat Ringan", 10000],
    ["K002", "Konsultasi Obat Kronis", 20000],
    ["K003", "Konsultasi Anak\t", 15000],
    ["K004", "Konsultasi Ibu Hamil\t", 25000],
    ["K005", "Konsultasi Gizi & Nutrisi", 30000],
    ["K006", "Konsultasi Kesehatan Mental", 35000],
    ["K007", "Konsultasi Lansia\t", 20000]
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
        print("\n","="*10,"INPUT DATA PASIEN","="*10)
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])
        
        print("\n")
        print("     ","="*10,"LAYANAN KONSULTASI","="*10)
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
                diskon = 0

                if status == "y" and total >= 100000:
                    diskon = total * 0.1
                    print("Diskon member 10% diterapkan (≥100.000).")
                elif status == "n" and total >= 200000:
                    diskon = total * 0.1
                    print("Diskon 10% diterapkan untuk non-member (≥200.000).")

                total -= diskon
                transaksi.append([nama, k[1], 1, total])
                total_pendapatan += total
                print("\n")
                print("="*50)
                print("\t\tSTRUK KONSULTASI")
                print("="*50)
                print("Nama Pasien  :", nama)
                print("Keluhan      :", keluhan)
                print("Layanan      :", k[1])
                print("Diskon       : Rp", int(diskon))
                print("Total Bayar  : Rp", int(total))
                print("\n","="*50)
                print("Terima kasih telah berkonsultasi!\n")
                print("Tekan 0 untuk kembali ke menu utama...")
                input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode konsultasi tidak ditemukan.")

    elif menu == "2":
        print("\n")
        print("     ","="*10,"PENJUALAN OBAT","="*10)
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
                    diskon = 0

                    if status == "y" and total >= 100000:
                        diskon = total * 0.1
                        print("Diskon member 10% diterapkan (≥100.000).")
                    elif status == "n" and total >= 200000:
                        diskon = total * 0.1
                        print("Diskon 10% untuk non-member (≥200.000).")

                    total -= diskon
                    o[3] -= jumlah
                    transaksi.append([nama, o[1], jumlah, total])
                    total_pendapatan += total
                    
                    print("\n")
                    print("="*50)
                    print("\t\tSTRUK PEMBELIAN OBAT")
                    print("="*50)
                    print("Nama Pembeli :", nama)
                    print("Obat Dibeli  :", o[1])
                    print("Jumlah       :", jumlah)
                    print("Harga Satuan :", o[2])
                    print("Diskon       : Rp", int(diskon))
                    print("Total Bayar  : Rp", int(total))
                    print("Sisa Stok    :", o[3])
                    print("="*50)
                    print("Terima kasih telah berbelanja!\n")
                    print("Tekan 0 untuk kembali ke menu utama...")
                input(">> ")

                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode obat tidak ditemukan.")

    elif menu == "3":
        print("\n")
        print("\t","="*10,"INPUT DATA PASIEN","="*10)
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])

        print("\n","="*10,"LAYANAN KESEHATAN","="*10)
        print("Kode\tNama Pemeriksaan\t\t\tHarga")
        print("-" * 56)
        for l in layanan_kesehatan:
            print(l[0], "\t", l[1], l[2])
        kode = input("\nMasukkan kode layanan: ")

        ditemukan = 0
        for l in layanan_kesehatan:
            if l[0] == kode:
                status = input("Apakah Member? (y/n): ")
                total = l[2]
                diskon = 0

                if status == "y" and total >= 100000:
                    diskon = total * 0.1
                    print("Diskon member 10% diterapkan (≥100.000).")
                elif status == "n" and total >= 200000:
                    diskon = total * 0.1
                    print("Diskon 10% untuk non-member (≥200.000).")

                total -= diskon
                transaksi.append([nama, l[1], 1, total])
                total_pendapatan += total

                print("\n","="*50)
                print("\t\tSTRUK PEMERIKSAAN")
                print("="*50)
                print("Nama Pasien  :", nama)
                print("Layanan      :", l[1])
                print("Diskon       : Rp", int(diskon))
                print("Total Bayar  : Rp", int(total))
                print("="*50)
                print("Terima kasih telah menggunakan layanan!\n")
                print("Tekan 0 untuk kembali ke menu utama...")
                input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode layanan tidak ditemukan.")

    elif menu == "4":
        print("\n")
        print("     ","="*10,"INPUT DATA PASIEN","="*10)
        nama = input("Nama Pasien: ")
        umur = input("Umur: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")
        keluhan = input("Keluhan Utama: ")
        berat = input("Berat Badan (kg): ")
        tinggi = input("Tinggi Badan (cm): ")
        pasien_list.append([nama, umur, jenis_kelamin, keluhan, berat, tinggi])

        print("\n","="*10,"LAYANAN VAKSINASI","="*10)
        print("Kode\tJenis Vaksin\t\t\tHarga")
        print("-" * 50)
        for v in vaksinasi:
            print(v[0], "\t", v[1], v[2])
        kode = input("\nMasukkan kode vaksin: ")

        ditemukan = 0
        for v in vaksinasi:
            if v[0] == kode:
                status = input("Apakah Member? (y/n): ")
                total = v[2]
                diskon = 0

                if status == "y" and total >= 100000:
                    diskon = total * 0.1
                    print("Diskon member 10% diterapkan (≥100.000).")
                elif status == "n" and total >= 200000:
                    diskon = total * 0.1
                    print("Diskon 10% untuk non-member (≥200.000).")

                total -= diskon
                transaksi.append([nama, v[1], 1, total])
                total_pendapatan += total

                print("\n","="*50)
                print("\t\tSTRUK VAKSINASI")
                print("="*50)
                print("Nama Pasien  :", nama)
                print("Jenis Vaksin :", v[1])
                print("Diskon       : Rp", int(diskon))
                print("Total Bayar  : Rp", int(total))
                print("="*50)
                print("Terima kasih telah vaksinasi di Apotek Girsang!\n")
                print("Tekan 0 untuk kembali ke menu utama...")
                input(">> ")
                ditemukan = 1
                break
        if ditemukan == 0:
            print("Kode vaksin tidak ditemukan.")

    elif menu == "5":
        print("\n","="*10,"LAPORAN TRANSAKSI & DATA PASIEN","="*10)
        print("-" * 60)
        print("Nama\t\tLayanan/Obat\t\tJumlah\tTotal")
        for t in transaksi:
            print(t[0], "\t", t[1], t[2], "\tRp", t[3])
        print("-" * 60)
        print("Total Pendapatan Hari Ini: Rp", total_pendapatan)
        print("-" * 60)
        print("\nData Pasien:")
        for p in pasien_list:
            print("-", p[0], "(", p[1], "th ) |", p[3], "|", p[4], "kg /", p[5], "cm")

    elif menu == "6":
        print("\n","="*10,"CEK / TAMBAH STOK OBAT","="*10)
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
        print("\n")

    elif menu == "7":
        print("\n","="*10,"TERIMA KASIH","="*10)
        print("Total pendapatan hari ini: Rp", total_pendapatan)
        print("Sampai jumpa kembali!\n")

    else:
        print("Pilihan tidak valid, coba lagi!\n")