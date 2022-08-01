from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class OrangeHRM():
    def Test_login_valid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Elements
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.NAME, "txtPassword")
        login_btn = driver.find_element(By.ID, "btnLogin")
        forget_password = driver.find_element(By.LINK_TEXT, "Forgot your password?")


        #Login_Action

        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()


        time.sleep(5)

    def Test_login_invalid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

         # Find Elements
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.NAME, "txtPassword")
        login_btn = driver.find_element(By.ID, "btnLogin")
        forget_password = driver.find_element(By.LINK_TEXT, "Forgot your password?")

        # Login_Action

        username.clear()
        username.send_keys('Admin232')

        password.clear()
        password.send_keys('admin123456')

        login_btn.click()

        driver.close()


login_obj = OrangeHRM()
login_obj.Test_login_invalid()
login_obj.Test_login_valid()