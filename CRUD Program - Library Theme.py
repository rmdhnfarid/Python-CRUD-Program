daftarbuku = [{'No' : '001',
        'Judul' : 'Laskar Pelangi',
        'Penulis' : 'Andrea Hirata',
        'Penerbit' : 'Bentang Pustaka',
        'Kategori' : 'Novel',
        'Ketersediaan' : 'Tersedia'
    },
    {
        'No' : '002',
        'Judul' : 'Kambing Jantan',
        'Penulis' : 'Raditya Dika',
        'Penerbit' : 'GagasMedia',
        'Kategori' : 'Komedi',
        'Ketersediaan' : 'Tidak Tersedia'
    },
    {
        'No' : '003',
        'Judul' : 'Soekarno : Biografi Singkat 1901 - 1970', 
        'Penulis' : 'Taufik Adi Susilo',
        'Penerbit' : 'GARASI',
        'Kategori' : 'Biografi',
        'Ketersediaan' : 'Tersedia'},
    {
        'No' : '004',
        'Judul' : 'Solo Leveling',
        'Penulis' : 'Chugong',
        'Penerbit' : 'D&C Media',
        'Kategori' : 'Fiksi',
        'Ketersediaan' : 'Tidak Tersedia'},
    {
        'No' : '005',
        'Judul' : 'One-Punch Man Vol 1',
        'Penulis' : 'One',
        'Penerbit' : 'Shueisha',
        'Kategori' : 'Komik',
        'Ketersediaan' : 'Tersedia'
    }
]

# DAFTAR BUKU AWAL
def showlistupdate(listdata, x, newdata):
    print('=========== Daftar Buku ===========')
    print('|No\t| Judul\t| Penulis\t| Penerbit\t| Kategori\t| Ketersediaan\t|')
    if x == 1:
        for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['Judul'], listdata[i]['Penulis'], listdata[i]['Penerbit'], listdata[i]['Kategori'], listdata[i]['Ketersediaan']))
    elif x == 2:
         for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['No'], listdata[i]['Penulis'], listdata[i]['Penerbit'], listdata[i]['Kategori'], listdata[i]['Ketersediaan']))
    elif x == 3:
         for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['No'], listdata[i]['Judul'], listdata[i]['Penerbit'], listdata[i]['Kategori'], listdata[i]['Ketersediaan']))
    elif x == 4:
         for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['No'], listdata[i]['Judul'], listdata[i]['Penulis'], listdata[i]['Kategori'], listdata[i]['Ketersediaan']))
    elif x == 5:
         for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['No'], listdata[i]['Judul'], listdata[i]['Penulis'], listdata[i]['Penerbit'], listdata[i]['Ketersediaan']))
    elif x == 6:
         for i in range(len(listdata)):
            print('{}\t| {}\t| {}\t| {}\t| {}\t|'.format(newdata,listdata[i]['No'], listdata[i]['Judul'], listdata[i]['Penulis'], listdata[i]['Penerbit'], listdata[i]['Kategori']))

# FUNGSI UPDATE
def updatebarang(data, kolom, newdata2):
    inputupdatebarang = (input(' apakah data sudah benar? (Ya/Tidak): ')).capitalize()
    if inputupdatebarang == 'Ya':
        data[0][kolom] = newdata2
        print('data sudah diperbarui')
    else:
        print('data tidak diperbarui')

# TABEL BUKU
def showlist(listdata):
    print('============ Daftar Buku ============')
    print('|No\t| Judul\t| Penulis\t| Penerbit\t| Kategori\t| Ketersediaan\t|')
    for i in range(len(listdata)) :
        print('|{}\t| {}\t| {}\t| {}\t| {}\t| {}\t|'.format(listdata[i]['No'], listdata[i]['Judul'], listdata[i]['Penulis'], listdata[i]['Penerbit'], listdata[i]['Kategori'], listdata[i]['Ketersediaan']))

# FILTER BUKU
def searchlist(input):
    searchlist = (list(filter(lambda data: data['No'] == str(input), daftarbuku)))
    return searchlist

# DAFTAR BUKU
def read():
    inputread = (int(input(''' Daftar Data Buku 
    1. Daftar Semua Buku
    2. Cari Buku
    3. Kembali
    Masukkan no Menu yang Diinginkan: ''')))
    if inputread == 1 and len(daftarbuku):
        showlist(daftarbuku)
    elif inputread == 2 and len(daftarbuku):
        Nomorbuku = (input('Masukkan No Buku: '))
        searchlist(Nomorbuku)
        if len(searchlist(Nomorbuku)):
            showlist(searchlist(Nomorbuku))
        else:
            print('Buku Tidak Ada')
    elif inputread == 3:
        menu()
    else:
        print('Nomor yang Dimasukkan Tidak Sesuai')
    read()

