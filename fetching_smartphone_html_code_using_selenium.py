import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

s = Service("C:/Users/Lenovo/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service= s)

driver.get("https://www.smartprix.com/mobiles")

time.sleep(3)

#  excluding out of stock phones
driver.find_element(by= By.XPATH, value= '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
#  only selecting smart phones
driver.find_element(by= By.XPATH, value= '//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/input').click()

time.sleep(3)

old_height = driver.execute_script("return document.body.scrollHeight")

while True:
    #  loading more phones by clicking on "LOAD MORE"
    driver.find_element(by= By.XPATH, value= '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()

    time.sleep(2)
    
    new_height= driver.execute_script("return document.body.scrollHeight")

    if old_height == new_height:
        break

    old_height = new_height

time.sleep(15)

# getting the html code
html_code = driver.page_source

#  opening a file in write mode and writing down html_code into it
with open("C:\\Users\\Lenovo\\Desktop\\smartphone.html","w", encoding= "utf-8") as object:
    object.write(html_code)