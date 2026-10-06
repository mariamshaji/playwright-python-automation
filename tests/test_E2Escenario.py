from playwright.sync_api import Page
from pages.login import LoginPage
from pages.homepage import HomePage
from pages.cartpage import CartPage
from pages.checkout import CheckoutPage
from pages.Finishorder import FinishPage
from pages.complete import CompletePage
from utilities.excelreader import getCellData

import time



def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")



    username = getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4 ,2)
    password = getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4, 3)
    login_object = LoginPage(page)
    login_object.login_function(username,password)
    time.sleep(2)

    homepage_object = HomePage(page)
    homepage_object.addtocart()

    cartpage_object = CartPage(page)
    cartpage_object.checkout()

    checkout_object = CheckoutPage(page)
    checkout_object.checkout_info()

    finishpage_object = FinishPage(page)
    finishpage_object.finish_order()

    complete_object = CompletePage(page)
    complete_object.text_assert()


