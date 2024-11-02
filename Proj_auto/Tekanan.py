from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Tekanan(driver, Inp_qff, Inp_qfe):
    QFF = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_qff']")))
    QFF.clear()
    QFF.send_keys(str(Inp_qff))

    QFE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='input_qfe']")))
    QFE.clear()
    QFE.send_keys(str(Inp_qfe))