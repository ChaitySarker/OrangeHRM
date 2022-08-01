from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Immigration:
    def Test_Immigration(self):
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

        # Immigration
        driver.find_element(By.LINK_TEXT, 'Immigration').click()

        Document = driver.find_element(By.ID, 'immigration_type_flag_1')
        Document.click()

        Number = driver.find_element(By.ID, 'immigration_number')
        Number.clear()
        Number.send_keys('01717263696')

        IssuedDate = driver.find_element(By.ID, 'immigration_passport_issue_date')
        IssuedDate.clear()
        IssuedDate.send_keys('2022-01-01')
        time.sleep(2)

        ExpiryDate = driver.find_element(By.ID, 'immigration_passport_expire_date')
        ExpiryDate.clear()
        ExpiryDate.send_keys('2027-01-01')
        time.sleep(2)

        EligibleStatus = driver.find_element(By.ID, 'immigration_i9_status')
        EligibleStatus.clear()
        EligibleStatus.send_keys('Yes Eligible')

        IssuedBy = driver.find_element(By.ID, 'immigration_country')
        sel = Select(IssuedBy)
        sel.select_by_value('BD')
        time.sleep(2)

        EligibleReviewDate = driver.find_element(By.ID, 'immigration_i9_review_date')
        EligibleReviewDate.clear()
        EligibleReviewDate.send_keys('2022-06-25')
        time.sleep(2)

        Comments = driver.find_element(By.ID, 'immigration_comments')
        Comments.clear()
        Comments.send_keys('Immigration')

        save = driver.find_element(By.ID, 'btnSave')
        save.click()

        checkbox = driver.find_element(By.ID, 'immigrationCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'btnDelete')
        delete.click()
        time.sleep(5)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(5)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Bristy\\Desktop\\Pic\\Girl.jpg')
        time.sleep(5)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('Dependents')
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


test_obj = Immigration()
test_obj.Test_Immigration()
