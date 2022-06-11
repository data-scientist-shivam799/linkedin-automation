# Importing required libraries
from selenium import webdriver
import time

# Path to chromedriver on your local machine
# Chrome version should be compatible with chromedriver
driver = webdriver.Chrome('E:\RPA\chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)
driver.maximize_window()

#********** LOG IN *************
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys('xyz@email.com')
password.send_keys('***************')
time.sleep(5)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()

# Looping for 50 pages
for j in range(1,51):
    # To obtain this URL go to linkedin search bar apply preferable filters and select second connections
    driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page='+str(j))
    # driver.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105080838%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=' + str(j))
    time.sleep(2)
    allButtons=driver.find_elements_by_tag_name('button')
    connectButtons=[i for i in allButtons if i.text=='Connect']
    for i in connectButtons:
        driver.execute_script("arguments[0].click();",i)
        time.sleep(2)
        send=driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        closeButton=driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", closeButton)
        time.sleep(2)