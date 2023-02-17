# Dictionary untuk List Data Penjualan Toko
products = {
    1: {'nama': 'Bola lampu', 'harga': 10000, 'jumlah': 70},
    2: {'nama': 'Meteran', 'harga': 20000, 'jumlah': 73},
    3: {'nama': 'Kipas angin', 'harga': 12000, 'jumlah': 87},
    4: {'nama': 'Sepatu', 'harga': 26000, 'jumlah': 68},
    5: {'nama': 'Pisau lipat', 'harga': 8000, 'jumlah': 65},
    6: {'nama': 'Gitar', 'harga': 19500, 'jumlah': 98},
    7: {'nama': 'Kelereng', 'harga': 3000, 'jumlah': 89},
    8: {'nama': 'Stapler', 'harga': 22000, 'jumlah': 42},
    9: {'nama': 'Alat perkakas', 'harga': 65000, 'jumlah': 20}
}


def main():
    # Menampilkan Menu Opsi Program - Capstone Project
    while True:
        menu_option = int(input('''
    Welcome to Capstone Emmerce by Fadhil Mulyono Yulius
    Main Menu:
    1. Baca Data Penjualan
    2. Tambah Data Penjualan
    3. Edit Data Penjualan
    4. Hapus Data Penjualan
    5. Exit Program

    Input Menu Option : '''))

        if menu_option == 1:
            # Fungsi Read Data
            read_data()
        elif menu_option == 2:
            # Fungsi Create Data
            create_data()
        elif menu_option == 3:
            # Fungsi Update Data
            update_data()
        elif menu_option == 4:
            # Fungsi Delete Data
            delete_data()
        elif menu_option == 5:
            # Keluar dari program
            break
        else:
            # Munculkan error jika salah input menu
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def create_data():
    # Tampil Menu Menambahkan Data (Tambah Data)
    while True:
        menu_option = int(input('''
    Menambahkan Data Penjualan Toko
    1. Tambah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            # User input Primary Key (ID) data yang akan ditambahkan
            id_tambah = int(input('''
    Tambah Data Penjualan
    Masukkan ID data yang ingin ditambahkan: '''))

            # Cek input data duplikat
            if id_tambah in products:
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) sudah ada.".format(id_tambah))
            else:
                # Initialize Dictionary untuk data yang akan ditambahkan
                products[id_tambah] = {}

                # User input kelengkapan data (Nama, Harga, Jumlah barang)
                print("\n\tTambah Data Penjualan")
                nama_barang = input("\tMasukkan nama barang: ")
                harga_barang = int(input("\tMasukkan harga barang: "))
                jumlah_barang = int(input("\tMasukkan jumlah barang terjual: "))

                # Menampilkan Menu pilihan Simpan Data
                simpan_data = input("\tYakin menambahkan data yang baru Anda masukkan untuk ID : {} ? "
                                    .format(id_tambah))

                if simpan_data.lower() == "ya":
                    # Input "ya" untuk Simpan Data
                    print("\n\tSukses, data berhasil ditambahkan.")
                    products[id_tambah]['nama'] = nama_barang
                    products[id_tambah]['harga'] = harga_barang
                    products[id_tambah]['jumlah'] = jumlah_barang
                else:
                    # Jika input selain "ya" atau dibiarkan kosong, data tidak tersimpan
                    print("\n\tMohon maaf, data tidak berhasil ditambahkan.")

        elif menu_option == 2:
            # Kembali ke menu utama
            break
        else:
            # Munculkan error jika salah input menu
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def read_data():
    # Initialize variable border untuk output tabel
    border = '=' * 60

    while True:
        # Tampil Menu Menampilkan Data (Baca Data)
        menu_option = int(input('''
    Menampilkan Data Penjualan Toko
    1. Tampilkan Seluruh Data
    2. Cari Data Berdasarkan Index
    3. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            if len(products) == 0:
                # Tampilkan notifikasi Tidak Ada Data
                print("\n\tMohon maaf, tidak ada data penjualan toko yang dapat ditampilkan.")
            else:
                # Initialize variable Total Penjualan Produk per kolom
                total_penjualan = 0

                # Menampilkan Seluruh Data
                print("""
    Menampilkan Seluruh Data Penjualan Toko
    {}
    {} | {:<15} | {:<10} | {:<6} | {}
    {}""".format(border, "No", "Nama Produk", "Harga", "Jumlah", "Total", border))
                for i in products:
                    # Total Penjualan = Kalikan harga produk dengan jumlah produk terjual
                    total = products[i]['harga'] * products[i]['jumlah']

                    # Jumlahkan semua kolom Total Penjualan
                    total_penjualan += total

                    # Tampilkan daftar penjualan per kolom
                    print("""\t {} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}""".format
                          (i, products[i]['nama'], products[i]['harga'], products[i]['jumlah'], total))

                # Tampilkan hasil dari penjumlahan Total Penjualan
                print("""\t{}
         Total Penjualan : Rp. {}""".format(border, total_penjualan))

        elif menu_option == 2:
            # User input Primary Key (ID) data yang ingin dicari
            id_cari = int(input('''
    Cari Data Berdasarkan ID
    Masukkan ID data yang ingin dicari: '''))

            # Cek apakah ID data yang dicari ada di Dictionary
            if id_cari not in products.keys():
                # Tampilkan notifikasi Tidak Ada Data
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_cari))
            else:
                # Total Penjualan = Kalikan harga produk dengan jumlah produk terjual
                total = products[id_cari]['harga'] * products[id_cari]['jumlah']

                # Menampilkan Data Sesuai Input User
                print("""
    Menampilkan Data Penjualan Berdasarkan ID: {}
    {}
    {} | {:<15} | {:<10} | {:<6} | {}
    {}
     {} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}
    {}""".format(id_cari, border, "No", "Nama Produk", "Harga", "Jumlah", "Total", border, id_cari,
                 products[id_cari]['nama'], products[id_cari]['harga'], products[id_cari]['jumlah'], total, border))

        elif menu_option == 3:
            # Kembali ke menu utama
            break
        else:
            # Munculkan error jika salah input menu
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def update_data():
    # Initialize variable border untuk output tabel
    border = '=' * 60

    # Tampil Menu Mengubah Data (Edit Data)
    while True:
        menu_option = int(input('''
    Mengubah Data Penjualan Toko
    1. Ubah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            # User input Primary Key (ID) data yang ingin diubah
            id_update = int(input('''
    Ubah Data Penjualan
    Masukkan ID data yang ingin diubah: '''))

            if id_update not in products.keys():
                # Tampilkan notifikasi Tidak Ada Data
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_update))
            else:
                # Total Penjualan = Kalikan harga produk dengan jumlah produk terjual
                total = products[id_update]['harga'] * products[id_update]['jumlah']

                # Menampilkan Data Sesuai ID Data yang diinput user
                print("""
    Menampilkan Data Penjualan Berdasarkan ID: {}
    {}
    {} | {:<15} | {:<10} | {:<6} | {}
    {}
     {} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}
    {}""".format(id_update, border, "No", "Nama Produk", "Harga", "Jumlah", "Total", border, id_update,
                 products[id_update]['nama'], products[id_update]['harga'], products[id_update]['jumlah'],
                 total, border))

                print("\n\tUbah Data Penjualan Untuk ID: {}".format(id_update))
                # User input kolom yang akan di Update (Nama, Harga, Jumlah barang)
                nama_barang = input("\tMasukkan nama barang: ")
                harga_barang = int(input("\tMasukkan harga barang: "))
                jumlah_barang = int(input("\tMasukkan jumlah barang terjual: "))

                simpan_data = input("\tYakin menyimpan perubahan data yang Anda masukkan untuk ID : {} ? "
                                    .format(id_update))

                if simpan_data.lower() == "ya":
                    print("\n\tSukses, data berhasil diubah.")
                    products[id_update]['nama'] = nama_barang
                    products[id_update]['harga'] = harga_barang
                    products[id_update]['jumlah'] = jumlah_barang
                else:
                    print("\n\tMohon maaf, data tidak berhasil diubah.")

        elif menu_option == 2:
            # Kembali ke menu utama
            break
        else:
            # Munculkan error jika salah input menu
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def delete_data():
    # Tampil Menu Menghapus Data (Delete Data)
    while True:
        menu_option = int(input('''
    Menghapus Data Penjualan Toko
    1. Hapus Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            # User input Primary Key (ID) data yang ingin dihapus
            id_delete = int(input('''
    Hapus Data Penjualan
    Masukkan ID data yang ingin dihapus: '''))

            if id_delete not in products.keys():
                # Tampilkan notifikasi Tidak Ada Data
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_delete))
            else:
                # Menampilkan Menu pilihan Hapus Data
                hapus_data = input("\n\tYakin menghapus data yang sesuai dengan ID : {} ? ".format(id_delete))

                if hapus_data.lower() == "ya":
                    # Input "ya" untuk Menghapus Data
                    print("\n\tSukses, data berhasil dihapus.")
                    del products[id_delete]
                else:
                    # Jika input selain "ya" atau dibiarkan kosong, data tidak dihapus
                    print("\n\tMohon maaf, data tidak berhasil dihapus.")

        elif menu_option == 2:
            # Kembali ke menu utama
            break
        else:
            # Munculkan error jika salah input menu
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


main()
