from controllers import *
from models import *

def addCar():
    print('\nTambah mobil')
    plateNo = input('Nomor plat: ')
    model = input('Model: ')
    price = float(input('Harga/hari: Rp '))
    car = Car(0, plateNo, model, price)
    result = CarController().add(car)

    if result != 0:
        print('Berhasil menambah mobil baru dengan ID', result)
    else:
        print('Maaf, sistem gagal menambah mobil baru')
    
    carMenu()

def editCar():
    print('\nUbah mobil')
    carID = int(input('ID mobil: '))
    plateNo = input('Nomor plat: ')
    model = input('Model: ')
    price = float(input('Harga/hari: Rp '))
    car = Car(carID, plateNo, model, price)
    result = CarController().edit(car)

    if result != 0:
        print('Berhasil mengubah mobil dengan ID', car.getCarID())
    else:
        print('Maaf, sistem gagal mengubah mobil dengan ID', car.getCarID())
    
    carMenu()

def viewCars():
    print('\nLihat mobil')
    cars = CarController().view()

    for car in cars:
        print(car.getCarID(), car.getPlateNo(), car.getModel(), car.getPrice(), sep = '\t')

    carMenu()

def carMenu():
    print('\nManajemen mobil')
    print('1. Tambah mobil')
    print('2. Ubah mobil')
    print('3. Lihat mobil')
    print('4. Kembali ke menu utama')

    choice = input('Silakan pilih menu: ')

    if choice == '1':
        addCar()
    elif choice == '2':
        editCar()
    elif choice == '3':
        viewCars()
    elif choice == '4':
        mainMenu()
    else:
        print('Pilihan tidak dikenal, silakan ulang')
        carMenu()

def mainMenu():
    print('\nMenu utama')
    print('1. Manajemen mobil')
    print('2. Manajemen pelanggan')
    print('3. Manajemen sewa')
    print('4. Keluar')

    choice = input('Silakan pilih menu: ')

    if choice == '1':
        carMenu()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        print("Terima kasih dan selamat tinggal")
        exit()
    else:
        print('Pilihan tidak dikenal, silakan ulang')
        mainMenu()

staffID = input('Masukkan ID staf: ')
password = input('Masukkan password: ')
staff = StaffController().login(staffID, password)

if staff:
    print(f"Selamat datang, {staff.getName()}")
    mainMenu()
else:
    print('ID staf dan password salah')