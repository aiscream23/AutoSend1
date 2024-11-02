from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def AwanRendah(driver, Opsi, Opsi2, Opsi3, Opsi4, Opsi5, Opsi6, Opsi7, Opsi8, Opsi9):
    CL = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_low_type_cl']//i[@aria-label='icon: down']//*[name()='svg']")))
    
    time.sleep(0.5)
    CL.click()

    """
    Opsi = 2 #2 awan kumulus, 5 awan sc
    Opsi2 = 2 #Jumlah awan rendah yang menutupi langit dalam oktas
    Opsi3 = 8 #Jenis awan C untuk jenis awan rendah
    Opsi4 = 2 #Jumlah awan rendah untuk jenis awan C yang dipilih dalam oktas
    Opsi5 = 480 #Tinggi dasar untuk jenis awan C yang dipilih dalam meter
    Opsi6 = 2400 #Tinggi puncak untuk jenis awan rendah (Cu atau Cb) yang dipilih dalam meter
    Opsi7 = 0 # Arah dari mana awan CL bergerak
    Opsi8 = 15 #Sudut elevasi puncak awan CL (Cu atau Cb)
    Opsi9 = 0 #Arah sebenarnya dari awan orografik atau awan konvektif terlihat
    """

    if Opsi == 0:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[normalize-space()='0 - tidak ada awan C1']")))
        CL2.click()
    elif Opsi == 1:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'1 - cumulus humilis atau fracto cumulus atao kedua')]")))
        CL2.click()
    elif Opsi == 2:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'2 - cumulus mediocris atau congestus, disertai ata')]")))
        CL2.click()

        #ini yang dipakai
        NCL21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_low_cover_oktas']//i[@aria-label='icon: down']//*[name()='svg']")))
        NCL21.click()
        NCL22 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_low_cover_oktas']//input[@class='ant-select-search__field']")))
        NCL22.send_keys(str(Opsi2))
        NCL22.send_keys(Keys.RETURN)
       
        time.sleep(1)        
        #ini yang dipakai
        NCL31 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/i[1]/*[name()='svg'][1]")))
        NCL31.click()
        NCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[3]/div/div/div/div[2]/div/input')))           
        NCL3.send_keys(str(Opsi3))
        NCL3.send_keys(Keys.RETURN)

        time.sleep(1)       
        #ini yang dipakai
        NCL41 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]")))
        NCL41.click()
        NCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[4]/div/div/div/div[2]/div/input')))
        NCL4.send_keys(str(Opsi4))
        NCL4.send_keys(Keys.RETURN)
 
        TDA = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='cloud_low_base_1']")))
        TDA.clear()
        TDA.send_keys(str(Opsi5))

        TPA = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='cloud_low_peak_1']")))
        TPA.clear()
        TPA.send_keys(str(Opsi6))

        DD = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/span[1]/i[1]/*[name()='svg'][1]")))
        DD.click()

        DD2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select ant-select-open ant-select-focused ant-select-enabled is-valid']//input[@class='ant-select-search__field']")))
        DD2.send_keys(str(Opsi7))
        DD2.send_keys(Keys.RETURN)  

        DEG = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]")))
        DEG.click()
        DEG2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_elevation_1_angle_ec']//input[@class='ant-select-search__field']"))) 
        DEG2.send_keys(str(Opsi8))
        DEG2.send_keys(Keys.RETURN)

        DD3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[9]/div/div/div')))
        DD3.click()
        DD4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[9]/div/div/div/div/div/input')))
        DD4.send_keys(str(Opsi9))
        DD4.send_keys(Keys.RETURN)
                    
    elif Opsi == 3:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'3 - cumulunimbus tanpa landasan, disertai atau tid')]")))
        CL2.click()
    elif Opsi == 4:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'4 - stratocumulus yang terjadi dari bentangan cumu')]")))
        CL2.click()
    elif Opsi == 5:
        CL2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'5 - stratocumulus yang tidak terjadi dari bentanga')]")))
        CL2.click()

        #ini yang dipakai
        NCL21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_low_cover_oktas']//i[@aria-label='icon: down']//*[name()='svg']")))
        time.sleep(0.5)
        NCL21.click()
        time.sleep(0.5)
        NCL22 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_low_cover_oktas']//input[@class='ant-select-search__field']")))
        NCL22.send_keys(str(Opsi2))
        NCL22.send_keys(Keys.RETURN)
        
        time.sleep(1)        
        #ini yang dipakai
        NCL31 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/i[1]/*[name()='svg'][1]")))
        time.sleep(0.5)
        NCL31.click()
        time.sleep(0.5)
        NCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[3]/div/div/div/div[2]/div/input')))           
        NCL3.send_keys(str(Opsi3))
        NCL3.send_keys(Keys.RETURN)

        time.sleep(1)       
        #ini yang dipakai
        NCL41 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]")))
        time.sleep(0.5)
        NCL41.click()
        time.sleep(0.5)
        NCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[4]/div/div/div/div[2]/div/input')))
        NCL4.send_keys(str(Opsi4))
        NCL4.send_keys(Keys.RETURN)
       
        TDA = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='cloud_low_base_1']")))
        TDA.clear()
        TDA.send_keys(str(Opsi5))

        DD = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[7]/div[1]/div[1]/span[1]/i[1]/*[name()='svg'][1]")))
        DD.click()

        DD2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collapse-row-2"]/div/div[2]/div[7]/div/div/div/div[2]/div/input')))
        DD2.send_keys(str(Opsi7))
        time.sleep(2)
        DD2.send_keys(Keys.RETURN)
    elif Opsi == 6:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[normalize-space()='6 - stratus']")))
        CL2.click()
    elif Opsi == 7:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'7 - fraktostratus atau fraktocumulus yang menyerta')]")))
        CL2.click()
    elif Opsi == 8:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'8 - cumulus dan stratocumulus yang tidak terjadi d')]")))
        CL2.click()
    elif Opsi == 9:
        CL2 = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'9 - cumulunimbus, biasanya berlandasan disertai at')]")))
        CL2.click()
    else:
        pass
