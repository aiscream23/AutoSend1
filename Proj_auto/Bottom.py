from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import JavascriptException, TimeoutException
import time

def Bottom_d(driver, Inp_Penguapan, Inp_IE, Inp_Jam, Inp_tanah):

    Penguapan = Inp_Penguapan
    IE = Inp_IE
    Jam = Inp_Jam
    Tanah = Inp_tanah

    try:
        # JAM 00
        Penguapan1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="evaporation_24hours_mm_eee"]')))
        Penguapan1.clear()
        Penguapan1.send_keys(str(Penguapan))
        time.sleep(2)
    except JavascriptException:
        pass
    
    try:
        IE1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="evaporation_eq_indicator_ie"]/div/span/i/svg')))
        IE1.click()
        time.sleep(2)
        IE2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="evaporation_eq_indicator_ie"]/div/div/div[2]/div/input')))
        IE2.send_keys(str(IE))
        IE2.send_keys(Keys.RETURN)
        time.sleep(2)
    except JavascriptException:
        pass
    except TimeoutException:
        pass

    try:
        Jam1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sunshine_h_sss"]')))
        Jam1.clear()
        Jam1.send_keys(str(Jam))
        time.sleep(2)
    except JavascriptException:
        pass
    except TimeoutException:
        pass

    Tanah1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='land_cond']//div[@role='combobox']")))
    Tanah1.click()
    Tanah2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="land_cond"]/div/div/div[2]/div/input')))
    Tanah2.send_keys(str(Tanah))
    Tanah2.send_keys(Keys.RETURN)
    time.sleep(2)






