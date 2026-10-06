from playwright.sync_api import Page,expect
import time


class AboutPage:
    def __init__(self,page:Page):
        self.page = page
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.about_menu = page.locator("#about_sidebar_link")


    def about_page(self):
        self.menu_button.click()
        self.about_menu.click()
        self.page.go_back()
        time.sleep(2)
        

        