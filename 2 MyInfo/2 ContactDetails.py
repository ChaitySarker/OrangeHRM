from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Contacts:
    def Test_Contact_Details(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Elements
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.NAME, "txtPassword")
        login_btn = driver.find_element(By.ID, "btnLogin")

        # Login_Action

        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My_info_click
        driver.find_element(By.ID, 'menu_pim_viewMyDetails').click()

        # Click Contact Details
        driver.find_element(By.XPATH, '//*[@id="sidenav"]/li[2]/a').click()

        # Input Field

        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()

        addressStreet1 = driver.find_element(By.ID, 'contact_street1')
        addressStreet1.clear()
        addressStreet1.send_keys('House-7,Road-2/c,Baridhara')

        addressStreet2 = driver.find_element(By.ID, 'contact_street2')
        addressStreet2.clear()
        addressStreet2.send_keys('Block - J')

        city = driver.find_element(By.ID, 'contact_city')
        city.clear()
        city.send_keys('Gulshan')

        State = driver.find_element(By.ID, 'contact_province')
        State.clear()
        State.send_keys('Dhaka')

        PostalCode = driver.find_element(By.ID, 'contact_emp_zipcode')
        PostalCode.clear()
        PostalCode.send_keys('1212')

        Country = driver.find_element(By.ID, 'contact_country')
        sel = Select(Country)
        sel.select_by_value('BD')
        time.sleep(5)

        HomeTele = driver.find_element(By.ID, 'contact_emp_hm_telephone')
        HomeTele.clear()
        HomeTele.send_keys('45468458')

        Mobile = driver.find_element(By.ID, 'contact_emp_mobile')
        Mobile.clear()
        Mobile.send_keys('0172636965')

        WorkTele = driver.find_element(By.ID, 'contact_emp_work_telephone')
        WorkTele.clear()
        WorkTele.send_keys('112-898-7612')

        WorkEmail = driver.find_element(By.ID, 'contact_emp_work_email')
        WorkEmail.clear()
        WorkEmail.send_keys('paul1@osohrm.com')

        OtherEmail = driver.find_element(By.ID, 'contact_emp_oth_email')
        OtherEmail.clear()
        OtherEmail.send_keys('pasdghul1@osohrm.com')
        time.sleep(3)

        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()
        time.sleep(3)

        # add Attachment
        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Bristy\\Desktop\\Pic\\Girl.jpg')

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('Hello')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(3)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()

        driver.close()


test_obj = Contacts()
test_obj.Test_Contact_Details()
