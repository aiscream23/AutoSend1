from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
import time

def Send(driver):

    time.sleep(3)
    preview = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Preview']")))
    preview.click()

    #ekstrak sandi sinopnya
    #SandiSinop = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-preview"]/tbody/tr[10]/td')))
    time.sleep(1)
    #dewpoint
    TD = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-preview"]/tbody/tr[6]/td[7]/label')))
    time.sleep(1)
    TD2 = TD.text
    time.sleep(1)
    #print(SandiSinop.text)
    print(TD2)
    
    time.sleep(3)
    try:
        Ok = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-preview___BV_modal_footer_"]/button')))
        Ok.click()
    except ElementClickInterceptedException:
        pass
    except TimeoutException:
        pass

    try:
        close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-preview___BV_modal_header_"]/button')))
        close.click()
    except ElementClickInterceptedException:
        pass
    except TimeoutException:
        pass
    except StaleElementReferenceException:
        pass
    
    
    #bagian sendnya, matikan komentar jika ingin send
    """time.sleep(1)
    send = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Send']")))
    time.sleep(1)
    send.click()

    time.sleep(1)
    sendGTS = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="send-gts-message___BV_modal_footer_"]/button[2]')))
    time.sleep(1)
    print('sendGTS sinop bisa')
    #sendGTS.click()

    time.sleep(1)
    sendGTSsucces = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
    time.sleep(1)
    sendGTSsucces.click()"""

    try:
        time.sleep(3)
        SubmitUpdate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']")))
        SubmitUpdate.click()
    except ElementClickInterceptedException:
        pass
    except TimeoutException:
        pass
    
    try:
        time.sleep(3)
        SubmitUpdate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']")))
        SubmitUpdate.click()
    except ElementClickInterceptedException:
        pass
    except TimeoutException:
        pass
        
    time.sleep(3)
    EditSucces = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
    time.sleep(3)
    EditSucces.click()
    
    time.sleep(5)
    return TD2
    
    
    
    

