import datetime
import sqlite3
import pembukuan as p
databaseName = "pembukuan.db"
conn = sqlite3.connect(databaseName)

print("===SISTEM PEMBUKUAN===\n1.Masukan Data Baru\n2.Login\n")
pilihan = int(input("masukan pilihan anda : "))


if pilihan == 1:
    pilih = input("karyawan atau owner? : ")

    if pilih == "karyawan" :
        conn.execute(
        "CREATE TABLE IF NOT EXISTS Karyawan (username text primary key, jabatan text, email text, name text, address text, phoneNumber text, password text, gajiKaryawan)"
        )

        inputKaryawan = p.Karyawan(input("Username :"),input("Email :"),input("Nama :"),input("Alamat :"),input("Nomor Telepon :"),input("Password :"), int(input("gaji : ")))

        res = conn.execute("select * from Karyawan where username = ?", (inputKaryawan.get_username(),))

        cursor = conn.cursor().execute("select * from Karyawan")
        for row in cursor:
            if res.fetchone() is None:
                conn.execute("insert into Karyawan values (?,?,?,?,?,?,?,?)", (inputKaryawan.get_username(),inputKaryawan.get_jabatan(),inputKaryawan.get_email(), inputKaryawan.get_name(), inputKaryawan.get_address(), inputKaryawan.get_phoneNumber(), inputKaryawan.get_password(), inputKaryawan.get_gajiKaryawan()))
                conn.commit()
                print("data karyawan berhasil ditambahkan")
            else :
                print("maaf username yang anda masukan sudah terdaftar")
    
    elif pilih=="owner":
        conn.execute(
        "CREATE TABLE IF NOT EXISTS Owner (username text primary key, jabatan text, email text, name text, address text, phoneNumber text, password text)"
        )

        inputOwner = p.Owner(input("Username :"),input("Email :"),input("Nama :"),input("Alamat :"),input("Nomor Telepon :"),input("Password :"))

        conn.execute("insert into Owner values (?,?,?,?,?,?,?)", (inputOwner.get_username(),inputOwner.get_jabatan(),inputOwner.get_email(), inputOwner.get_name(), inputOwner.get_address(), inputOwner.get_phoneNumber(), inputOwner.get_password()))
        conn.commit()
        print("data Owner berhasil ditambahkan")