# MENAMBAH BUKU
def add():
    inputadd = (int(input(''' Menambah Data Buku
    1. Menambah Data Buku
    2. Kembali
    Masukkan no Menu yang Diinginkan: ''')))
    if inputadd == 1:
        nomorbukubaru = (input('Masukkan No Buku: '))
        listvalue = [value for databuku1 in daftarbuku for value in databuku1]
        if nomorbukubaru in listvalue:
            print('Buku Sudah Ada')
        else:
            judulbaru = (input('Judul: '))
            penulisbaru = (input('Penulis: '))
            penerbitbaru = (input('Penerbit: '))
            kategoribaru = (input('Kategori: '))
            ketersediaanbaru = (input('Ketersediaan: '))
            daftarbukubaru = [{
                'No' : nomorbukubaru,
                'Judul' : judulbaru,
                'Penulis' : penulisbaru,
                'Penerbit' : penerbitbaru,
                'Kategori' : kategoribaru,
                "Ketersediaan" : ketersediaanbaru
            }]
            showlist(daftarbukubaru)
            simpan = (input('Simpan Data Buku Baru (Ya/Tidak')).capitalize()
            if simpan == 'Ya':
                daftarbuku.extend(daftarbukubaru)
                showlist(daftarbuku)
                print('Data Buku Baru Sudah Disimpan')
            else:
                print('Data Buku Baru Tidak Disimpan')
    elif inputadd == 2:
        menu()
    add()

# MENGUBAH BUKU
def update():
    inputupdate = (int(input(''' Mengubah Data Buku
    1. Mengubah Data Buku
    2. Kembali''')))
    if inputupdate == 1:
        updatebook = (input('Masukkan No Buku: '))
        listvalue = [value for databuku1 in daftarbuku for value in databuku1]
        if updatebook not in listvalue:
            print('No Buku Tidak Ada')
            update()
        else:
            searchlist(updatebook)
            showlist(searchlist(updatebook))
            inputupdate = (input('update data buku? (Ya/Tidak): ')).capitalize
            if inputupdate == 'Ya':
                inputkategori = int(input('''
                pilihan ubah data:
                1. No
                2. Judul
                3. Penulis
                4. Penerbit
                5. Kategori
                6. Ketersediaan
                Masukkan no pilihan yang ingin diubah: '''))
                if inputkategori == 1:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),1,masukkandata)
                    updatebarang(searchlist(updatebook), 'No', masukkandata)
                elif inputkategori == 2:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),2,masukkandata)
                    updatebarang(searchlist(updatebook), 'Judul', masukkandata)
                elif inputkategori == 3:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),3,masukkandata)
                    updatebarang(searchlist(updatebook), 'Penulis', masukkandata)
                elif inputkategori == 4:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),4,masukkandata)
                    updatebarang(searchlist(updatebook), 'Penerbit', masukkandata)
                elif inputkategori == 5:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),5,masukkandata)
                    updatebarang(searchlist(updatebook), 'Kategori', masukkandata)
                elif inputkategori == 6:
                    masukkandata = input('masukkan data baru: ')
                    showlistupdate(searchlist(updatebook),6,masukkandata)
                    updatebarang(searchlist(updatebook), 'Ketersediaan', masukkandata)
                else:
                    print('pilihan tidak tersedia')
    elif inputupdate == 2:
        menu()
    update()       
        
# MENGHAPUS BUKU
def delete():
    inputdel = (int(input(''' Daftar Data Buku 
    1. Menghapus Data Buku
    2. Kembali
    Masukkan no Menu yang Diinginkan: ''')))
    if inputdel == 1:
        showlist(daftarbuku)
        delbookid = input('masukkan id yang ingin dihapus: ')
        listvalue2 = [value2 for databuku in daftarbuku for value2 in databuku]
        if delbookid not in listvalue2:
            print('Buku tidak ada')
        else:
            searchlist(delbookid)
            showlist(searchlist(delbookid))
            hapus = (input('hapus buku? (Ya/Tidak): ')).capitalize
            if hapus == 'Ya':
                for e in searchlist(delbookid):
                    daftarbuku.remove(e)
                print('data buku sudah dihapus')
            else:
                print('data buku tidak dihapus')
    elif inputdel == 2:
        menu()
    delete()

# EXIT
def exit():
    print('Sampai Jumpa')

# MENU
def menu():
    while True :
        menuutama = input('''Menu Utama Perpustakaan
        
        Daftar Menu:
        1. Daftar Data Buku
        2. Menambah Data Buku
        3. Mengubah Data Buku
        4. Menghapus Data Buku
        5. Keluar
        
        Masukkan no Menu yang Diinginkan: ''')

        if(menuutama == '1') :
            read()
        elif(menuutama == '2') :
            add()
        elif(menuutama == '3') :
            update()
        elif(menuutama == '4') :
            delete()
        elif(menuutama == '5') :
            exit()
        else:
            menu()