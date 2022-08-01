from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Dependents:
    def Test_Dependents(self):
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

        # Dependents
        driver.find_element(By.LINK_TEXT, 'Dependents').click()

        add = driver.find_element(By.ID, 'btnAddDependent')
        add.click()

        name = driver.find_element(By.ID, 'dependent_name')
        name.click()
        name.send_keys('auro')

        Relationship = driver.find_element(By.ID, 'dependent_relationshipType')
        sel = Select(Relationship)
        sel.select_by_value('Child')
        time.sleep(5)

        DateOfBirth = driver.find_element(By.ID, 'dependent_dateOfBirth')
        DateOfBirth.clear()
        DateOfBirth.send_keys('2000-06-12')
        time.sleep(3)

        save = driver.find_element(By.ID, 'btnSaveDependent')
        save.click()

        checkbox = driver.find_element(By.ID, 'checkAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'delDependentBtn')
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


test_obj = Dependents()
test_obj.Test_Dependents()