class Sekolah:
    def __init__(self, nama_sekolah, alamat, jumlah_guru, jumlah_siswa):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.jumlah_guru = jumlah_guru
        self.jumlah_siswa = jumlah_siswa

    def info_sekolah(self):
        print(f"{self.nama_sekolah} beralamat di {self.alamat}")

    def tambah_siswa(self):
        print(f"Jumlah siswa sebanyak {self.jumlah_siswa} siswa ")

    def tambah_guru(self):
        print(f"Menambah guru sebanyak {self.jumlah_guru} ")

my_sekolah = Sekolah("SMP Dirgantara", "Jalan Sudirman", 2, 1000)
my_siswa = Sekolah("SMK Sakti Gemolong","Jalan Sukowati", 5, 1600)

my_sekolah.info_sekolah()
my_sekolah.tambah_siswa()
my_sekolah.tambah_guru()

my_siswa.info_sekolah()
my_siswa.tambah_siswa()
my_siswa.tambah_guru()