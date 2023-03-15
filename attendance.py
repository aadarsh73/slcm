from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random as r
from selenium.webdriver.support.ui import Select
from pymongo import MongoClient
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome_driver_path = "C:/Users/MAHE/Downloads/chromedriver_win32"
chromeOptions = Options()
# chromeOptions.headless = True

df = pd.read_csv("attendance.csv")
y = df.iloc[:,-1:]


def fetch_url(url, driver):
    try:
        print("fetching url...")
        return driver.get(url)
        print("url fetched successfully!")
    except:
        t = r.randint(5,10)
        print("Error, retrying in ",t," seconds...")
        time.sleep(t)
        fetch_url(url, driver)

def scraper():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        fetch_url("https://slcm.manipal.edu", driver)
        curr_url = 'https://slcm.manipal.edu/FacultyHome.aspx'
        # username = driver.find_element(By.XPATH,'//*[@id="txtUserid"]')
        # password = driver.find_element(By.XPATH,'//*[@id="txtpassword"]')
        
        
        while driver.current_url!= curr_url:
            time.sleep(1)
            print(driver.current_url)
        print("got url")
        time.sleep(2)


        #attendance 
        number = y.shape[0]

        for i in range(number):
            r = f'{i}'
            check_path = '//*[@id="ContentPlaceHolder1_grdAttendanceDetails_chkEmp_',r,'"]'
            reg_path = '//*[@id="ContentPlaceHolder1_grdAttendanceDetails_grdlblStudentNo_',r,'"]'

            if (y['attd'][i]=='A'):
                try:
                    driver.find_element(By.XPATH,reg_path)
                    driver.find_element(By.XPATH,check_path).click()
                except:
                    print("error")

                

        # xpath: "//*[@id="ContentPlaceHolder1_grdAttendanceDetails_chkEmp_0"]"
        #     "//*[@id="ContentPlaceHolder1_grdAttendanceDetails_chkEmp_1"]"

        # css : #ContentPlaceHolder1_grdAttendanceDetails_chkEmp_0
        #     #ContentPlaceHolder1_grdAttendanceDetails_chkEmp_1

        # reg no :  css : #ContentPlaceHolder1_grdAttendanceDetails_grdlblStudentNo_0
        #                 #ContentPlaceHolder1_grdAttendanceDetails_grdlblStudentNo_1
        # xpath : //*[@id="ContentPlaceHolder1_grdAttendanceDetails_grdlblStudentNo_0"]
        # //*[@id="ContentPlaceHolder1_grdAttendanceDetails_grdlblStudentNo_1"]

        
        

        # driver.quit()
    except Exception as e:
        time.sleep(10)
        print(e)
        print("error, fetching data, trying again...")
        time.sleep(100)
        # driver.quit()
        # scraper()
    
scraper()

# after getting endsem 

back = '//*[@id="lnkback"]'
#  close grade tab 