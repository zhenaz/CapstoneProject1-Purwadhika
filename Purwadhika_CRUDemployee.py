# Benazheer Salsabila
# Library yang digunakan hanya untuk memperapih tampilan
import os
from time import sleep
from tabulate import tabulate


# db
karyawan = [
    {
        'NIP': '0001',
        'Nama': 'Benazheer Salsabila',
        'Gender': 'Wanita',
        'Divisi' : 'IT',
        'Level' : '',
        'Gaji' : 'Rp 18.000.000',
        'Status' : 'Admin',
        'Password': '123'
    },
    {
        'NIP': '0003',
        'Nama': 'Luthfi Hardiansyah',
        'Gender': 'Pria',
        'Divisi': 'IT',
        'Level': 'Manager',
        'Gaji': 'Rp 20.000.000',
        'Status': 'Karyawan',
        'Password': '123'
    },
    {
        'NIP': '0009',
        'Nama': 'Eklesias Fressdiarin',
        'Gender': 'Wanita',
        'Divisi': 'HR',
        'Level': 'Manager',
        'Gaji': 'Rp 18.000.000',
        'Status': 'Karyawan',
        'Password': '123'
    },
    {
        'NIP': '0007',
        'Nama': 'Alfina ferra',
        'Gender': 'Wanita',
        'Divisi': 'HR',
        'Level': 'Staf',
        'Gaji': 'Rp 12.000.000',
        'Status': 'Karyawan',
        'Password': '123'
    },
]

logged_data = []

# login
def login():
    os.system('cls')
    while True:
        print("************************************************************")
        print("                     Selamat Datang!")
        print("                   Aplikasi Kepegawaian")
        print("************************************************************")
        print("Silahkan login untuk memulai")
        uname = input("Masukkan NIP: ")
        check_nip(uname)
        print("************************************************************")

def check_nip(input_nip):
    index_perulangan = 0
    for data_karyawan in karyawan:
        index_perulangan +=1
        if input_nip == data_karyawan['NIP']:
            input_pwd = input("Masukkan password: ")
            is_pwd_valid = check_pwd(input_pwd, data_karyawan)

            if (is_pwd_valid):
                global logged_data
                logged_data = data_karyawan
                if(data_karyawan['Status'] == 'Admin'):
                    menu_utama()
                    break
                else:
                    menu_karyawan()
                    break
            else:
                break
        else:
            if (len(karyawan) == index_perulangan):
                print(f"Pengguna dengan nip {input_nip} tidak ditemukan.")
                # break

def check_pwd(input_pwd, data_karyawan):
    if(data_karyawan['Password'] == input_pwd):
        return True
    else:
        print(f"Password salah!")
        sleep(2.0)
        os.system('cls')



