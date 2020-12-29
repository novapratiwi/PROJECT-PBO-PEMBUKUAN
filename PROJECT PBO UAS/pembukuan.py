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
    def __init__(self, username, email, nama, alamat, nomorTlpn, password):
        super().__init__(username, email, nama, alamat, nomorTlpn, password)
        self.__jabatan = "karyawan"

    def get_jabatan(self):
        return self.__jabatan

class Stock_Barang:
    def __init__(self, idbrg, namabrg, harga, persediaan, jumlahTerjual):
        self.__idBarang = idbrg
        self.__namaBarang = namabrg
        self.__harga = harga
        self.__persediaan = persediaan
        self.__jumlahTerjual = jumlahTerjual

    def get_idBarang(self):
        return self.__idBarang
    
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
        self.noTransaksi = 1
        self.__namaPembeli = namaPembeli
        self.idBarang = []
        self.__listBarang = listBarang
        self.hargaSatuan = []
        self.totalHarga = 0
        self.totalTransaksi = 0
        self.__tanggalPembelian = 0


    def get_listBarang(self):
        return self.__listBarang

    def get_namaPembeli(self):
        return self.__namaPembeli

    def get_tanggalPembelian(self):
        return self.__tanggalPembelian

    def total_transaksi(self):
        

class Pemasukan_kelas:
    def __init__(self, tanggalpemasukan, transaksi, totalpemasukan):
        self.tglpemasukan = tanggalpemasukan
        self.transaksi = transaksi
        self.totalmasuk = totalpemasukan

    def get_noTransaksi(self):
        return self.noTransaksi

    def get_totalPemasukan(self):
        return self.totalmasuk

    def cetak_laporanPenjualan(self):
        pass

    def totalPemasukan():
        return self.totalmasuk


print ("HAI NOVA ASSALAMUALAIKUM SELAMAT HARI SELASA JANGAN LUPA RISET OPERASI")

#satu = Transaksi("nova","kecap")




# karyawan1 = Karyawan(input("a :"),input("b :"),input("c :"),input("d :"),input("e :"),input("f :"))
# print(karyawan1.__dict__)

# kar1 = Login("adinda1", "abcdefg")
# print(kar1.__dict__)
# print(kar1.get_status())

# kar1.log_out()

# print(kar1.__dict__)
# print(kar1.get_status())