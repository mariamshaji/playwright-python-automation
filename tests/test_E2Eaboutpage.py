from playwright.sync_api import Page
from pages.about import AboutPage
from pages.login import LoginPage
from utilities.excelreader import ExcelUtility
import time




def test_about(page : Page):


    page.goto("https://www.saucedemo.com/")

    excel_obj = ExcelUtility()
    username = excel_obj.getCellData("testData/userInfo.xlsx","Sheet 1",4, 2)
    password = excel_obj.getCellData("testData/userInfo.xlsx" , "Sheet 1" , 4, 3)
    login_obj = LoginPage(page)
    login_obj.login_function(username,password)
    time.sleep(1)





    about_obj = AboutPage(page)
    about_obj.about_page()