# dashboard
def menu_utama():
    while True:
        os.system('cls')
        print("************************************************************")
        print("                   Aplikasi Kepegawaian")
        print("************************************************************")
        print(f"Anda Login Sebagai {logged_data['Nama']} ({logged_data['Status']})")
        print("\nList Menu :")
        print("1. Data Karyawan")
        print("2. Tambah Data Karyawan")
        print("3. Perbarui Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Keluar")
        pilihan = input("Masukkan Menu Yang Ingin Anda Akses: ")
        print("************************************************************")
        # Read
        if pilihan == "1":
            os.system('cls')
            while True:
                print("********************* Data Karyawan ************************")
                print("1. Tampilkan Semua karyawan")
                print("2. Cari karyawan")
                print("3. Kembali ke Menu Utama")
                pilihan2 = input("Masukkan pilihan Anda: ")
                if pilihan2 == "1":
                    show_karyawan()
            
                elif pilihan2 == "2":
                    nip = input("Masukkan nip karyawan untuk dicari: ")
                    show_karyawan_nip(nip)
            
                elif pilihan2 == "3":
                    break
        # Create
        elif pilihan == "2":
            os.system('cls')
            while True:
                print("******************* Tambah Data Karyawan *******************")
                print("1. Tambahkan Data karyawan")
                print("2. Kembali ke Menu Utama")
                pilihan = input("Masukkan pilihan Anda: ")
            
                if pilihan == "1":
                    nip = input("Masukkan nip karyawan: ")
                    nama = input("Masukkan nama karyawan: ")
                    gender = input("Masukkan Gender karyawan (Pria/Wanita): ")
                    divisi = input("Masukkan divisi karyawan: ")
                    level = input("Masukkan level karyawan: ")
                    gaji = input("Masukkan gaji karyawan: ")
                    status = input("Masukkan status karyawan: ")
                    password = '123'

                    add_karyawan(nip, nama, gender, divisi, level, gaji, status, password)
                    sleep(2.0)
                    os.system('cls')

                elif pilihan == "2":
                    break

        # Update
        elif pilihan == "3":
            os.system('cls')
            while True:
                print("***************** Perbarui Data Karyawan *****************")
                print("1. Ubah Data karyawan")
                print("2. Kembali ke Menu Utama")
                pilihan = input("Masukkan pilihan Anda: ")
            
                if pilihan == "1":
                    nip = input("Masukkan nip yang akan diperbarui: ")
                    tampil = show_karyawan_nip(nip)
                    if tampil:
                        update_karyawan(nip)
                        sleep(2.0)
                        os.system('cls')
                    else:
                          pass

                elif pilihan == "2":
                    break

        # Delete
        elif pilihan == "4":
            os.system('cls')
            while True:
                print("*************** Hapus Data Karyawan *******************")
                print("1. Hapus Data karyawan")
                print("2. Kembali ke Menu Utama")
                pilihan = input("Masukkan pilihan Anda: ")
            
                if pilihan == "1":
                    nip = input("Masukkan nip yang akan dihapus: ")
                    tampil = show_karyawan_nip(nip)
                    if tampil:
                        input_ = input("Apakah anda yakin untuk hapus data karyawan ini? (y/n) ")
                        if input_.lower() == 'y':
                            hapus_karyawan(nip)
                            sleep(2.0)
                            os.system('cls')
                        else:
                            pass
                elif pilihan == "2":
                    break

        elif pilihan == "5":            
            os.system('cls')
            login()

        else:
            print("Pilihan tidak valid. Silakan anda pilih opsi yang valid.")  

def menu_karyawan():
    while True:
        os.system('cls')
        print("************************************************************")
        print("                   Aplikasi Kepegawaian")
        print("************************************************************")
        print(f"Anda Login Sebagai {logged_data['Nama']} ({logged_data['Status']})")
        print("\nList Menu :")
        print("1. Data Karyawan")
        print("2. Ubah Password")
        print("3. Keluar")
        pilihan = input("Masukkan Menu Yang Ingin Anda Akses: ")
        print("************************************************************")
        if pilihan == "1":
            os.system('cls')
            print("********************** Data Pribadi ************************")
            for key, value in logged_data.items():
                if key != "NIP":
                    print(f"{key}: {value}")
            print("************************************************************")
            print("1. Kembali ke Menu Utama")
            while True:
                pilihan = input("Masukkan pilihan Anda: ")
            
                if pilihan == "1":
                    break
                else :
                    print("Pilihan tidak valid. Silakan anda pilih opsi yang valid.")  
        elif pilihan == "2":
            new_pwd = input("Masukkan Password baru anda : ")
            confirm_pwd = input("Masukkan Password baru anda lagi : ")
            is_changed = change_password(new_pwd, confirm_pwd)
            if(is_changed) :
                print('Password berhasil diubah!')
            else :
                print('Password gagal diubah! Konfirmasi password tidak sesuai dengan yang diketikkan!')

        elif pilihan == "3":
            os.system('cls')
            login()

        else:
            print("Pilihan tidak valid. Silakan anda pilih opsi yang valid.")  

def show_karyawan():
    header = ["NIP", "Nama", "Gender", "Divisi", "Level", "Gaji", "Status"]
    rows = []
    # Sorting
    karyawan.sort(key=lambda sorting: sorting['NIP'])

    for data_karyawan in karyawan:
        row = [data_karyawan['NIP'], data_karyawan['Nama'], data_karyawan['Gender'], data_karyawan['Divisi'], data_karyawan['Level'], data_karyawan['Gaji'], data_karyawan['Status']]
        rows.append(row)
    print(tabulate(rows, header, tablefmt="grid"))

