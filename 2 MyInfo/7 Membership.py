from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Menbership:
    def Test_Menbership(self):
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

        # Menbership
        driver.find_element(By.LINK_TEXT, 'Memberships').click()

        # Assigned Memberships

        add = driver.find_element(By.ID, 'btnAddMembershipDetail')
        add.click()

        cancel = driver.find_element(By.ID, 'btnCancel')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAddMembershipDetail')
        add.click()

        Membership = driver.find_element(By.ID, 'membership_membership')
        sel = Select(Membership)
        sel.select_by_value('1')
        time.sleep(2)

        SubscriptionPaidBy = driver.find_element(By.ID, 'membership_subscriptionPaidBy')
        sel = Select(SubscriptionPaidBy)
        sel.select_by_value('Individual')
        time.sleep(2)

        SubscriptionAmount = driver.find_element(By.ID, 'membership_subscriptionAmount')
        SubscriptionAmount.clear()
        SubscriptionAmount.send_keys('1000')
        time.sleep(2)

        Currency = driver.find_element(By.ID, 'membership_currency')
        sel = Select(Currency)
        sel.select_by_value('USD')
        time.sleep(2)

        SubscriptionCommenceDate = driver.find_element(By.ID, 'membership_subscriptionCommenceDate')
        SubscriptionCommenceDate.clear()
        SubscriptionCommenceDate.send_keys('2020-12-25')
        time.sleep(2)

        SubscriptionRenewalDate = driver.find_element(By.ID, 'membership_subscriptionRenewalDate')
        SubscriptionRenewalDate.clear()
        SubscriptionRenewalDate.send_keys('2023-12-25')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnSaveMembership')
        save.click()

        checkbox = driver.find_element(By.ID, 'checkAllMem')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'delMemsBtn')
        delete.click()
        time.sleep(5)

        # Attachment
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
        comment.send_keys('Membership')
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

test_obj = Menbership()
test_obj.Test_Menbership()