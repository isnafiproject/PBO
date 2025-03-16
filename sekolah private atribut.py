class Sekolah:
    def __init__(self, nama_sekolah, alamat, jumlah_guru, jumlah_siswa):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.__jumlah_guru = jumlah_guru  # Private
        self.__jumlah_siswa = jumlah_siswa  # Private

    def info_sekolah(self):
        print(f"{self.nama_sekolah} beralamat di {self.alamat}")

    # Getter untuk jumlah siswa
    def get_jumlah_siswa(self):
        return self.__jumlah_siswa

    # Setter untuk jumlah siswa
    def set_jumlah_siswa(self, jumlah):
        if jumlah >= 0:
            self.__jumlah_siswa = jumlah
        else:
            print("Jumlah siswa tidak boleh negatif!")

    # Getter untuk jumlah guru
    def get_jumlah_guru(self):
        return self.__jumlah_guru

    # Setter untuk jumlah guru
    def set_jumlah_guru(self, jumlah):
        if jumlah >= 0:
            self.__jumlah_guru = jumlah
        else:
            print("Jumlah guru tidak boleh negatif!")

    def __str__(self):
        return f"{self.nama_sekolah} - {self.alamat} | Guru: {self.__jumlah_guru}, Siswa: {self.__jumlah_siswa}"


# Membuat objek baru
sekolah_baru = Sekolah("SMK Sakti Gemolong", "Jalan Raya Sukowati Km. 1", 100, 1550)

# Mengakses atribut private menggunakan getter
print(f"Jumlah siswa sebelum: {sekolah_baru.get_jumlah_siswa()}")
print(f"Jumlah guru sebelum: {sekolah_baru.get_jumlah_guru()}")

# Mengubah jumlah siswa dan guru menggunakan setter
sekolah_baru.set_jumlah_siswa(1660)
sekolah_baru.set_jumlah_guru(130)

# Mengakses kembali setelah perubahan
print(f"Jumlah siswa setelah: {sekolah_baru.get_jumlah_siswa()}")
print(f"Jumlah guru setelah: {sekolah_baru.get_jumlah_guru()}")

# Menampilkan seluruh informasi sekolah
print(sekolah_baru)
