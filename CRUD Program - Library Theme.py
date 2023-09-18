daftar_buku = [{'KODE' : '001',
        'JUDUL' : 'Laskar Rainbow',
        'PENULIS' : 'Andrea Hirata',
        'PENERBIT' : 'Bentang Pustaka',
        'KATEGORI' : 'Novel',
        'STATUS' : 'Tersedia'
    },
]

# FUNGSI LIST BUKU
def listbuku(databuku1):
    for i in range(len(databuku1)) :
        print('\n\tKODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(databuku1[i]['KODE'], databuku1[i]['JUDUL'], databuku1[i]['PENULIS'], databuku1[i]['PENERBIT'], databuku1[i]['KATEGORI'], databuku1[i]['STATUS']))

# FUNGSI FILTER BUKU
def filter_buku(databuku2):
    filter_list = []
    for data in daftar_buku:
        if data['KODE'] == str(databuku2):
            filter_list.append(data)
    return filter_list

# FUNGSI UPDATE
def updatebuku(data, Kategori_Pilih, databaru):
    inputan_updatebuku = input('\nApakah Data Sudah Benar? (Ya/Tidak): ').capitalize()
    if inputan_updatebuku == 'Ya':
        data[0][Kategori_Pilih] = databaru
        print('\nData Sudah Diperbarui')
    else:
        print('\nData Tidak Diperbarui')

# FUNGSI LIST UPDATE
def listbuku_update(listbuku, Nomor_Kategori, dataupdate):
    if Nomor_Kategori == 1:
        for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(dataupdate,listbuku[i]['JUDUL'], listbuku[i]['PENULIS'], listbuku[i]['PENERBIT'], listbuku[i]['KATEGORI'], listbuku[i]['STATUS']))
    elif Nomor_Kategori == 2:
         for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(listbuku[i]['KODE'], dataupdate, listbuku[i]['PENULIS'], listbuku[i]['PENERBIT'], listbuku[i]['KATEGORI'], listbuku[i]['STATUS']))
    elif Nomor_Kategori == 3:
         for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(listbuku[i]['KODE'], listbuku[i]['JUDUL'], dataupdate, listbuku[i]['PENERBIT'], listbuku[i]['KATEGORI'], listbuku[i]['STATUS']))
    elif Nomor_Kategori == 4:
         for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(listbuku[i]['KODE'], listbuku[i]['JUDUL'], listbuku[i]['PENULIS'], dataupdate, listbuku[i]['KATEGORI'], listbuku[i]['STATUS']))
    elif Nomor_Kategori == 5:
         for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(listbuku[i]['KODE'], listbuku[i]['JUDUL'], listbuku[i]['PENULIS'], listbuku[i]['PENERBIT'], dataupdate, listbuku[i]['STATUS']))
    elif Nomor_Kategori == 6:
         for i in range(len(listbuku)):
            print('\n KODE: {} JUDUL: {} PENULIS: {} PENERBIT: {} KATEGORI: {} STATUS: {}'.format(listbuku[i]['KODE'], listbuku[i]['JUDUL'], listbuku[i]['PENULIS'], listbuku[i]['PENERBIT'], listbuku[i]['KATEGORI'], dataupdate))


# DAFTAR BUKU
def read():
    inputan_read = (int(input('''
    Daftar Data Buku 

    1. Daftar Semua Buku
    2. Kembali

    Masukkan Nomor Menu yang Diinginkan: ''')))
    if inputan_read == 1 and len(daftar_buku):
        listbuku(daftar_buku)
    elif inputan_read == 2:
        menu()
    else:
        print('\n\tNomor yang Dimasukkan Tidak Sesuai')
    read()

# MENAMBAH BUKU
def create():
    inputan_create = (int(input('''
        Menambah Data Buku
        
        1. Menambah Data Buku
        2. Kembali
        
        Masukkan Nomor Menu yang Diinginkan: ''')))
    if inputan_create == 1:
            nomorbukubaru = input('\nKode: ')
            for nobuku1 in daftar_buku:
                if nobuku1['KODE'] == nomorbukubaru:
                    print('\nKode Buku Sudah Terdaftar')
                    create()
                else:
                    continue
            judulbaru = (input('Judul: '))
            penulisbaru = (input('Penulis: '))
            penerbitbaru = (input('Penerbit: '))
            kategoribaru = (input('Kategori: '))
            ketersediaanbaru = (input('Status: '))
            daftarbukubaru = [{
                'KODE' : nomorbukubaru,
                'JUDUL' : judulbaru,
                'PENULIS' : penulisbaru,
                'PENERBIT' : penerbitbaru,
                'KATEGORI' : kategoribaru,
                'STATUS' : ketersediaanbaru
            }]
            listbuku(daftarbukubaru)
            simpan = input('\nSimpan Data Buku Baru (Ya/Tidak): ').capitalize()
            if simpan == 'Tidak':
                print("\nData Buku Tidak Jadi Disimpan")
            elif simpan == 'Ya':
                print('\nData Buku Baru Sudah Disimpan')
                daftar_buku.extend(daftarbukubaru)
                create()    
            else:
                print('\nMasukkan Ya atau Tidak')
    elif inputan_create == 2:
        menu()
    else:
        print('\n\tNomor yang Dimasukkan Tidak Sesuai')
    create()

