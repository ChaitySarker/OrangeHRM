from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Personal:
    def Test_Personal_Details(self):
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

        # Click_PersonalDetails
        driver.find_element(By.LINK_TEXT, 'Personal Details').click()

        # Edit Field
        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()

        # Full Name
        FirstName = driver.find_element(By.ID, 'personal_txtEmpFirstName')
        FirstName.clear()
        FirstName.send_keys('Poul')

        MiddleName = driver.find_element(By.ID, 'personal_txtEmpMiddleName')
        MiddleName.clear()
        MiddleName.send_keys('jou')

        lastName = driver.find_element(By.ID, 'personal_txtEmpLastName')
        lastName.clear()
        lastName.send_keys('Mark')

        EmployeeId = driver.find_element(By.ID, 'personal_txtEmployeeId')
        EmployeeId.clear()
        EmployeeId.send_keys('263646')

        OtherId = driver.find_element(By.ID, 'personal_txtOtherID')
        OtherId.clear()
        OtherId.send_keys('161515')

        DriversLicenseNumber = driver.find_element(By.ID, 'personal_txtLicenNo')
        DriversLicenseNumber.clear()
        DriversLicenseNumber.send_keys('12121')

        LicenseExpiryDate = driver.find_element(By.ID, 'personal_txtLicExpDate')
        LicenseExpiryDate.clear()
        LicenseExpiryDate.send_keys('2025-06-30')
        time.sleep(2)

        SSN_Number = driver.find_element(By.ID, 'personal_txtNICNo')
        SSN_Number.clear()
        SSN_Number.send_keys('1234')

        SIN_Number = driver.find_element(By.ID, 'personal_txtSINNo')
        SIN_Number.clear()
        SIN_Number.send_keys('4321')

        driver.find_element(By.ID, 'personal_optGender_2').click()

        MaritalStatus = driver.find_element(By.ID, 'personal_cmbMarital')
        sel = Select(MaritalStatus)
        sel.select_by_value('Single')
        time.sleep(2)

        Nationality = driver.find_element(By.ID, 'personal_cmbNation')
        sel = Select(Nationality)
        sel.select_by_value('15')
        time.sleep(2)

        DateOfBirth = driver.find_element(By.ID, 'personal_DOB')
        DateOfBirth.clear()
        DateOfBirth.send_keys('2000-03-10')
        time.sleep(2)

        NickName = driver.find_element(By.ID, 'personal_txtEmpNickName')
        NickName.clear()
        NickName.send_keys('jo')

        '''smoke = driver.find_element(By.ID, 'personal_chkSmokeFlag')
        smoke.click()
        time.sleep(2)'''

        MilitaryService = driver.find_element(By.ID, 'personal_txtMilitarySer')
        MilitaryService.clear()
        MilitaryService.send_keys('ifo30')

        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()
        time.sleep(3)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Bristy\\Desktop\\Pic\\Girl.jpg')
        time.sleep(5)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('personal Details')
        time.sleep(2)

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()
        time.sleep(5)

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        time.sleep(5)

        driver.close()


test_obj = Personal()
test_obj.Test_Personal_Details()
