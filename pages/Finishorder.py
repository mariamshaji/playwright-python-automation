from playwright.sync_api import Page,expect
from utilities.configreader import ConfigReader


class FinishPage:
    def __init__(self,page:Page):
        self.page = page
        self.finish_button = page.locator("#finish")
        


    def finish_order(self):
        self.finish_button.click()
        config_readerobj = ConfigReader()
        completeurl = config_readerobj.config_reader("basic info" , "complete_url")
        expect(self.page).to_have_url(completeurl)