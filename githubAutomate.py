import sys
import os
import credentials as cd
from selenium import webdriver #pip3 install selenium
from time import sleep

projectName = str(sys.argv[1])
os.chdir('/home/ashwith/MyProjects/')
os.mkdir(projectName)
destPath = '/home/ashwith/MyProjects/'+projectName
os.chdir(destPath)

browser = webdriver.Chrome(executable_path='/home/ashwith/PythonProjects/chromedriver')

browser.get("https://github.com/login")
browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(cd.username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(cd.password)
browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]').click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary').click()
sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(projectName)
sleep(1)
browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()