elif pilihan == 2:
    pilih = input("owner atau karyawan? : ")

    if pilih=="owner":

        login = p.Login(input("Username : "), input("Password : "))

        username = login.get_username()
        password = login.get_password()

        cursor = conn.cursor().execute("select username,password from Owner where username = ? AND password = ?", (username, password))
        ketemu = cursor.fetchone()
        # print(ketemu) #mengecek variabel ketemu

        if ketemu:
            print("anda berhasil login")
            masuk = True

            if masuk == True:
                print("1. StokBrg\n2. Transaksi\n3. Pemasukan\n4. Pengeluaran")
                choose = int(input("Masukan pilihanmu :"))

                if choose==1:
                    # membaca data lewat python
                    cursor = conn.cursor().execute("select * from Stock_Barang")
                    for row in cursor:
                        print(row)

                if choose == 2:
                    # membaca data lewat python
                    cursor = conn.cursor().execute("select * from Transaksi")
                    for row in cursor:
                        print(row)

                if choose == 3 :
                    pilih = input("input pemasukan atau lihat pemasukan? : ")

                    if pilih == "input":
                        print("=====PEMASUKAN=====")
                        conn.execute(
                        "CREATE TABLE IF NOT EXISTS Pemasukan (tanggal_transaksi datetime primary key, total_pemasukan int)"
                        )
                        addpemasukan = p.Pemasukan(input("Tanggal Transaksi : "))

                        tampung =[]

                        cursor = conn.cursor().execute("select * from Transaksi WHERE DATE(waktuTransaksi) = ?", (addpemasukan.get_datePemasukan(),))
                        for row in cursor:
                            tampung.append(row)

                        for row in tampung:
                            addpemasukan.set_totalPemasukan(row[6])

                        conn.execute("insert into Pemasukan values (?,?)", (addpemasukan.get_datePemasukan(), addpemasukan.get_totalPemasukan()))
                        conn.commit()
                        print("pemasukan berhasil ditambahkan")
                        
                        conn.execute("delete from Login where username = ?", (username,))
                        conn.commit()
                        print("anda berhasil log out")


                    if pilih == "seluruh":
                        # membaca data lewat python
                        cursor = conn.cursor().execute("select * from Pemasukan")
                        for row in cursor:
                            print(row)

                if choose == 4 :
                    pilih = input("tambah pengeluaran atau lihat pengeluaran? : ")

                    if pilih == "tambah":
                        conn.execute(
                        "CREATE TABLE IF NOT EXISTS Pengeluaran (idPengeluaran int primary key, namaPengeluaran text, idBarang int, biayaPengeluaranSatuan int, jumlah int, totalPengeluaran int, waktuPengeluaran datetime)"
                        )
                        conn.commit()

                        pengeluaran = p.Pengeluaran(input("nama pengeluaran : "),int(input("jumlah : ")), int(input("Total harga barang yang distock : ")))

                        cursor1 = conn.cursor().execute("select idPengeluaran from Pengeluaran")
                        
                        # id pengeluaran
                        for row in cursor1:
                            for i in row:
                                pengeluaran.set_idPengeluaran(1)
                                print(pengeluaran.get_idPengeluaran())
                        
                        # id barang dan biaya satuan
                        cursor = conn.cursor().execute("select * from Stock_Barang")
                        cursor1 = conn.cursor().execute("select * from Karyawan")
                        for row in cursor:
                            if row[1] == pengeluaran.get_namaPengeluaran():
                                print(row[1])
                                pengeluaran.set_idBarang(row[0])
                                print(pengeluaran.get_idBarang())
                                pengeluaran.set_biayaSatuan(row[2])
                                print(pengeluaran.get_biayaSatuan())

                            elif pengeluaran.get_namaPengeluaran() == "gaji karyawan" :
                                for row in cursor1:
                                    print(pengeluaran.get_idBarang())
                                    pengeluaran.set_biayaSatuan(row[7])
                                    print(pengeluaran.get_biayaSatuan())
                                    break
                                break

                        # waktu pengeluaran
                        pengeluaran.set_waktuPengeluaran(datetime.datetime.now())
                                
                        conn.execute("insert into Pengeluaran values (?,?,?,?,?,?,?)", (pengeluaran.get_idPengeluaran(), pengeluaran.get_namaPengeluaran(),pengeluaran.get_idBarang(), pengeluaran.get_biayaSatuan(), pengeluaran.get_jumlah(), pengeluaran.get_totalhrgPengeluaran(), pengeluaran.get_waktuPengeluaran()))
                        conn.commit()

                        conn.execute("delete from Login where username = ?", (username,))
                        conn.commit()
                        print("anda berhasil log out")

                    if pilih == "lihat":
                        # membaca data lewat python
                        cursor = conn.cursor().execute("select * from Pengeluaran")
                        for row in cursor:
                            print(row)

        else:
            print("maaf username/password yang anda masukan salah")

    
    if pilih == "karyawan":
        conn.execute(
        "CREATE TABLE IF NOT EXISTS Login(username text primary key, password text, status text)"
        )

        login = p.Login(input("Username : "), input("Password : "))

        username = login.get_username()
        password = login.get_password()

        cursor = conn.cursor().execute("select username,password from Karyawan where username = ? AND password = ?", (username, password))
        ketemu = cursor.fetchone()
        # print(ketemu) #mengecek variabel ketemu

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
                    
                    tambahstok = p.Stock_Barang(input("nama barang : "), int(input("harga barang : ")), int(input("persediaan : ")), int(input("jumlah terjual : ")))
                    
                    cursor = conn.cursor().execute("select idBarang from Stock_Barang")
                    hitung=0
                    for row in cursor:
                        hitung+=1
                    tambahstok.set_idBarang(hitung+1)
                    print(tambahstok.get_idBarang())

                    conn.execute("insert into Stock_Barang values (?,?,?,?,?)", (tambahstok.get_idBarang(), tambahstok.get_namaBarang(), tambahstok.get_harga(), tambahstok.get_persediaan(), tambahstok.get_jumlahTerjual()))
                    conn.commit()

                    conn.execute("delete from Login where username = ?", (username,))
                    conn.commit()
                    print("anda berhasil log out")

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
                    # print(listbrg)
                    newlistbrg = ",".join(listbrg)

                    cursor = conn.cursor().execute("select * from Stock_Barang")
                    for row in cursor:
                        print(row[1])
                        for i in listbrg:
                            if i==row[1]:
                                print(i)
                                continue
                    


                    #hitung baris di db transaksi
                    cursor1 = conn.cursor().execute("select idTransaksi from Transaksi")
                    hitung=0
                    for row in cursor1:
                        hitung+=1
                    transaksi.set_noTransaksi(hitung+1)

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


                    
                    # conn.execute("insert into Transaksi values (?,?,?,?,?,?,?,?)", (transaksi.get_noTransaksi(), login.get_username(), transaksi.get_namaPembeli(), newlistIDbarang, newlistbrg, newlistHargaSatuan, transaksi.totalHarga, tanggal))
                    # conn.commit()

                    conn.execute("delete from Login where username = ?", (username,))
                    conn.commit()
                    print("anda berhasil log out")

        else:
            print("maaf username/password yang anda masukan salah")
            

else:
    print("heyho")   
           
    conn.execute("delete from Login where username = ?", (username,))
    conn.commit()
    print("anda berhasil log out")


conn.close()