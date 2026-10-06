from playwright.sync_api import Page,expect
from utilities.configreader import ConfigReader



class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.product_added = page.locator("#add-to-cart-sauce-labs-backpack")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.all_products = page.locator('.inventory_item_name ')
        self.product_description = page.locator('.inventory_details_desc')
        



    def addtocart(self):
        self.product_added.click()
        self.shopping_cart.click()
        config_readerobj = ConfigReader()
        carturl = config_readerobj.config_reader("basic info" , "cart_url")
        expect(self.page).to_have_url(carturl)


    def navigate_to_products(self):
        for product in self.all_products.all():
            product.click()
            expect(self.product_description).to_be_visible()
            print(self.product_description.inner_text())
            self.page.go_back()

