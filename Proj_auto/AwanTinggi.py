from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def AwanTinggi(driver, Opsih, Opsih2, Opsih3, Opsih4, Opsih5, Opsih6):
    CL = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_high_type_ch']//i[@aria-label='icon: down']//*[name()='svg']")))
    time.sleep(0.5)
    CL.click()

    Opsi = Opsih #Jenis awan menengah
    Opsi2 = Opsih2 #Jumlah awan menengah yang menutupi langit dalam oktas
    Opsi3 = Opsih3 #Jenis awan C untuk jenis awan menengah
    Opsi4 = Opsih4 #Jumlah awan menengah untuk jenis awan C yang dipilih dalam oktas
    Opsi5 = Opsih5 #Tinggi dasar untuk jenis awan C yang dipilih dalam meter
    Opsi6 = Opsih6 #Arah dari mana awan CH bergerak
    
    if Opsi == 0:
        #pembuka aja ini
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_high_type_ch"]/div/div/div[2]/div/input')))
        CL2.send_keys(str(Opsi))
        CL2.send_keys(Keys.RETURN)
        time.sleep(1)
    elif Opsi == 1:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_high_type_ch"]/div/div/div[2]/div/input')))
        CL2.send_keys(str(Opsi))
        CL2.send_keys(Keys.RETURN)

        NCL21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_high_cover_oktas']//i[@aria-label='icon: down']//*[name()='svg']")))
        time.sleep(0.5)
        NCL21.click()
        time.sleep(0.5)
        NCL22 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_high_cover_oktas"]/div/div/div[2]/div/input')))
        NCL22.send_keys(str(Opsi2))
        NCL22.send_keys(Keys.RETURN)
             
        NCL31 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[3]/div/div)[3]')))  
        time.sleep(0.5)   
        NCL31.click()
        time.sleep(0.5)
        NCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[3]/div/div/div/div[2]/div/input)[3]')))
        NCL3.send_keys(str(Opsi3))
        NCL3.send_keys(Keys.RETURN)
        
        NCL41 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[4]/div/div/div)[3]')))
        time.sleep(0.5)
        NCL41.click()
        time.sleep(0.5)
        NCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select ant-select-open ant-select-focused ant-select-enabled is-valid']//input[@class='ant-select-search__field']")))
        NCL4.send_keys(str(Opsi4))
        NCL4.send_keys(Keys.RETURN)
        
        TDA = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_high_base_1"]')))
        TDA.clear()
        TDA.send_keys(str(Opsi5))
        
        DEG = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[6]/div/div)[2]')))
        time.sleep(0.5)
        DEG.click()
        time.sleep(1)
        DEG2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select ant-select-open ant-select-focused ant-select-enabled is-valid']//input[@class='ant-select-search__field']"))) 
        DEG2.send_keys(str(Opsi6))
        DEG2.send_keys(Keys.RETURN)
        time.sleep(1)
        
   
