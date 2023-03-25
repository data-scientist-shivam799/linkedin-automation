for z in range(0,10):
    from selenium import webdriver
    import time
    time.sleep(10)
    driver = webdriver.Chrome('E:\RPA\chromedriver.exe')
    driver.get('https://www.linkedin.com')
    time.sleep(2)
    driver.maximize_window()

    #********** LOG IN *************

    username = driver.find_element_by_xpath("//input[@name='session_key']")
    password = driver.find_element_by_xpath("//input[@name='session_password']")
    username.send_keys('shivam799kumar@gmail.com')
    password.send_keys('7765955116')
    time.sleep(2)
    submit = driver.find_element_by_xpath("//button[@type='submit']").click()

    for m in range(0,6):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
    allButton=driver.find_elements_by_tag_name('button')
    likeButton=[i for i in allButton if i.text=='Like']
    print(likeButton)
    print('***')
    for j in likeButton:
        driver.execute_script("arguments[0].click();",j)
        time.sleep(3)

    time.sleep(2)
    driver.quit()