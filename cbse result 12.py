from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
##import requests 
##from bs4 import BeautifulSoup 
import csv 
import time
#creating csv file
filename="cbse.csv"
#open csv file to write
f=open(filename,'w')
#creat header in file
header="NAME,STATUS,NUM\n"
f.write(header)
#put range of rollnumber
for i in range(9639428,9639432):
    #use try and exception because if any rollnumber is invalid then whole program is not stop.
    try:
        driver=webdriver.Chrome()
        #link is given above copy and paste
        driver.get("http://resultsarchives.nic.in/cbseresults/cbseresults2014/class12/cbse122014_total.htm")
       


        #put rollnumber
        driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/p/input[1]').send_keys(i)
        #view result xpath
        driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/p/input[2]').click()
        #student name
        name=driver.find_element_by_xpath('/html/body/div[2]/table[2]/tbody/tr[2]/td[2]/font/b').text
        #status pass or fail
        status=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[12]/td[2]/b[1]/font').text
        #first subject find xpath then next 4 subject
        m1=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[2]/td[5]/font').text
        m2=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[3]/td[5]/font').text
        m3=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[4]/td[5]/font').text
        m4=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[5]/td[5]/font').text
        m5=driver.find_element_by_xpath('/html/body/div[2]/div/center/table/tbody/tr[6]/td[5]/font').text
        #sum all marks
        num=str(int(m1)+int(m2)+int(m3)+int(m4)+int(m5))
        
               #all details fill into file
        f.write(name+","+status[9:]+","+num+"\n")
        driver.close()
    except NoSuchElementException as exception:
        continue
f.close()
