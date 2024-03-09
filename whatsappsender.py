from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver=webdriver.Chrome()

baseurl="https://web.whatsapp.com/"

driver.get(baseurl)

time.sleep(10)

with open('phone_nuumbers.csv',newline='') as csvf:
    rdc=csv.reader(csvf)
    for num in rdc:
        sameTab=(baseurl+"/send?phone=91"+str(num))
        driver.get(sameTab)
        time.sleep(5)
        content=driver.switch_to.active_element
        
        content.send_keys("hey skadooshhh")
        
        content.send_keys(Keys.RETURN)
        
        time.sleep(8)