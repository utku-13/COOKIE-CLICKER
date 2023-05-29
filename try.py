from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep,time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/Users/utkuozer/chromedriver"

optns = webdriver.ChromeOptions()
optns.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=optns,service=Service(executable_path=path,log_path="NUL"))

driver.get("https://orteil.dashnet.org/cookieclicker/")

# lang_sel = driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')

# lang_sel.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
        )
    element.click()
except:
    driver.quit()

sleep(2)

# n = 0
# while True:
#     start_time = time() 
while True:   
    start_time = time()
    while True:
        driver.find_element(By.XPATH,'//*[@id="bigCookie"]').click()
        if time() - start_time > 5:  # check if 5 seconds have passed
            break
    sleep(1)
    #buying code!
    cursor = driver.find_elements(By.CLASS_NAME, "enabled")
    # 3 class isminden biri olan enable i cagirdik cunku unique olan oydu.
    cursor[-1].click()
    



    
