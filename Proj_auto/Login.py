from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

def login(driver):
    # Tunggu hingga elemen email muncul dan isi
    email_field = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "login-email")))
    email_field.send_keys('kodenya')
    # Tunggu hingga elemen password muncul dan isi
    password_field = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "login-password")))
    password_field.send_keys('kodenya')
    # Tunggu pengguna menyelesaikan CAPTCHA, kalau ada
    #input("Silakan selesaikan CAPTCHA dan tekan Enter untuk melanjutkan...")

    tombol = driver.find_element(By.CLASS_NAME, 'btn')
    tombol.click()

    try:
        InpData = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Input Data']")))
        InpData.click()
        time.sleep(3)
        Meteorologi = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/meteorologi']")))
        Meteorologi.click()
    except TimeoutException:
    # Jika elemen tidak ditemukan, lewati (pass)
        pass