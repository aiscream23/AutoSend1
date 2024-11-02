from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def metar4(driver, Inp_tbk, Inp_qff, TD):

    #TD3 = 22.9, hanya uji coba td3
    #Angin
    TBK = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='v-air-temp']")))
    TBK.clear()
    TBK.send_keys(str(Inp_tbk))

    TD2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='v-dew-point']")))
    TD2.clear()
    TD2.send_keys(str(TD))

    QNH2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='v-presure']")))
    QNH2.clear()
    QNH2.send_keys(str(Inp_qff))

