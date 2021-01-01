class Login:
    def __init__(self,username, password):
        self.__username = username
        self.__password = password
        self.__status = "online"
    
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
    
    def set_username(self, new):
        self.__username = new

    def set_password(self,new):
        self.__password = new

    def get_status(self):
        return self.__status

class User(Login):
    def __init__(self, username, email, nama, alamat, nomorTlpn, password):
        super().__init__(username, password)
        self.__email = email
        self.__name = nama
        self.__address = alamat
        self.__phoneNumber = nomorTlpn

    def get_email(self):
        return self.__email
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phoneNumber(self):
        return self.__phoneNumber
    
    def set_email(self,new):
        self.__email = new

    def set_name(self,new):
        self.__name = new

    def set_address(self,new):
        self.__address = new

    def set_phoneNumber(self,new):
        self.__phoneNumber = new

class Owner(User):
    def __init__(self, username, email, nama, alamat, nomorTlpn, password):
        super().__init__(username, email, nama, alamat, nomorTlpn, password)
        self.__jabatan = "owner"

    def get_jabatan(self):
        return self.__jabatan

class Karyawan(User):
    def __init__(self, username, email, nama, alamat, nomorTlpn, password, gaji):
        super().__init__(username, email, nama, alamat, nomorTlpn, password)
        self.__jabatan = "karyawan"
        self.__gajiKaryawan = gaji

    def get_jabatan(self):
        return self.__jabatan

    def get_gajiKaryawan(self):
        return self.__gajiKaryawan

    def set_gajiKaryawan(self, gaji):
        self.__gajiKaryawan = gaji

class Stock_Barang:
    def __init__(self, namabrg, harga, persediaan, jumlahTerjual):
        self.__idBarang = 0
        self.__namaBarang = namabrg
        self.__harga = harga
        self.__persediaan = persediaan
        self.__jumlahTerjual = jumlahTerjual

    def get_idBarang(self):
        return self.__idBarang

    def set_idBarang(self, id):
        self.__idBarang = id
    
    def get_namaBarang(self):
        return self.__namaBarang
    
    def get_harga(self):
        return self.__harga
    
    def get_persediaan(self):
        return self.__persediaan
    
    def get_jumlahTerjual(self):
        return self.__jumlahTerjual

class Transaksi(Login):
    def __init__(self, namaPembeli, listBarang):
        self.__noTransaksi = 1
        self.__namaPembeli = namaPembeli
        self.idBarang = []
        self.__listBarang = listBarang
        self.hargaSatuan = []
        self.totalHarga = 0
        self.totalTransaksi = 0
        self.__tanggalPembelian = 0

    def get_noTransaksi(self):
        return self.__noTransaksi
    
    def set_noTransaksi(self,no):
        self.__noTransaksi = no

    def get_listBarang(self):
        return self.__listBarang

    def get_namaPembeli(self):
        return self.__namaPembeli

    def get_tanggalPembelian(self):
        return self.__tanggalPembelian

class Pemasukan(Transaksi):
    def __init__(self, tanggal):
        #super().__init__(namaPembeli, listBarang)
        self.__tglpemasukan = tanggal
        self.__totalmasuk = 0
    
    def get_datePemasukan(self):
        return self.__tglpemasukan 

    def get_totalPemasukan(self):
        return self.__totalmasuk

    def set_totalPemasukan(self,tambah):
        self.__totalmasuk += tambah

class Pengeluaran(Stock_Barang):
    def __init__(self, namapengeluaran, jumlah, totalhrg):
        self.__idPengeluaran = 1
        self.__idBarang = 0
        self.__biayaSatuan = 0
        self.__namaPengeluaran = namapengeluaran
        self.__jumlah = jumlah
        self.__totalPengeluaran = totalhrg
        self.__waktuPengeluaran = 0

    def get_idPengeluaran(self):
        return self.__idPengeluaran

    def set_idPengeluaran(self, tambahID):
        self.__idPengeluaran += tambahID
    
    def get_namaPengeluaran(self):
        return self.__namaPengeluaran

    def get_idBarang(self):
        return self.__idBarang

    def set_idBarang(self, id):
        self.__idBarang = id

    def get_biayaSatuan(self):
        return self.__biayaSatuan

    def set_biayaSatuan(self, biaya):
        self.__biayaSatuan = biaya
    
    def get_jumlah(self):
        return self.__jumlah

    def get_totalhrgPengeluaran(self):
        return self.__totalPengeluaran

    def get_waktuPengeluaran(self):
        return self.__waktuPengeluaran

    def set_waktuPengeluaran(self,waktu):
        self.__waktuPengeluaran = waktu
