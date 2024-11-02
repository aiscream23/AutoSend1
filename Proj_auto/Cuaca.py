from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def cuaca(driver, Inp_ww, Inp_W11, Inp_W21):
    ww = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='present_weather_ww']//i[@aria-label='icon: down']//*[name()='svg']")))
    ww.click()

    ww1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="present_weather_ww"]/div/div/div[2]/div/input')))
    ww1.send_keys(str(Inp_ww))
    ww1.send_keys(Keys.RETURN)
    
    W1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='past_weather_w1']//i[@aria-label='icon: down']//*[name()='svg']")))
    W1.click()

    W11 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="past_weather_w1"]/div/div/div[2]/div/input')))
    W11.send_keys(str(Inp_W11))
    W11.send_keys(Keys.RETURN)
    
    W2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='past_weather_w2']//i[@aria-label='icon: down']//*[name()='svg']")))
    W2.click()

    W21 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="past_weather_w2"]/div/div/div[2]/div/input')))
    W21.send_keys(str(Inp_W21))
    W21.send_keys(Keys.RETURN)
   