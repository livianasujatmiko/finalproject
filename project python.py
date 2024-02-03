class pegawai:
    def __init__(self):
        self.pegawai_data = []

    def add_pegawai(self):
        nama = input("Masukkan nama pegawai: ")
        status_kerja = input("Masukkan status kerja (full time/part time/internship): ")
        tahun_masuk = input("Masukkan tahun masuk: ")
        gaji = input("Masukkan gaji: ")

        add = {
            "Nama": nama,
            "Status Kerja": status_kerja,
            "Tahun Masuk": tahun_masuk,
            "Gaji": gaji
        }
        self.pegawai_data.append(add)
    def show_pegawai(self):
        print("==============================")
        print("DATA PEGAWAI")
        for data in self.pegawai_data:
            print("==============================")
            print(f"Nama: {data['Nama']}")
            print(f"Status Kerja: {data['Status Kerja']}")
            print(f"Tahun Masuk: {data['Tahun Masuk']}")
            print(f"Gaji: {data['Gaji']}")
            print("==============================\n")
            print()
    def edit_pegawai(self):
        self.show_pegawai()
        num_pegawai = int(input("Masukkan nomor pegawai yang diedit: ")) - 1

        if 0 <= num_pegawai < len(self.pegawai_data):
            nama = input("Masukkan nama pegawai: ")
            status_kerja = input("Masukkan status kerja (full time/part time/internship): ")
            tahun_masuk = input("Masukkan tahun masuk: ")
            gaji = input("Masukkan gaji: ")

            self.pegawai_data[num_pegawai] = {
                "Nama": nama,
                "Status Kerja": status_kerja,
                "Tahun Masuk": tahun_masuk,
                "Gaji": gaji
            }
            print("Data pegawai diubah.")

    def delete_pegawai(self):
        self.show_pegawai()
        num_pegawai = int(input("Masukkan nomor pegawai yang akan dihapus: ")) - 1

        if 0 <= num_pegawai < len(self.pegawai_data):
            del self.pegawai_data[num_pegawai]
            print("Data pegawai berhasil dihapus.")

def main():
    info_pegawai = pegawai()

    while True:
        print("|--------------------|")
        print("|MENU UTAMA          |")
        print("|--------------------|")
        print("|1. Tambah Pegawai   |")
        print("|--------------------|")
        print("|2. Tampilkan Pegawai|")
        print("|--------------------|")
        print("|3. Edit Pegawai     |")
        print("|--------------------|")
        print("|4. Hapus Pegawai    |")
        print("|--------------------|")
        pilihan = input("PILIH MENU (1/2/3/4): ")
        print("|--------------------|")

        if pilihan == '1':
                info_pegawai.add_pegawai()
        elif pilihan == '2':
                info_pegawai.show_pegawai()
        elif pilihan == '3':
                info_pegawai.edit_pegawai()
        elif pilihan == '4':
                info_pegawai.delete_pegawai()

if __name__ == "__main__":
    main()