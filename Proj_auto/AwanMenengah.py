from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def AwanMenengah(driver, Opsim, Opsi2m, Opsi3m, Opsi4m, Opsi5m, Opsi6m):
    CL = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_med_type_cm']//i[@aria-label='icon: down']//*[name()='svg']")))
    time.sleep(0.5)
    CL.click()

    Opsi = Opsim #Jenis awan menengah
    Opsi2 = Opsi2m #Jumlah awan menengah yang menutupi langit dalam oktas
    Opsi3 = Opsi3m #Jenis awan C untuk jenis awan menengah
    Opsi4 = Opsi4m #Jumlah awan menengah untuk jenis awan C yang dipilih dalam oktas
    Opsi5 = Opsi5m #Tinggi dasar untuk jenis awan C yang dipilih dalam meter
    Opsi6 = Opsi6m #Arah dari mana awan CH bergerak
    
    if Opsi == 0:
        #pembuka aja ini
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[normalize-space()='0 - tidak ada awan C1']")))
        CL2.click()
    elif Opsi == 1:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'1 - cumulus humilis atau fracto cumulus atao kedua')]")))
        CL2.click()
    elif Opsi == 2:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_med_type_cm"]/div/div/div[2]/div/input')))
        CL2.send_keys(str(Opsi))
        CL2.send_keys(Keys.RETURN)

        NCL21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_med_cover_oktas"]/div/div')))
        time.sleep(0.5)
        NCL21.click()
        time.sleep(0.5)
        NCL22 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_med_cover_oktas"]/div/div/div[2]/div/input')))
        NCL22.send_keys(str(Opsi2))
        NCL22.send_keys(Keys.RETURN)
             
        NCL31 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/i[1]/*[name()='svg'][1]")))      
        time.sleep(0.5)
        NCL31.click()
        time.sleep(0.5)
        NCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[3]/div/div/div/div[2]/div/input)[2]')))
        NCL3.send_keys(str(Opsi3))
        NCL3.send_keys(Keys.RETURN)

        NCL41 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[4]/div/div/div)[2]')))
        time.sleep(0.5)
        NCL41.click()
        time.sleep(0.5)
        NCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[4]/div/div/div/div[2]/div/input)[2]')))
        NCL4.send_keys(str(Opsi4))
        NCL4.send_keys(Keys.RETURN)
        
        TDA = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_med_base_1"]')))
        TDA.clear()
        TDA.send_keys(str(Opsi5))
        
        DEG = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@id="collapse-row-2"]/div/div[2]/div[6]/div/div)[1]')))
        time.sleep(0.5)
        DEG.click()
        time.sleep(0.5)
        DEG2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[6]/div/div/div/div[2]/div/input'))) 
        DEG2.send_keys(str(Opsi6))
        DEG2.send_keys(Keys.RETURN)
   
