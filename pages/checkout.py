from playwright.sync_api import Page,expect
from utilities.random_data import RandomDataClass
from utilities.configreader import ConfigReader


class CheckoutPage:
    def __init__(self,page:Page):
        self.page = page
        self.firstname = page.get_by_placeholder("First Name")
        self.lastname =  page.get_by_placeholder("Last Name")
        self.zipcode =  page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")
        
        


    def checkout_info(self):

        random_obj = RandomDataClass()
        firstname = random_obj.first_name()
        lastname = random_obj.last_name()
        zipcode = random_obj.get_zipcode()
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.zipcode.fill(zipcode)
        self.page.wait_for_timeout(2000)
        self.continue_button.click()
        config_readerobj = ConfigReader()
        finishurl = config_readerobj.config_reader("basic info" , "finish_url")
        expect(self.page).to_have_url(finishurl)