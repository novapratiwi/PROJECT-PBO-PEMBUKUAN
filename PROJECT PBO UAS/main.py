import datetime
import sqlite3
import pembukuan as p
databaseName = "pembukuan.db"
conn = sqlite3.connect(databaseName)

print("===SISTEM PEMBUKUAN===\n1.Masukan Data Karyawan Baru\n2.Login\n")
pilihan = int(input("masukan pilihan anda : "))

if pilihan == 1:
    conn.execute(
    "CREATE TABLE IF NOT EXISTS Karyawan (username text primary key, jabatan text, email text, name text, address text, phoneNumber text, password text)"
    )

    inputKaryawan = p.Karyawan(input("Username :"),input("Email :"),input("Nama :"),input("Alamat :"),input("Nomor Telepon :"),input("Password :"))

    res = conn.execute("select * from Karyawan where username = ?", (inputKaryawan.get_username(),))

    cursor = conn.cursor().execute("select * from Karyawan")
    for row in cursor:
        if res.fetchone() is None:
            conn.execute("insert into Karyawan values (?,?,?,?,?,?,?)", (inputKaryawan.get_username(),inputKaryawan.get_jabatan(),inputKaryawan.get_email(), inputKaryawan.get_name(), inputKaryawan.get_address(), inputKaryawan.get_phoneNumber(), inputKaryawan.get_password()))
            conn.commit()
            print("data karyawan berhasil ditambahkan")
        else :
            print("maaf username yang anda masukan sudah terdaftar")

elif pilihan == 2:
    conn.execute(
    "CREATE TABLE IF NOT EXISTS Login(username text primary key, password text, status text)"
    )

    login = p.Login(input("Username :"), input("Password :"))

    username = login.get_username()
    password = login.get_password()

    cursor = conn.cursor().execute("select username,password from Karyawan where username = ? AND password = ?", (username, password))
    ketemu = cursor.fetchone()
    #print(ketemu) mengecek variabel ketemu

    if ketemu:
        conn.execute("insert into Login values (?,?,?)", (login.get_username(), login.get_password(), login.get_status()))
        conn.commit()
        print("anda berhasil login")
        masuk = True


        if masuk == True:
            print("1. LOG OUT\n2. StokBrg\n3. Transaksi")
            choose = int(input("Masukan pilihanmu :"))

            if choose == 1:
                conn.execute("delete from Login where username = ?", (username,))
                conn.commit()
                print("anda berhasil log out")
            
            if choose == 2:
                conn.execute(
                    "CREATE TABLE IF NOT EXISTS Stock_Barang (idBarang int primary key,namaBarang text,hargaSatuan int, persediaan int, jumlahTerjual int)"
                    )
                
                tambahstok = p.Stock_Barang(input("id barang : "), input("nama barang : "), input("harga barang : "), input("persediaan : "), input("jumlah terjual : "))
                
                conn.execute("insert into Stock_Barang values (?,?,?,?,?)", (tambahstok.get_idBarang(), tambahstok.get_namaBarang(), tambahstok.get_harga(), tambahstok.get_persediaan(), tambahstok.get_jumlahTerjual()))


            if choose == 3:
                conn.execute(
                    "CREATE TABLE IF NOT EXISTS Transaksi (idTransaksi int primary key, username text, namaPembeli text, idBarang text, listBarang text, hargaSatuan text, totalHarga int, waktuTransaksi DATETIME)"
                    )
                
                listbrg = []

                transaksi = p.Transaksi(input("nama pembeli : "),input("nama barang : "))
                listbrg.append(transaksi.get_listBarang())
                lanjut = input("lagi? (y/n) : ")
                while lanjut == "y":
                    more = input("nama barang : ")
                    listbrg.append(more)
                    lanjut = input("lagi? (y/n) : ")
                    if lanjut == "n":
                        break
                #menjadikan list id barang menjadi string
                print(listbrg)
                newlistbrg = ",".join(listbrg)


                #hitung baris di db transaksi
                cursor1 = conn.cursor().execute("select idTransaksi from Transaksi")
                for row in cursor1:
                    for i in row:
                        transaksi.noTransaksi += i

                #mengambil idbarang dari tabel stock brg
                cursor2 = conn.cursor().execute("select * from Stock_Barang")
                for row in cursor2:
                    for i in listbrg:
                        if row[1] == i:
                            transaksi.idBarang.append(row[0])
                            transaksi.hargaSatuan.append(row[2])
                            transaksi.totalHarga += (row[2])

                tanggal = datetime.datetime.now()

                #menjadikan list idbarang menjadi string
                newlistIDbarang = ",".join(map(str, transaksi.idBarang))

                #menjadikan list harga satuan menjadi string
                newlistHargaSatuan = ",".join(map(str, transaksi.hargaSatuan))


                
                conn.execute("insert into Transaksi values (?,?,?,?,?,?,?,?)", (transaksi.noTransaksi, login.get_username(), transaksi.get_namaPembeli(), newlistIDbarang, newlistbrg, newlistHargaSatuan, transaksi.totalHarga, tanggal))
                conn.commit()

    else:
        print("maaf username/password yang anda masukan salah")
            

else:
    print("heyho")   
           
    conn.execute("delete from Login where username = ?", (username,))
    conn.commit()
    print("anda berhasil log out")

    


# membaca data lewat python
# cursor = conn.cursor().execute("select * from Karyawan")
# for row in cursor:
#     print(row)

conn.close()