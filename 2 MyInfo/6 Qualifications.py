from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Qualifications:
    def Test_Qualifications(self):
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

        # Qualifications
        driver.find_element(By.LINK_TEXT, 'Qualifications').click()

        # Work Experience

        add = driver.find_element(By.ID, 'addWorkExperience')
        add.click()

        Company = driver.find_element(By.ID, 'experience_employer')
        Company.clear()
        Company.send_keys('Zoom')

        JobTitle = driver.find_element(By.ID, 'experience_jobtitle')
        JobTitle.clear()
        JobTitle.send_keys('SQA')

        From = driver.find_element(By.ID, 'experience_from_date')
        From.clear()
        From.send_keys('2015-12-19')

        To = driver.find_element(By.ID, 'experience_to_date')
        To.clear()
        To.send_keys('2020-12-02')

        Comment = driver.find_element(By.ID, 'experience_comments')
        Comment.clear()
        Comment.send_keys('Qualifications')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnWorkExpSave')
        save.click()

        cancel = driver.find_element(By.ID, 'btnWorkExpCancel')
        cancel.click()

        checkbox = driver.find_element(By.ID, 'workCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'delWorkExperience')
        delete.click()
        time.sleep(5)

        # LEVEL
        add1 = driver.find_element(By.ID, 'addEducation')
        add1.click()

        Level = driver.find_element(By.ID, 'education_code')
        sel = Select(Level)
        sel.select_by_value('2')
        time.sleep(2)

        Institute = driver.find_element(By.ID, 'education_institute')
        Institute.clear()
        Institute.send_keys('Uits')
        time.sleep(2)

        Specialization = driver.find_element(By.ID, 'education_major')
        Specialization.clear()
        Specialization.send_keys('CSE')
        time.sleep(2)

        Year = driver.find_element(By.ID, 'education_year')
        Year.clear()
        Year.send_keys('2020')
        time.sleep(2)

        GPA = driver.find_element(By.ID, 'education_gpa')
        GPA.clear()
        GPA.send_keys('3.33')

        StartDate = driver.find_element(By.ID, 'education_start_date')
        StartDate.clear()
        StartDate.send_keys('2016-12-25')
        time.sleep(2)

        EndDate = driver.find_element(By.ID, 'education_end_date')
        EndDate.clear()
        EndDate.send_keys('2020-12-25')
        time.sleep(2)

        save1 = driver.find_element(By.ID, 'btnEducationSave')
        save1.click()

        cancel1 = driver.find_element(By.ID, 'btnEducationCancel')

        checkbox1 = driver.find_element(By.ID, 'educationCheckAll')
        status = checkbox1.is_selected()
        if not status:
            checkbox1.click()
        time.sleep(5)

        delete1 = driver.find_element(By.ID, 'delEducation')
        delete1.click()
        time.sleep(5)

        # Skill
        add2 = driver.find_element(By.ID, 'addEducation')
        add2.click()

        Skill = driver.find_element(By.ID, 'skill_code')
        sel = Select(Skill)
        sel.select_by_value('14')
        time.sleep(2)

        Years_of_Experience = driver.find_element(By.ID, 'skill_years_of_exp')
        Years_of_Experience.clear()
        Years_of_Experience.send_keys('2 Years')
        time.sleep(2)

        comments1 = driver.find_element(By.ID, 'skill_comments')
        comments1.clear()
        comments1.send_keys('My Skill')

        save2 = driver.find_element(By.ID, 'btnSkillSave')
        save2.click()

        cancel2 = driver.find_element(By.ID, 'btnSkillCancel')
        cancel2.click()

        checkbox2 = driver.find_element(By.ID, 'skillCheckAll')
        status = checkbox2.is_selected()
        if not status:
            checkbox2.click()
        time.sleep(5)

        delete1 = driver.find_element(By.ID, 'delSkill')
        delete1.click()
        time.sleep(5)

        # Language
        add3 = driver.find_element(By.ID, 'addLanguage')
        add3.click()

        Language = driver.find_element(By.ID, 'language_code')
        sel = Select(Language)
        sel.select_by_value('3')
        time.sleep(2)

        Fluency = driver.find_element(By.ID, 'language_lang_type')
        sel = Select(Fluency)
        sel.select_by_value('3')
        time.sleep(2)

        Competency = driver.find_element(By.ID, 'language_competency')
        sel = Select(Competency)
        sel.select_by_value('3')
        time.sleep(2)

        Comment2 = driver.find_element(By.ID, 'language_comments')
        Comment2.clear()
        Comment2.send_keys('English')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnLanguageSave')
        save.click()

        cancel = driver.find_element(By.ID, 'btnLanguageCancel')

        checkbox3 = driver.find_element(By.ID, 'languageCheckAll')
        status = checkbox3.is_selected()
        if not status:
            checkbox3.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'delLanguage')
        delete.click()
        time.sleep(5)

        # License
        add3 = driver.find_element(By.ID, 'addLicense')
        add3.click()

        LicenseType = driver.find_element(By.ID, 'license_code')
        sel = Select(LicenseType)
        sel.select_by_value('6')
        time.sleep(2)

        LicenseNumber = driver.find_element(By.ID, 'license_license_no')
        LicenseNumber.clear()
        LicenseNumber.send_keys('263646')

        IssuedDate = driver.find_element(By.ID, 'license_date')
        IssuedDate.clear()
        IssuedDate.send_keys('2020-12-02')
        time.sleep(2)

        ExpiryDate = driver.find_element(By.ID, 'license_renewal_date')
        ExpiryDate.clear()
        ExpiryDate.send_keys('2023-12-02')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnLicenseSave')
        save.click()

        cancel = driver.find_element(By.ID, 'btnLicenseCancel')
        cancel.click()

        checkbox4 = driver.find_element(By.ID, 'licenseCheckAll')
        status = checkbox4.is_selected()
        if not status:
            checkbox4.click()
        time.sleep(5)

        delete = driver.find_element(By.ID, 'delLicense')
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
        comment.send_keys('Qualifications')
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


test_obj = Qualifications()
test_obj.Test_Qualifications()
