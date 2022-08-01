from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains


class Candidates:
    def Test_Candidates(self):
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

        # Recruitment_click
        Recruitment = driver.find_element(By.ID, 'menu_recruitment_viewRecruitmentModule')
        try:
            actions = ActionChains(driver)
            actions.move_to_element(Recruitment).perform()

            candidates= driver.find_element(By.ID, 'menu_recruitment_viewCandidates')
            candidates.click()
            time.sleep(5)

        except:
            print('Mouse Hover Actions Field')

        # Candidates
        JobTitle = driver.find_element(By.ID, 'candidateSearch_jobTitle')
        sel = Select(JobTitle)
        sel.select_by_value('7')
        time.sleep(2)

        Vacancy = driver.find_element(By.ID, 'candidateSearch_jobVacancy')
        sel = Select(Vacancy)
        sel.select_by_value('1')
        time.sleep(2)

        HiringManager = driver.find_element(By.ID, 'candidateSearch_hiringManager')
        sel = Select(HiringManager)
        sel.select_by_value('2')
        time.sleep(2)

        Status = driver.find_element(By.ID, 'candidateSearch_status')
        sel = Select(Status)
        sel.select_by_value('APPLICATION INITIATED')
        time.sleep(2)

        CandidateName = driver.find_element(By.ID, 'candidateSearch_candidateName')
        CandidateName.clear()
        CandidateName.send_keys('John')
        time.sleep(2)

        Keywords = driver.find_element(By.ID, 'candidateSearch_keywords')
        Keywords.clear()
        Keywords.send_keys('Hello')
        time.sleep(2)

        # Date of Application
        From = driver.find_element(By.ID, 'candidateSearch_fromDate')
        From.clear()
        From.send_keys('2022-06-10')
        time.sleep(2)

        To = driver.find_element(By.ID, 'candidateSearch_toDate')
        To.clear()
        To.send_keys('2022-07-10')
        time.sleep(2)

        Method_of_Application = driver.find_element(By.ID, 'candidateSearch_modeOfApplication')
        sel = Select(Method_of_Application)
        sel.select_by_value('1')
        time.sleep(2)

        Search = driver.find_element(By.ID, 'btnSrch')
        Search.click()


        add = driver.find_element(By.ID, 'btnAdd')
        add.click()

        FirstName = driver.find_element(By.ID, 'addCandidate_firstName')
        FirstName.clear()
        FirstName.send_keys('Poul')

        MiddleName = driver.find_element(By.ID, 'addCandidate_middleName')
        MiddleName.clear()
        MiddleName.send_keys('jou')

        lastName = driver.find_element(By.ID, 'addCandidate_lastName')
        lastName.clear()
        lastName.send_keys('Mark')

        Email = driver.find_element(By.ID, 'addCandidate_email')
        Email.clear()
        Email.send_keys('admin@gmail.com')

        ContactNo = driver.find_element(By.ID, 'addCandidate_contactNo')
        ContactNo.clear()
        ContactNo.send_keys('01717263646')

        JobVacancy = driver.find_element(By.ID, 'addCandidate_vacancy')
        sel = Select(JobVacancy)
        sel.select_by_value('6')
        time.sleep(2)

        Resume = driver.find_element(By.ID, 'addCandidate_resume')
        Resume.send_keys('C:\\Users\\Bristy\\Desktop\\Pic\\Girl.jpg')
        time.sleep(5)

        Keywords = driver.find_element(By.ID, 'addCandidate_keyWords')
        Keywords.clear()
        Keywords.send_keys('Hello')
        time.sleep(2)

        Comment = driver.find_element(By.ID, 'addCandidate_comment')
        Comment.clear()
        Comment.send_keys('yeap')
        time.sleep(2)

        DateOfApplication = driver.find_element(By.ID, 'addCandidate_appliedDate')
        DateOfApplication.clear()
        DateOfApplication.send_keys('2022-06-10')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(5)

        driver.close()


test_obj = Candidates()
test_obj.Test_Candidates()
