from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.keys import Keys

def middle_d(driver, Inp_okt, Inp_mm):
    Oktas = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "//div[@id='cloud_cover_oktas_m']//i[@aria-label='icon: down']//*[name()='svg']")))
    Oktas.click()
    Oktas2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_cover_oktas_m"]/div/div/div[2]/div/input')))
    Oktas2.send_keys(str(Inp_okt))
    Oktas2.send_keys(Keys.RETURN)
    
    try:
        # JAM 12
        mm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='rainfall_last_mm']")))
        mm.clear()
        mm.send_keys(str(Inp_mm))
    except JavascriptException:
        pass    
