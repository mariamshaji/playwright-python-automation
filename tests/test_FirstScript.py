import pytest
from pages.login import LoginPage
import time
from pages.homepage import HomePage
from pages.cartpage import CartPage
from pages.checkout import CheckoutPage
from pages.Finishorder import FinishPage
from pages.complete import CompletePage
from utilities.excelreader import ExcelUtility


@pytest.mark.usefixtures("page")
class TestE2Escenario:
    
    @pytest.mark.smoke
    def test_E2Escenario(self,page):

            #page.goto("/")
            login_object = LoginPage(page)
            excel_readerobj = ExcelUtility()
            username = excel_readerobj.getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4 ,2)
            password = excel_readerobj.getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4, 3)
            login_object.login_function(username,password)
            time.sleep(2)
        
            homepage_object = HomePage(page)
            homepage_object.navigate_to_products()
            

    
    
    @pytest.mark.regression
    def test_E2Escenario2(self,page):
        page.goto("/")
                        

            
                
        login_object = LoginPage(page)
        excel_readerobj = ExcelUtility()
        username = excel_readerobj.getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4 ,2)
        password = excel_readerobj.getCellData("testData/userInfo.xlsx" ,"Sheet 1", 4, 3)
        login_object.login_function(username,password)
        time.sleep(2)
                    
        homepage_object = HomePage(page)
        homepage_object.navigate_to_products()
        homepage_object.addtocart()
            
        cartpage_object = CartPage(page)
        cartpage_object.checkout()
            
        checkout_object = CheckoutPage(page)
        checkout_object.checkout_info()
            
        finishpage_object = FinishPage(page)
        finishpage_object.finish_order()
            
        complete_object = CompletePage(page)
        complete_object.text_assert()
        
        
        

   
