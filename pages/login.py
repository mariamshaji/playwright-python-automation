from playwright.sync_api import Page,expect
from utilities.configreader import ConfigReader
import time





class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_placeholder('Username')
        self.password_input = page.get_by_placeholder('Password')
        self.login_button = page.get_by_role('button' , name = 'Login')



    def login_function(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        time.sleep(2)

        config_readerobj = ConfigReader()
        dashboardurl = config_readerobj.config_reader("basic info" ,"dashboard_url")
        expect(self.page).to_have_url(dashboardurl)
