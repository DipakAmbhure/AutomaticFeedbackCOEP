import random
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

import time

#Enter Datails Here
MIS = "UserMIS"
PASSWORD = "USERPASSWORD"

#2 IS FOR POOR
#3 FOR GOOD
#4 FOR VERY GOOD
choice = ['3','3','3']





#driver call  
#ENTER PATH TO CHROME DRIVER
driver=webdriver.Chrome(executable_path='D:\AVANTAR\PythonProjects\Automation\chromedriver_win32\chromedriver.exe')


#website call
driver.get("http://portal.coep.org.in:9093/FeedBackResponse") 
wait = WebDriverWait(driver, 3000) 


t=wait.until(EC.presence_of_element_located((By.ID, "UserName")))
t.send_keys(MIS)

t=wait.until(EC.presence_of_element_located((By.ID, "Password")))
t.send_keys(PASSWORD)
b=wait.until(EC.presence_of_element_located((By.ID, "btnSignIn")))
b.click()


b=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"sidebar-menu\"]/div/ul/li[2]/a")))
b.click()

b=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"sidebar-menu\"]/div/ul/li[2]/ul/li[1]/a")))
b.click()



t=wait.until(EC.presence_of_element_located((By.ID, "FeedBackId")))
input_box=driver.find_elements_by_name("FeedBackId")
for i in input_box:
    try:
        select=Select(i)
        select.select_by_value('4327')
    except:
        continue
    


flag=1

for j in range(2):



    wait.until(EC.presence_of_element_located((By.ID, "FeedBackRatingID")))
    input_box=driver.find_elements_by_name("FeedBackRatingID")

    count=0
    for i in input_box:
        try:
            select=Select(i)
            select.select_by_value(choice[random.randint(0,2)])
        except:
            continue

    if(flag):
        b=wait.until(EC.presence_of_element_located((By.ID, "btnSubmit1")))
        b.click()
        flag=0

while(True):
    1==1