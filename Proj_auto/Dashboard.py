from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

def Dashboard(driver, Inp_jam):

    #Stasiun
    time.sleep(3)
    stasiun = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='select-station']//i[@aria-label='icon: down']//*[name()='svg']")))
    stasiun.click()
    AndJm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[normalize-space()='Stasiun Meteorologi Andi Jemma']")))
    AndJm.click()

    time.sleep(3)
    #Nama OBS
    Obs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div")))
    Obs.click()

    Nama = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='select-observer']//input[@class='ant-select-search__field']")))  # Sesuaikan XPath dengan elemen input
    Nama.send_keys("usernamenya")
    Nama.send_keys(Keys.RETURN)
    
    #Tanggal
    Tanggal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[@id='input-datepicker__value_']")))
    Tanggal.click() 
    Tanggal2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='btn border-0 rounded-circle text-nowrap btn-outline-light text-muted'][normalize-space()='29']")))#tanggal diganti
    Tanggal2.click()


    #Jam
    Jam = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='input-jam']//div[@class='ant-select-selection__rendered']")))
    Jam.click()
    Jam2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-jam"]/div/div/div[2]/div/input')))
    Jam2.send_keys(str(Inp_jam))
    time.sleep(1)
    Jam2.send_keys(Keys.RETURN)

    try:
        # Tunggu hingga tombol "View" muncul dalam waktu 10 detik
        View = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View']")))
        View.click()
    except TimeoutException:
    # Jika elemen tidak ditemukan, lewati (pass)
        print('uji coba')
        pass