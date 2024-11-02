from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def metar5(driver):

    time.sleep(3)
    preview = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Preview']")))
    preview.click()

    send = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Send']")))
    time.sleep(1.5)
    send.click()
    time.sleep(1.5)

    time.sleep(1)
    sendGTScancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="send-gts-message___BV_modal_header_"]/button'))) #ini cancel, kalau mau send tinggal ganti inspectnya jadi ok
    time.sleep(1)
    sendGTScancel.click()

    time.sleep(3)
    SubmitUpdate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']")))
    SubmitUpdate.click()

    time.sleep(3)
    EditSucces = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
    time.sleep(3)
    EditSucces.click()   
    time.sleep(3)