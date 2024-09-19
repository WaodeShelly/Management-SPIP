# Struktur data awal
data_perusahaan = {
    "Sarana": {
        "Transportasi Darat": ["Bus","Microbus", "Manhaul"],
        "Transportasi Air": ["Speedboat"],
        "Transportasi Support": ["Light Vehicle","Light Truck"]
    },
    "Prasarana": {
        "Bangunan Operasional" : ["Head office","Gedung Penyimpanan", "Mess","Ruang kendali"],
        "Bangunan Support" :  ["Fuel Station", "Rest Area","Pit stop", "Change Shift Pit"],
    },
    "Instalasi": {
        "Instalasi Listrik" : ["Main Office","Mess Facility","Workshop Facility"],
        "Instalasi Pengelolaan Air" : ["IPAL Main Office", "IPAL Site"]
    },  
    "Peralatan Pertambangan": {
        "A2B Track" : ["Bulldozer","Excavator"],
        "A2B Wheel" : ["Dump Truck","Double Trailer","Forklift", "Crane Truck"],
        "Permesinan" : ["Generator Set", "Tower Lamp","Over Head Crane", ]
    }
}

status = ["Aktif","Tidak Aktif","Breakdown"]

# Daftar unit yang telah ditambahkan
daftar_unit = [
    {
        "id" : 1,
        "No SPIP" : "BM-01",
        "Kategori" : "Sarana",
        "Sub kategori" : "Transportasi Darat",
        "Jenis" : "Bus",
        "Status" : "Aktif"
    },
    {
        "id": 2,
        "No SPIP" : "PM-01",
        "Kategori" : "Sarana",
        "Sub kategori" : "Transportasi Darat",
        "Jenis" : "Bus",
        "Status" : "Aktif"
    },

]

#Lihat data struktur unit
def lihat_data():
    print("\nStruktur Data Unit Perusahaan:")
    for Kategori, Subkategori in data_perusahaan.items():
        print(f"Kategori: {Kategori}")
        for sub, jenis in Subkategori.items():
            print(f"  Subkategori: {sub}")
            for j in jenis:
                print(f"    Jenis: {j}")
    print()


# Fungsi untuk menghasilkan ID baru
def generate_new_id(daftar_unit):
    if not daftar_unit:
        return 1
    return max(unit['id'] for unit in daftar_unit) + 1

# Fungsi untuk memeriksa apakah No SPIP sudah ada
def no_spip_ada(no_spip):
    return any(unit['No SPIP'] == no_spip for unit in daftar_unit)

# Fungsi untuk menampilkan Kategori saja
def lihat_kategori():
    print("Berikut list Kategori yang ada pada system:")
    for kategori, subkategori_dict in data_perusahaan.items():
        print(f"{kategori}")