def show_karyawan_nip(input_nip):
    os.system('cls')
    header = ["nip", "Nama", "Gender", "divisi", "level", "gaji", "status"]
    rows = []

    for data_karyawan in karyawan:
        if input_nip in data_karyawan['NIP']:
            row = [data_karyawan['NIP'], data_karyawan['Nama'], data_karyawan['Gender'], data_karyawan['Divisi'], data_karyawan['Level'], data_karyawan['Gaji'], data_karyawan['Status']]
            rows.append(row)

    if rows:
        print(tabulate(rows, header, tablefmt="grid"))
        return True
    else:
        print(f"karyawan dengan nip {input_nip} tidak ditemukan.")
        return False

def add_karyawan(nip, nama, gender, divisi, level, gaji, status, password):
    while True:
        if gender.lower() == 'pria' or gender.lower() == 'wanita':
            if(status.lower() == 'admin' or status.lower() == 'karyawan'):
                if nip.isdigit() and gaji.isdigit():
                    if not any(data_karyawan['NIP'] == nip for data_karyawan in karyawan):
                        data_karyawan = {
                            'NIP': nip,
                            'Nama': nama.capitalize(),
                            'Gender': gender.capitalize(),
                            'Divisi': divisi.capitalize(),
                            'Level': level.capitalize(),
                            'Gaji': format_uang(gaji),
                            'Status': status.capitalize(),
                            'Password' : password,
                        }
                        karyawan.append(data_karyawan)
                        print("\nkaryawan berhasil ditambahkan!\n")
                        break
                    else:
                        print("Nip sudah ada dalam daftar karyawan.")
                        break
                else:
                    print("Nip atau gaji harus terdiri dari angka")
                    break
            else: 
                print("Status harus karyawan atau admin!")
                break

        else:
            print("Gender harus 'Pria' atau 'Wanita'!")
            break
    print("************************************************************")


def update_karyawan(nip):
    for data_karyawan in karyawan:
        if data_karyawan["NIP"] == nip:
            print("Data karyawan yang ingin diubah:")
            for key, value in data_karyawan.items():
                if key != "NIP":
                    print(f"{key}: {value}")
            print("************************************************************")
            kolom = input("Masukkan nama kolom yang ingin diubah: ").title()

            if kolom in data_karyawan:
                data_baru = input(f"Masukkan data baru untuk {kolom}: ")

                if(kolom.lower() == 'gaji'):
                    if data_baru.isdigit():
                        data_baru = format_uang(data_baru)
                    else :
                        print(f"Data {kolom} harus berupa digit!")
                        break

                pilihan = input(f"Apakah anda yakin ingin mengubah data {kolom} : {data_karyawan[kolom]} dengan {kolom} : {data_baru} ? (y/n) ")
                if pilihan.lower() == 'y':
                    data_karyawan[kolom] = data_baru.capitalize()
                    print("\nData karyawan berhasil diubah!\n")
                else:
                    print("\nData tidak jadi diubah!\n")
                    break
            else:
                print("Kolom tidak valid.")
            break
    else:
        print("karyawan dengan nip tersebut tidak ditemukan.")

def hapus_karyawan(nip):
    for data_karyawan in karyawan:
        if data_karyawan['NIP'] == nip :
            if(data_karyawan['NIP'] != logged_data['NIP']):
                karyawan.remove(data_karyawan)
                print("\nkaryawan berhasil dihapus!\n")
                break
            else :
                print("\nTidak dapat menghapus data diri sendiri!\n")
                break
    else:
        print("karyawan tidak ditemukan.") 

def change_password(new_pwd, confirm_pwd):
    if(new_pwd == confirm_pwd) :
        logged_data['Password'] = new_pwd
        print('password berhasil diubah')
        sleep(2.0)
    else :
        print('password gagal diubah! password konfirmasi salah')
        sleep(2.0)
    
def format_uang(gaji):
    string_gaji = str(gaji)
    jml_setelah_desimal = len(string_gaji) % 3

    formatted_gaji = "Rp "

    for i, digit in enumerate(string_gaji):
        if i > 0 and (i - jml_setelah_desimal) % 3 == 0:
            formatted_gaji += "."

        formatted_gaji += digit

    return formatted_gaji

# run
login()