# MENGUBAH BUKU
def update():
    inputan_update = (int(input('''
    Mengubah Data Buku
    
    1. Mengubah Data Buku
    2. Kembali
    
    Masukkan Nomor Menu Yang Diinginkan: ''')))
    if inputan_update == 1:
        input_update = input('\nMasukkan Kode Buku: ')
        list_nobuku = [nobuku1['KODE'] for nobuku1 in daftar_buku]
        if input_update in list_nobuku:
                filter_buku(input_update)
                listbuku(filter_buku(input_update))
                inputan_update = (input('\nUpdate Data Buku? (Ya/Tidak): ')).capitalize()
                if inputan_update == 'Ya':
                    inputan_kategori = int(input('''
                Pilihan Ubah Data:
                
                1. Kode
                2. Judul
                3. Penulis
                4. Penerbit
                5. Kategori
                6. Status

                Masukkan Nomor Pilihan yang Ingin Diubah: '''))
                    if inputan_kategori == 1:
                        update_keys = input('\nMasukkan Kode Baru: ')
                        listbuku_update(filter_buku(input_update),1,update_keys)
                        updatebuku(filter_buku(input_update), 'KODE', update_keys)
                    elif inputan_kategori == 2:
                        update_keys = input('\nMasukkan Judul Baru: ')
                        listbuku_update(filter_buku(input_update),2,update_keys)
                        updatebuku(filter_buku(input_update), 'JUDUL', update_keys)
                    elif inputan_kategori == 3:
                        update_keys = input('\nMasukkan Penulis Baru: ')
                        listbuku_update(filter_buku(input_update),3,update_keys)
                        updatebuku(filter_buku(input_update), 'PENULIS', update_keys)
                    elif inputan_kategori == 4:
                        update_keys = input('\nMasukkan Penerbit Baru: ')
                        listbuku_update(filter_buku(input_update),4,update_keys)
                        updatebuku(filter_buku(input_update), 'PENERBIT', update_keys)
                    elif inputan_kategori == 5:
                        update_keys = input('\nMasukkan Kategori Baru: ')
                        listbuku_update(filter_buku(input_update),5,update_keys)
                        updatebuku(filter_buku(input_update), 'KATEGORI', update_keys)
                    elif inputan_kategori == 6:
                        update_keys = input('\nMasukkan Status Baru: ')
                        listbuku_update(filter_buku(input_update),6,update_keys)
                        updatebuku(filter_buku(input_update), 'STATUS', update_keys)
                    else:
                        print('\nPilihan Tidak Tersedia')
                else:
                    update()
        else:
            print('\nData Tidak Ada')
            update()
    elif inputan_update == 2:
        menu()
    else:
        print('\n\tNomor yang Dimasukkan Tidak Sesuai')    
    update()    
        
# MENGHAPUS BUKU
def delete():
    inputan_delete = (int(input('''
    Daftar Data Buku 
    
    1. Menghapus Data Buku
    2. Kembali
    
    Masukkan Nomor Menu yang Diinginkan: ''')))
    if inputan_delete == 1:
        listbuku(daftar_buku)
        hapusbuku = input('\nMasukkan Kode Buku yang Ingin Dihapus: ')
        list_nobuku = [nobuku1['KODE'] for nobuku1 in daftar_buku]
        if hapusbuku not in list_nobuku:
            print('\nBuku Tidak ada')
        else:
            filter_buku(hapusbuku)
            listbuku(filter_buku(hapusbuku))
            hapus = (input('\nHapus Buku? (Ya/Tidak): ')).capitalize()
            if hapus == 'Ya':
                for i in filter_buku(hapusbuku):
                    daftar_buku.remove(i)
                print('\nData Buku Sudah Dihapus')
            else:
                print('\nData Buku Tidak Jadi Dihapus')
    elif inputan_delete == 2:
        menu()
    else:
        print('\n\tNomor yang Dimasukkan Tidak Sesuai')
    delete()

# MENU
def menu():
    while True :
        menuutama = input('''
    Menu Utama Perpustakaan
        
    Daftar Menu:
    1. Daftar Data Buku
    2. Menambah Data Buku
    3. Mengubah Data Buku
    4. Menghapus Data Buku
    5. Keluar
        
    Masukkan Nomor Menu yang Diinginkan: ''')

        if(menuutama == '1') :
            read()
        elif(menuutama == '2') :
            create()
        elif(menuutama == '3') :
            update()
        elif(menuutama == '4') :
            delete()
        elif(menuutama == '5') :
            print('\n\tKELUAR DARI PROGRAM\n')
            quit()
        else:
            print('\nNomor yang Dimasukkan Tidak Sesuai')
            menu()

menu()
