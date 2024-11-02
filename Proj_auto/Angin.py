from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def angin(driver, Inp_iw, Inp_dr, Inp_dr2, Inp_dr3):
    #Jam
    iw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='wind_indicator_iw']//i[@aria-label='icon: down']//*[name()='svg']")))
    iw.click()
    iw2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wind_indicator_iw"]/div/div/div[2]/div/input')))
    iw2.send_keys(str(Inp_iw))
    iw2.send_keys(Keys.RETURN)

    dr = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='wind_dir_deg_dd']")))
    dr.clear()
    dr.send_keys(str(Inp_dr))

    dr2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='wind_speed_ff']")))
    dr2.clear()
    dr2.send_keys(str(Inp_dr2))

    dr3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='visibility_vv']")))
    dr3.clear()
    dr3.send_keys(str(Inp_dr3))
        