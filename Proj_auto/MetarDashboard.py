from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys

def metar1(driver,Inp_jam):

    n = Inp_jam + 1
    n = str(n)
    time.sleep(2)
    Mstasiun = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vs2__combobox']//div[@class='vs__actions']//*[name()='svg']")))
    Mstasiun2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vs2__combobox']//input[@type='search']")))
    Mstasiun2.send_keys("kodenya")
    time.sleep(2)
    Mstasiun2.send_keys(Keys.RETURN)
    time.sleep(2)

    #Mobs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vs3__combobox']//div[@class='vs__actions']//*[name()='svg']")))
    #print('pilih2 bisa')
    Mobs2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vs3__combobox']//input[@type='search']")))
    Mobs2.send_keys("usernamenya")
    time.sleep(2)
    Mobs2.send_keys(Keys.RETURN)
    time.sleep(2)
    
    #Tanggal
    MTanggal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="datepicker__value_"]')))
    MTanggal.click()
    time.sleep(2) 
    MTanggal2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='btn border-0 rounded-circle text-nowrap btn-outline-light text-muted'][normalize-space()='29']"))) #tanggal diganti
    time.sleep(2)
    MTanggal2.click()

    #Jam
    MJam = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-jam"]')))
    MJam.click() 
    MJam = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="input-jam"]/option[{n}]')))
    MJam.click()

    #menit
    Mmenit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-menit"]')))
    Mmenit.click() 
    Mmenit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-menit"]/option')))
    Mmenit.click()

    try:
        # Tunggu hingga tombol "View" muncul dalam waktu 10 detik
        View = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[3]/button[1]')))
        View.click()
    except TimeoutException:
        pass

    #print('masih bisa')
    time.sleep(3)

