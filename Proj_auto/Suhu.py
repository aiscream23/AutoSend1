from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, JavascriptException

def Suhu_d(driver, Inp_tbk, Inp_tbb, Inp_tmax, Inp_tmin):
    TBK = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='temp_drybulb_c_tttttt']")))
    TBK.clear()
    TBK.send_keys(str(Inp_tbk))

    TBB = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='temp_wetbulb_c']")))
    TBB.clear()
    TBB.send_keys(str(Inp_tbb))

    try:
        # JAM 12
        TMAX = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='temp_max_c_txtxtx']")))
        TMAX.clear()
        TMAX.send_keys(str(Inp_tmax))
    except JavascriptException:
        pass

    try:
        # JAM 00
        TMIN = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='temp_min_c_tntntn']")))
        TMIN.clear()
        TMIN.send_keys(str(Inp_tmin))
    except JavascriptException:
        pass
