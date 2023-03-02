from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import random as r
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup



chrome_driver_path = "/home/aadarsh/Development/chromedriver_linux64/chromedriver"
chromeOptions = Options()
# chromeOptions.headless = True

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
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chromeOptions)
        fetch_url("https://slcm.manipal.edu", driver)
        curr_url = 'https://slcm.manipal.edu/studenthomepage.aspx'
        # username = driver.find_element(By.XPATH,'//*[@id="txtUserid"]')
        # password = driver.find_element(By.XPATH,'//*[@id="txtpassword"]')
        
        
        while driver.current_url!= curr_url:
            time.sleep(1)
            print(driver.current_url)
        print("got url")
        time.sleep(2)

        # Admission Profile

        # Admission Details

        admission = driver.find_element(By.XPATH,'//*[@id="rtpchkMenu_lnkbtn2_0"]')
        admission.click()
        details = []
        name = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtNameAs12MarkCard"]').get_attribute('value')
        print(name)
        regno = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtApplicationNumber"]').get_attribute('value')
        print(regno)
        branch = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtProgramBranch"]').get_attribute('value')
        print(branch)
        mobile = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtStudentMobileNumberPresent"]').get_attribute('value')
        print(mobile)
        email = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtStudentEmailID"]').get_attribute('value')
        print(email)
        blood = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtBloodGroup"]').get_attribute('value')
        print(blood)
        dob = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtDOB"]').get_attribute('value')
        print(dob)

        print(name,regno,branch,mobile,email,blood,dob)
        details.extend([name,regno,branch,mobile,email,blood,dob])
        print(details)

        # Address Details

        address = driver.find_element(By.XPATH, '//*[@id="sub-tabs-list"]/li[3]/a')
        address.click()

        hostel = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtHostelBlock"]').get_attribute('value')
        print(hostel)
        room = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtHostelRoomNumber"]').get_attribute('value')
        print(room)

        details.extend([hostel,room])
        # Present Address

        present_address = {}
        present_address['mobile'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentMobile"]').get_attribute('value')
        present_address['email'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPesentEmail"]').get_attribute('value')
        present_address['al1'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentAddressLine1"]').get_attribute('value')
        present_address['al2'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentAddressLine2"]').get_attribute('value')
        present_address['al3'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentAddressLine3"]').get_attribute('value')
        present_address['place'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentPlace"]').get_attribute('value')
        present_address['country'] = driver.find_element(By.CSS_SELECTOR, 'option[selected="selected"]').text
        print(present_address['country'])
        present_address['state'] = driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_ddlPresentState > option[selected="selected"]').text
        print(present_address['state'])
        present_address['pin'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPresentPincode"]').get_attribute('value')
        print(present_address)
        # Permanent Address

        permanent_address = {}
        permanent_address['al1'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPermanentAddressLine1"]').get_attribute('value')
        permanent_address['al2'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPermanentAddressLine2"]').get_attribute('value')
        permanent_address['al3'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPermanentAddressLine3"]').get_attribute('value')
        permanent_address['place'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPlace"]').get_attribute('value')
        permanent_address['country'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtCountry"]').get_attribute('value')
        permanent_address['state'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtState"]').get_attribute('value')
        permanent_address['pin'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPincode"]').get_attribute('value')
        print(permanent_address)
        details.extend([present_address, permanent_address])

        # Parent Details

        # parents = driver.find_element(By.XPATH, '///*[@id="sub-tabs-list"]/li[5]/a')
        # parents.cick()
        father = {}
        father['name'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPFatherName"]').get_attribute('value')
        father['occupation'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtFatherOccupation"]').get_attribute('value')
        father['mobile'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtFatherContactNumber"]').get_attribute('value')
        father['email'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtFatherEmailID"]').get_attribute('value')
        print(father)
        mother = {}
        mother['name'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtPMotherName"]').get_attribute('value')
        mother['occupation'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtMotherOccupation"]').get_attribute('value')
        mother['mobile'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtMotherContactNumber"]').get_attribute('value')
        mother['email'] = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtMotherEmailID"]').get_attribute('value')
        print(mother)
        details.extend([father,mother])
        print(details)

        # Academic Details

        driver.find_element(By.XPATH, '//*[@id="rtpchkMenu_lnkbtn2_1"]').click()
        roll = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_lblRollNo"]').text
        print(roll)
        section = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_lblSection"]').text
        print(section)

        grades = {}
        
        internl = driver.find_element(By.XPATH, '//*[@id="sub-tabs-list"]/li[6]/a')
        internl.click()

        # select semester 

        # semester 1

        try :
            drop = Select(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlInternalSemester"]'))
        except :
            time.sleep(3)
            print('select button error')
            drop = Select(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlInternalSemester"]'))
        drop.select_by_visible_text('I')
        # driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_ddlInternalSemester > option:nth-child(2)').click()
        driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_lnkBtnInternalMark"]').click()
        time.sleep(10)   
        # get grades
        
        # print(driver.find_element(By.CSS_SELECTOR, '#accordion1 > div:nth-child(2) > div.panel-heading > h4 > a').get_attribute('href'))
        try :
            
            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[1]/div[1]/h4/a').get_attribute('href'))
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[1]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_0"]/b').text)
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_0"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[2]/div[1]/h4/a').get_attribute('href'))
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[2]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_1"]/b').text)
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_1"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[3]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_2"]/b').text)
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[3]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_2"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[4]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_3"]/b').text)
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[4]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_3"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[5]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_4"]/b').text)
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[5]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_4"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[6]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_5"]/b').text)
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[6]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            grades[sub_code] = []
            grades[sub_code].append(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_5"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[7]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_6"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[8]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_7"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[9]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_8"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[10]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_9"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[11]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_10"]/b').text)
        except:
            print("No more grades for semester 1")


        # semester 2

        drop = Select(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlInternalSemester"]'))
        drop.select_by_visible_text('II')
        # driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_ddlInternalSemester > option:nth-child(2)').click()
        driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_lnkBtnInternalMark"]').click()
        time.sleep(10)   
        # get grades
        
        # print(driver.find_element(By.CSS_SELECTOR, '#accordion1 > div:nth-child(2) > div.panel-heading > h4 > a').get_attribute('href'))
        try :
            
            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[1]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_0"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[2]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_1"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[3]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_2"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[4]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_3"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[5]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_4"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[6]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_5"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[7]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_6"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[8]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_7"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[9]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_8"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[10]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_9"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[11]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_10"]/b').text)
        except:
            print("No more grades for semester 2")

        # semester 3

        drop = Select(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlInternalSemester"]'))
        drop.select_by_visible_text('III')
        # driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_ddlInternalSemester > option:nth-child(2)').click()
        driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_lnkBtnInternalMark"]').click()
        time.sleep(10)   
        # get grades
        
        # print(driver.find_element(By.CSS_SELECTOR, '#accordion1 > div:nth-child(2) > div.panel-heading > h4 > a').get_attribute('href'))
        try :
            
            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[1]/div[1]/h4/a').get_attribute('href'))
            sub_code = driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[1]/div[1]/h4/a').get_attribute('href').split('#')[1]
            print(sub_code)
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_0"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[2]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_1"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[3]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_2"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[4]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_3"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[5]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_4"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[6]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_5"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[7]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_6"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[8]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_7"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[9]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_8"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[10]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_9"]/b').text)

            print(driver.find_element(By.XPATH, '//*[@id="accordion1"]/div[11]/div[1]/h4/a').get_attribute('href'))
            print(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_RepeaterPrintInternal_lblTotal_10"]/b').text)
        except:
            print("No more grades for semester 3")

        # grade sheet
        current_url = driver.current_url
        print(current_url)
        time.sleep(5);
        academic_details = driver.find_element(By.XPATH, '//*[@id="rtpchkMenu_lnkbtn2_1"]')
        academic_details.click()
        grade_page = driver.find_element(By.XPATH, '//*[@id="sub-tabs-list"]/li[7]/a')
        grade_page.click()
        time.sleep(2)
        # chwd = driver.window_handles
        # for w in chwd:
        #     driver.switch_to.window(w)
        #     if(driver.get(curr_url)==current_url):
        #         print("waiting for page to load")
        #         time.sleep(2)
        # print(driver.get(curr_url))
    
        # time.sleep(5)

        
        
        print(driver.current_url,'test1')
        chwd = driver.window_handles
        for w in chwd:
            driver.switch_to.window(w)
            if(driver.current_url==current_url):
                print("waiting for page to load")
                time.sleep(2)
            elif(driver.current_url=='https://slcm.manipal.edu/GradeSheet.aspx'):
                break
        print(driver.current_url,'test2')
        drop = Select(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlSemester"]'))
        drop.select_by_visible_text('I')
        
        time.sleep(5)
        data = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr td span')
        print(len(data))
        sem1 = []
        for x in data:
            print(x.text)
            sem1.append(x.text)
        while("" in sem1):
            sem1.remove("")
        print("cleaned : ")
        for x in sem1:
            print(x)
        
        print(len(sem1))
            
        print(sem1)
        i=0
        for j in range(len(sem1)):
            
            x = sem1[i].split(" ")
            # print(x)
            y = x[0]+x[1]
            # print(y)
            grades[y].append(sem1[i])
            grades[y].append(sem1[i+1])
            grades[y].append(sem1[i+3])
            grades[y].append(sem1[i+4])
            print(grades[y])
            i=i+5;

        print(grades)
        # driver.quit()
    except Exception as e:
        time.sleep(10)
        print(e)
        print("error, fetching data, trying again...")
        time.sleep(100)
        # driver.quit()
        # scraper()
    
scraper()

