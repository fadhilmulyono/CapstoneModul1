products = {
    1: {'nama': 'Bola lampu', 'harga': 10000, 'jumlah': 70},
    2: {'nama': 'Meteran', 'harga': 20000, 'jumlah': 73},
    3: {'nama': 'Kipas angin', 'harga': 12000, 'jumlah': 87},
    4: {'nama': 'Sepatu', 'harga': 26000, 'jumlah': 68},
    5: {'nama': 'Pisau lipat', 'harga': 8000, 'jumlah': 65},
    6: {'nama': 'Gitar', 'harga': 19500, 'jumlah': 98},
    7: {'nama': 'Kelereng', 'harga': 3000, 'jumlah': 89},
    8: {'nama': 'Stapler', 'harga': 22000, 'jumlah': 42},
    9: {'nama': 'Alat perkakas', 'harga': 6500, 'jumlah': 70}
}


def main():
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
            read_data()
        elif menu_option == 2:
            create_data()
        elif menu_option == 3:
            update_data()
        elif menu_option == 4:
            delete_data()
        elif menu_option == 5:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def create_data():
    while True:
        menu_option = int(input('''
    Menambahkan Data Penjualan Toko
    1. Tambah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            id_tambah = int(input('''
    Tambah Data Penjualan
    Masukkan ID data yang ingin ditambahkan: '''))

            if id_tambah in products:
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) sudah ada.".format(id_tambah))
            else:
                # Initialize empty dictionary for new data
                products[id_tambah] = {}

                print("\n\tTambah Data Penjualan")
                nama_barang = input("\tMasukkan nama barang: ")
                harga_barang = int(input("\tMasukkan harga barang: "))
                jumlah_barang = int(input("\tMasukkan jumlah barang terjual: "))

                simpan_data = input("\tYakin menambahkan data yang baru Anda masukkan ({})? ")

                if simpan_data.lower() == "ya":
                    print("\n\tSukses, data berhasil ditambahkan.")
                    products.update({id_tambah: {nama_barang, harga_barang, jumlah_barang}})
                else:
                    print("\n\tMohon maaf, data tidak berhasil ditambahkan.")

        elif menu_option == 2:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def read_data():
    border = '=' * 40

    while True:
        menu_option = int(input('''
    Menampilkan Data Penjualan Toko
    1. Tampilkan Seluruh Data
    2. Cari Data Berdasarkan Index
    3. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            print("""
    Menampilkan Seluruh Data Penjualan Toko
    {}
    {} | {:<15} | {:<5} | {}
    {}""".format(border, "No", "Nama Produk", "Harga", "Jumlah", border))
            for i in products:
                # display
                print("""\t {} | {:<15} | {:<5} | {}""".format
                      (i, products[i]['nama'], products[i]['harga'], products[i]['jumlah']))
            print("\t{}".format(border))

        elif menu_option == 2:
            id_cari = int(input('''
    Cari Data Berdasarkan ID
    Masukkan ID data yang ingin dicari: '''))

            if id_cari not in products.keys():
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_cari))
            else:

                print("""
    Menampilkan Data Penjualan Berdasarkan ID: {}
    {}
    Nama Produk: {}
    Harga Produk: Rp. {}
    Jumlah Penjualan Produk: {}
    {}"""
                      .format(id_cari, border, products[id_cari]['nama'], products[id_cari]['harga'],
                              products[id_cari]['jumlah'], border))

        elif menu_option == 3:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def update_data():
    while True:
        menu_option = int(input('''
    Mengubah Data Penjualan Toko
    1. Ubah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            id_update = int(input('''
    Ubah Data Penjualan
    Masukkan ID data yang ingin diubah: '''))

            if id_update not in products.keys():
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_update))
            else:
                print("\n\tUbah Data Penjualan")
                nama_barang = input("\tMasukkan nama barang: ")
                harga_barang = int(input("\tMasukkan harga barang: "))
                jumlah_barang = int(input("\tMasukkan jumlah barang terjual: "))

                simpan_data = input("\tYakin menyimpan perubahan data yang Anda masukkan untuk ID: {} ? "
                                    .format(id_update))

                if simpan_data.lower() == "ya":
                    print("\n\tSukses, data berhasil diubah.")
                    products[id_update]['nama'] = nama_barang
                    products[id_update]['harga'] = harga_barang
                    products[id_update]['jumlah'] = jumlah_barang
                else:
                    print("\n\tMohon maaf, data tidak berhasil diubah.")

        elif menu_option == 2:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def delete_data():
    while True:
        menu_option = int(input('''
    Menghapus Data Penjualan Toko
    1. Hapus Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            id_delete = int(input('''
    Hapus Data Penjualan
    Masukkan ID data yang ingin dihapus: '''))

            if id_delete not in products.keys():
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_delete))
            else:
                hapus_data = input("\n\tYakin menghapus data yang sesuai dengan ID: {} ? ".format(id_delete))

                if hapus_data.lower() == "ya":
                    print("\n\tSukses, data berhasil dihapus.")
                    del products[id_delete]
                else:
                    print("\n\tMohon maaf, data tidak berhasil dihapus.")

        elif menu_option == 2:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


main()
