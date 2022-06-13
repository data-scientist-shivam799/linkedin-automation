from selenium import webdriver
import time
import pyautogui as pt
import random as rd

driver=webdriver.Chrome(executable_path='E:\RPA\chromedriver.exe')

driver.get('https://linkedin.com')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id('session_key').send_keys('xyz@email.com')
driver.find_element_by_id('session_password').send_keys('************')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button').click()
time.sleep(2)

for j in range(1,51):
    link='https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page='+str(j)
    driver.get(link)
    time.sleep(2)
    allButtons = driver.find_elements_by_tag_name('button')
    message_button = [i for i in allButtons if i.text == 'Message']
    for i in range(0,len(message_button)):
        driver.execute_script("arguments[0].click();",message_button[i])
        time.sleep(2)
        mainDiv=driver.find_element_by_xpath("//div[starts-with(@class,'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click();",mainDiv)
        time.sleep(5)
        paragraphs=driver.find_elements_by_tag_name('p')

        allSpan = driver.find_elements_by_tag_name("span")
        allSpan = [d for d in allSpan if d.get_attribute('aria-hidden') == 'true']
        greetings = ['Hello', 'Hi', 'Ahoy', 'Sup', 'Namaste']
        idx = [*range(16, 54, 4)]
        allName=[]

        for j in idx:
            firstName = allSpan[j].text.split(" ")[0]
            allName.append(firstName)

        rd_greetings = rd.randint(0, len(greetings) - 1)
        message=greetings[rd_greetings] + " " + allName[i] + ", how are you?"

        paragraphs[-5].send_keys(message)
        pt.press('enter')
        time.sleep(2)
        closeButton=driver.find_element_by_xpath("//button[starts-with(@data-control-name,'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();",closeButton)
        time.sleep(2)