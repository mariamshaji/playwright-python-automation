from playwright.sync_api import Page,expect
from utilities.configreader import ConfigReader


class CartPage:
    def __init__(self, page:Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        


    def checkout(self):
        self.checkout_button.click()
        config_readerobj = ConfigReader()
        carturl = config_readerobj.config_reader("basic info" ,"checkout_url")
        expect(self.page).to_have_url(carturl)