# Fungsi untuk menambahkan unit baru
def tambah_unit():

    #Input No SPIP
    no_spip = input("Masukkan No SPIP: ").upper()
        
     #Validasi No SPIP
    if no_spip_ada(no_spip):
        print("No SPIP sudah ada. Silakan masukkan No SPIP yang lain.")
        return

    # Memilih kategori
    lihat_kategori()
    kategori = input("Pilih kategori dari daftar di atas: ").title()
    if kategori not in data_perusahaan:
        print("Kategori tidak valid.")
        return
    
    # Memilih subkategori
    subkategori_list = list(data_perusahaan[kategori].keys())
    print(f"Subkategori untuk kategori {kategori}: {subkategori_list}")
    subkategori = input("Pilih subkategori dari daftar di atas: ").title()
    if subkategori not in data_perusahaan[kategori]:
        print("Subkategori tidak valid.")
        return
    
    # Memilih jenis
    jenis_list = data_perusahaan[kategori][subkategori]
    if jenis_list:
        print(f"Jenis untuk subkategori {subkategori}: {jenis_list}")
        jenis = input("Pilih jenis dari daftar di atas: ").title()
        if jenis not in jenis_list:
            print("Jenis tidak valid.")
            return
    else:
        jenis = None
    
    # Memilih Status
    global status
    print(f"Pilihan status: {status}")
    status_input = input("Masukkan Status: ").title()
    if status_input not in status:
        print("Status tidak valid.")
        return
    
    # Menambahkan unit baru ke daftar_unit
    new_id = generate_new_id(daftar_unit)
    unit_baru = {
        "id": new_id,
        "No SPIP": no_spip,
        "Kategori": kategori,
        "Sub kategori": subkategori,
        "Jenis": jenis,
        "Status": status_input
    }
    
    daftar_unit.append(unit_baru)
    print("\nUnit berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua unit
def lihat_unit():
    print("\nDaftar Unit Perusahaan:")
    if not daftar_unit:
        print("Tidak ada unit yang tersedia.\n")
    else:
        for idx, unit in enumerate(daftar_unit, start=1):
            print(f"{idx}. ID: {unit['id']}, No SPIP: {unit['No SPIP']}, Kategori: {unit['Kategori']}, Sub Kategori: {unit['Sub kategori']}, Jenis: {unit['Jenis']}, Status: {unit['Status']}")
        print()

# Fungsi untuk menampilkan spefisik unit
def cari_unit(no_spip):
    for unit in daftar_unit:
        if unit["No SPIP"] == no_spip:
            return unit
    return None

def tampilkan_unit(no_spip):
    unit = cari_unit(no_spip)
    if unit:
        print("Data unit ditemukan:")
        print(f"ID: {unit['id']}")
        print(f"No SPIP: {unit['No SPIP']}")
        print(f"Kategori: {unit['Kategori']}")
        print(f"Sub kategori: {unit['Sub kategori']}")
        print(f"Jenis: {unit['Jenis']}")
        print(f"Pilihan status: {status}")
        print(f"Status: {unit['Status']}")
    else:
        print("Unit dengan No SPIP tersebut tidak ditemukan.")

# Fungsi untuk mengupdate unit
def update_unit(no_spip):
    for unit in daftar_unit:
        if unit["No SPIP"] == no_spip:
            print(f"Unit ditemukan: {unit}")
            
            # Update No SPIP
            unit["No SPIP"] = input("Masukkan No SPIP baru: ").upper()

            # Update kategori
            lihat_kategori()
            kategori_baru = input("Masukkan Kategori baru: ").title()
            if kategori_baru not in data_perusahaan:
                print("Kategori tidak valid.")
                return
            unit["Kategori"] = kategori_baru

            # Update subkategori
            subkategori_list = list(data_perusahaan[kategori_baru].keys())
            print(f"Subkategori untuk kategori {kategori_baru}: {subkategori_list}")
            subkategori_baru = input("Masukkan Sub Kategori baru: ").title()
            if subkategori_baru not in data_perusahaan[kategori_baru]:
                print("Subkategori tidak valid.")
                return
            unit["Sub kategori"] = subkategori_baru

            # Update jenis
            jenis_list = data_perusahaan[kategori_baru][subkategori_baru]
            print(f"Jenis untuk subkategori {subkategori_baru}: {jenis_list}")
            jenis_baru = input("Masukkan Jenis baru: ").title()
            if jenis_baru not in jenis_list:
                print("Jenis tidak valid.")
                return
            unit["Jenis"] = jenis_baru

            # Update status
            print(f"Pilihan status: {status}")
            status_baru = input("Masukkan Status baru: ").title()
            if status_baru not in status:
                print("Status tidak valid.")
                return
            unit["Status"] = status_baru

            print("Data unit berhasil diperbarui.\n")
            return

    print("\nUnit dengan No SPIP tersebut tidak ditemukan.\n")

# Fungsi untuk menghapus unit
def hapus_unit(no_spip):
    for unit in daftar_unit:
        if unit["No SPIP"] == no_spip:
            daftar_unit.remove(unit)
            print("Unit berhasil dihapus.\n")
            return
    print("Unit dengan No SPIP tersebut tidak ditemukan.\n")
        
# Fungsi utama untuk mengelola menu CRUD
def menu():
    while True:
        print("\n-------- Program Data Unit Perusahaan --------")
        print("1. Lihat Struktur Data Unit Perusahaan")
        print("2. Lihat Daftar Unit")
        print("3. Tambah Unit")
        print("4. Ubah Data Unit")
        print("5. Hapus Data Unit")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            lihat_data()
        
        elif pilihan == "2":
            menu_lihat()
        
        elif pilihan == "3":
            menu_tambah()
        
        elif pilihan == "4":
            menu_edit()

        elif pilihan == '5':
            menu_hapus()
            
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Fungsi detail lihat untuk mengelola menu CRUD
def menu_lihat():
    while True:
        print("\n++++++++ Menu Lihat Daftar Unit Perusahaan ++++++++")
        print("1. Daftar Unit Perusahaan")
        print("2. Melihat Data Unit tertentu")
        print("3. Kembali ke Menu Utama")
        
        pilihanA = input("Pilih menu (1-3): ")
        
        if pilihanA == "1":
            lihat_unit()
        
        elif pilihanA == "2":
            no_spip_input = input("Masukkan No SPIP untuk mencari unit: ").upper()
            tampilkan_unit(no_spip_input)
        
        elif pilihanA == "3":
            menu()
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Fungsi detail tambah untuk mengelola menu CRUD
def menu_tambah():
    while True:
        print("\n++++++++ Menu Tambah Unit Perusahaan ++++++++")
        print("1. Menambah Data Unit")
        print("2. Kembali ke Menu Utama")

        pilihanB = input("Pilih menu (1-2): ")
        
        if pilihanB == "1":
            tambah_unit()
        
        elif pilihanB == "2":
            menu()
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Fungsi detail update untuk mengelola menu CRUD
def menu_edit():
    while True:
        print("\n++++++++ Menu Edit Unit Perusahaan ++++++++")
        print("1. Merubah Data Unit tertentu")
        print("2. Kembali ke Menu Utama")

        pilihanC = input("Pilih menu (1-2): ")
        
        if pilihanC == "1":
            no_spip_input = (input("Masukkan No SPIP unit yang ingin diperbarui: ")).upper()
            update_unit(no_spip_input)
        
        elif pilihanC == "2":
            menu()
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Fungsi detail Hapus untuk mengelola menu CRUD
def menu_hapus():
    while True:
        print("\n++++++++ Menu Hapus Unit Perusahaan ++++++++")
        print("1. Menghapus Data Unit tertentu")
        print("2. Kembali ke Menu Utama")

        pilihanD = input("Pilih menu (1-2): ")
        
        if pilihanD == "1":
            no_spip_input = (input("Masukkan No SPIP unit yang ingin dihapus: ")).upper()
            hapus_unit(no_spip_input)
        
        elif pilihanD == "2":
            menu()
        
        else:
            print("Pilihan tidak valid. Coba lagi.")


# Menjalankan program
menu()



