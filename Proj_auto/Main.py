from selenium import webdriver
import openpyxl
import time
from datetime import datetime, timedelta

# Import fungsi dari modul
from Login import login
from Dashboard import Dashboard
from Angin import angin
from Cuaca import cuaca
from Tekanan import Tekanan
from Suhu import Suhu_d
from Middle import middle_d
from AwanRendah import AwanRendah
from AwanMenengah import AwanMenengah
from AwanTinggi import AwanTinggi
from Bottom import Bottom_d
from Last import Send
# metar 
from MetarDashboard import metar1
from MetarAngin import metar2
from MetarAwan import metar3
from MetarSuhu import metar4
from MetarSend import metar5

# Path ke file Excel
file_path = 'Input.xlsx'
workbook = openpyxl.load_workbook(file_path)
sheets = workbook.sheetnames

def get_data(sheet, jam):
    """Mengambil data dari sheet yang diberikan dan menambahkan waktu 'Inp_jam'."""
    data = {
        'Inp_iw': sheet['B1'].value,
        'Inp_dr': sheet['B2'].value,
        'Inp_dr2': sheet['B3'].value,
        'Inp_dr3': sheet['B4'].value,
        'Inp_ww': sheet['D2'].value,
        'Inp_W11': sheet['D3'].value,
        'Inp_W21': sheet['D4'].value,
        'Inp_qff': sheet['F3'].value,
        'Inp_qfe': sheet['F4'].value,
        'Inp_tbk': sheet['H1'].value,
        'Inp_tbb': sheet['H2'].value,
        'Inp_tmax': sheet['H3'].value,
        'Inp_tmin': sheet['H4'].value,
        'Inp_okt': sheet['B6'].value,
        'Inp_mm': sheet['D6'].value,
        'Opsi': sheet['B8'].value,
        'Opsi2': sheet['B9'].value,
        'Opsi3': sheet['B10'].value,
        'Opsi4': sheet['B11'].value,
        'Opsi5': sheet['B12'].value,
        'Opsi6': sheet['B13'].value,
        'Opsi7': sheet['B14'].value,
        'Opsi8': sheet['B15'].value,
        'Opsi9': sheet['B16'].value,
        'Opsim': sheet['D8'].value,
        'Opsi2m': sheet['D9'].value,
        'Opsi3m': sheet['D10'].value,
        'Opsi4m': sheet['D11'].value,
        'Opsi5m': sheet['D12'].value,
        'Opsi6m': sheet['D13'].value,
        'Opsih': sheet['F8'].value,
        'Opsih2': sheet['F9'].value,
        'Opsih3': sheet['F10'].value,
        'Opsih4': sheet['F11'].value,
        'Opsih5': sheet['F12'].value,
        'Opsih6': sheet['F13'].value,
        'Inp_Penguapan': sheet['B18'].value,
        'Inp_IE': sheet['B19'].value,
        'Inp_Jam': sheet['D19'].value,
        'Inp_tanah': sheet['F18'].value,
        'Inp_jam': jam,  # Menggunakan jam yang dinamis,
        'hCL' : sheet['B22'].value,
        'hCM' : sheet['B23'].value
    }
    return data

# Inisialisasi driver
driver = webdriver.Chrome()
driver.maximize_window()
link = 'https://bmkgsatu.bmkg.go.id/dashboard'
driver.get(link)
login(driver)

# Waktu awal (misalnya dimulai dari jam 19)
start_hour = 19 #mulai jamnya, acuan UTC

# Iterasi per menit untuk setiap sheet yang ada
for i in range(len(sheets)):
    sheet = workbook[sheets[i]]
    current_hour = start_hour + i  # Tambahkan i ke start_hour untuk setiap iterasi
    data = get_data(sheet, current_hour)
    
    # Jalankan otomatisasi berdasarkan data yang diambil
    Dashboard(driver, data['Inp_jam'])
    angin(driver, data['Inp_iw'], data['Inp_dr'], data['Inp_dr2'], data['Inp_dr3'])
    cuaca(driver, data['Inp_ww'], data['Inp_W11'], data['Inp_W21'])
    Tekanan(driver, data['Inp_qff'], data['Inp_qfe'])
    Suhu_d(driver, data['Inp_tbk'], data['Inp_tbb'], data['Inp_tmax'], data['Inp_tmin'])
    middle_d(driver, data['Inp_okt'], data['Inp_mm'])
    AwanRendah(driver, data['Opsi'], data['Opsi2'], data['Opsi3'], data['Opsi4'], data['Opsi5'], data['Opsi6'], data['Opsi7'], data['Opsi8'], data['Opsi9'])
    AwanMenengah(driver, data['Opsim'], data['Opsi2m'], data['Opsi3m'], data['Opsi4m'], data['Opsi5m'], data['Opsi6m'])
    AwanTinggi(driver, data['Opsih'], data['Opsih2'], data['Opsih3'], data['Opsih4'], data['Opsih5'], data['Opsih6'])
    Bottom_d(driver, data['Inp_Penguapan'], data['Inp_IE'], data['Inp_Jam'], data['Inp_tanah'])
    TD = Send(driver)

    time.sleep(3)

    print(f'Form diisi untuk Sheet {sheets[i]} pada jam {data["Inp_jam"]}')

    #Metar
    driver.get('https://bmkgsatu.bmkg.go.id/meteorologi/metarspeci')
    metar1(driver, data['Inp_jam'])
    metar2(driver, data['Inp_dr'], data['Inp_dr2'], data['Inp_dr3'])
    metar3(driver, data['Opsi2'], data['hCL'], data['Opsi2m'], data['hCM'])
    metar4(driver, data['Inp_tbk'], data['Inp_qff'], TD)
    metar5(driver)

    #kembali ke dashboard sinop
    driver.get('https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik')

    # Ganti bagian ini di dalam loop:
    if i < len(sheets) - 1:
        next_time = datetime.now() + timedelta(seconds=3600) #sesuaikan dengan waktunya, acuan dari berjalannya script
        time.sleep((next_time - datetime.now()).total_seconds())

# Tutup browser setelah semua sheet selesai diproses
driver.quit()
