from selenium import webdriver
import os

search = "Desert+Fox"
url = "https://www.google.com/search?q="+search+"&source=lnms&tbm=isch"

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get(url)

if not os.path.exists(search):
    os.mkdir(search)

cnt = 0

for _ in range(500):
    if cnt==1500:
        break
    temp = driver.find_elements_by_class_name("rg_i")
    for i in temp:
        i.screenshot("./"+search+"/"+str(cnt)+".png")
        cnt+=1
    driver.execute_script("window.scrollBy(0,10000)")

