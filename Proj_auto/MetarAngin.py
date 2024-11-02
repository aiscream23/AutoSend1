from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

#sekalian depe visibility

def metar2(driver, Inp_dr, Inp_dr2, Vis):

    vis2 = Vis*1000
    #Angin
    dr = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='winds-direction']")))
    dr.clear()
    dr.send_keys(str(Inp_dr))

    dr2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='pl-1 col-sm-4']//input[@id='wind_speed']")))
    dr2.clear()
    dr2.send_keys(str(Inp_dr2))

    dr2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='pl-1 col-sm-4']//input[@id='input-prevailing']")))
    dr2.clear()
    dr2.send_keys(str(vis2))

