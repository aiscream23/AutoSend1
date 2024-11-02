from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

def metar3(driver, coverCL, hCL, coverCM, hCM):

  #CL
    if coverCL < 3:
        coverCL2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/select[1]")))
        time.sleep(2)
        coverCL2.click() 

        coverCL2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]/option[2]')))
        coverCL2.click()

        coverCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_height"]')))
        coverCL3.clear()
        coverCL3.send_keys(str(hCL))

        coverCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-icon rounded-circle btn-success btn-sm']")))
        coverCL4.click()
        time.sleep(3)

    elif coverCL == 3:
        coverCL2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]')))
        coverCL2.click() 
        coverCL2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]/option[3]')))
        coverCL2.click()

        coverCL3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_height"]')))
        coverCL3.clear()
        coverCL3.send_keys(str(hCL))

        coverCL4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select-type"]')))
        coverCL4.click()
        coverCL5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select-type"]/option[2]')))
        coverCL5.click()

        coverCL6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__353"]/tbody/tr/td[4]/button/svg')))
        coverCL6.click()
        time.sleep(3)

    #CM
    if coverCM < 2:
        pass
    elif coverCM == 3 or coverCM == 4:
        coverCM2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]')))
        coverCM2.click()
        coverCM2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]/option[3]')))
        coverCM2.click()

        coverCM3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_height"]')))
        coverCM3.clear()
        coverCM3.send_keys(str(hCM))

        coverCM4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__353"]/tbody/tr/td[4]/button/svg')))
        coverCM4.click()
        time.sleep(5)
    elif 5 <= coverCM <= 7:
        coverCM2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]')))
        coverCM2.click()

        coverCM2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clouds-jumlah"]/option[4]')))
        coverCM2.click()

        coverCM3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloud_height"]')))
        coverCM3.clear()
        coverCM3.send_keys(str(hCM))

        coverCM4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-icon rounded-circle btn-success btn-sm']")))
        coverCM4.click()
        time.sleep(5)
